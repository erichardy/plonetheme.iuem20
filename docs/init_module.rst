

.. include:: links.rst


==========================
La mise en place du module
==========================

Création du module
==================

Le module est créé avec l'utilitaire `mrbob`_::

   mrbob/bin/mrbob -O plonetheme.iuem20 bobtemplates:plone_addon

La structure mise en place par cet utilitaire a évolué et fait état de l'utilisation
d'une utilisation large de `grunt`_.

La description de cet outil est décrite dans le fichier ``HOWTO_DEVELOP.rst`` à la racine
du module.

**CEPENDANT**, ayant déjà mis en place des outils de développement avec `gulp`_,
j'ai préféré continuer avec ce dernier. D'où la présence d'un fichier ``gruntfile.js``.

.. note:: Les changements récents opérés par les développeurs de Plone dans la gestion
   des ressources JS et LESS/CSS
   ont été l'objet de divers tâtonnements de ma part... De ce fait, on constatera que les deux
   utilitaires ``grunt`` et ``gulp`` sont employés. Il serait bon d'unifier
   tout ça pour plus de clareté !

Dépendances du module
=====================

Les dépendances sont déclarées dans le fichier ``setup.py``.

* ``webcouturier.dropdownmenu`` : pour les menus déroulants. A partir de la version 3,
  ce module est compatible avec Plone 5

* ``collective.dexteritytextindexer`` : 2 des 3 behaviors développés dans ce module
  ont des champs qui doivent pouvoir être indéxés. Voir la section :ref:`behaviors`.


Générer les ressources CSS
==========================

La méthode qui était employée pour gérérer ces ressources (avec les
utilitaires ``plone-generate-gruntfile`` et ``plone-compile-resources`` ne semble
plus être d'actualité.

A l'aide des fichiers ``HOWTO_DEVELOP.rst`` et ``Gruntfile.js`` il a été possible de
comprendre que les ressource *CSS* sont compilées afin de générer les
fichier ``iuem20-compiled.\*``

Le fichier ``gulpfile.js`` reprend donc cette idée::

   /* ***********  LESS  ********** */
   /*
    * Pour construire les CSS a partir des fichiers LESS, utiliser :
    * # gulp less
    */
   var lessfiles = ['src/plonetheme/iuem20/theme/less/*.less'];
   
   gulp.task('build-css', shell.task('grunt compile', {cwd: '.'}))
   gulp.task('notifingless', ['build-css'], function() {
      notifier.notify({title: 'LESS/CSS',
              message: 'build finished...'
      })
   });
   
   gulp.task('less', function() {
      gulp.watch(lessfiles , ['notifingless'])  
   });

.. _generer-js:

Générer les ressources JS
=========================

Le fichier javascript compilé ``js/iuem20-compiled.min.js`` est, quant à lui,
généré avec l'utilitaire `grunt`_ et la tâche déclarée dans le fichier ``Gruntfile.js``
est ``uglify``.

Il suffit donc de lancer::

   grunt uglify

pour générer le javascript.


Générer la documentation
========================

La documentation est générée suivant la méthode décrite dans le
module *iuem.plonetemplates*.

Les lignes utiles du fuchier ``gulpfile.js`` pour la documentation sont::

   var gulp = require('gulp');
   var shell = require('gulp-shell');
   
   var concat = require('gulp-concat');
   var notify = require('gulp-notify');
   var notifier = require('node-notifier');
   
   var rstfiles = ['docs/*.rst', './docs/*.py'];
   var pyfiles = ['src/plonetheme/iuem20/*.py', 'src/plonetheme/iuem20/browser/*.py', 'src/plonetheme/iuem20/browser/behaviors/*.py', 'src/plonetheme/iuem20/browser/viewlets/*.py'];
   var docfiles = rstfiles.concat(pyfiles)
   
   gulp.task('notifing', ['build-docs'], function() {
      notifier.notify({title: 'Sphinx',
              message: 'build finished...'
      })
   });
   
   gulp.task('build-docs', shell.task('bin/sphinx-build docs docs/html', {cwd: '.'}))
   gulp.task('html', function() {
      gulp.watch(docfiles , ['notifing']) 
   });
   
   gulp.task('default', ['html']);

La tâche par défaut étant ``html``, il suffit de lancer ``gulp`` sans paramètre
pour que la doc soit générée automatiquement dès qu'un fichier ``*.rst`` ou ``*.py`` 
est modifié.


