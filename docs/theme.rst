
.. include:: links.rst

========
Le Thème
========

Le registre des ressources JS et LESS/CSS
=========================================

Dans le fichier ``profiles/default/registry.xml``, sont déclarés :

* une *ressource* qui contient les fichiers ``js/iuem20.js`` et ``less/iuem20.less``

* un *bundle*, dépendant du bundle ``plone`` qui ne contient que la ressource
  prédécemment déclarée.


Les ressources JS
=================

Deux ressources ``javascript`` sont mises en place :

* une ressource qui est compilée avec le bundle : ``theme/js/iuem20.js``.
   
  Actuellement, la seule fonction de ce script est d'ajouter la classe ``iuem20-main`` au ``<body>``
  de la page.

* une ressource qui est appelée dans le fichier de thème ``index.html`` : ``iuem20-theme.js``.
  
  C'est dans ce script que sont réalisées la plupart des opérations javascript.


.. note:: A terme, il serait bon d'intégrer l'essentiel des fonctions de ``iuem20-theme.js``
   dans ``iuem.js``.

Comme indiqué dans le paragraphe :ref:`generer-js`, le fichier ``js/iuem20-compiled.min.js``
déclaré dans ``registry.xml`` est généré avec la commande::

   grunt uglify


Les ressources LESS/CSS
=======================

Les ressources LESS/CSS sont gérées de façon *centralisée* : le fichier ``iuem20.less``
ne fait pas d'autre chose qu'importer les différentes ressources LESS et CSS venant de :

* les ressources issues du thème *barceloneta* : ``@import "@{barceloneta_path}/...``

* `bootstrap`_ : ``@import (less) url('bootstrap.css');``

* les ressources développées spécifiquement pour le thème : ``@import url('iuem20-.....');``

Rôles des différents fichiers **LESS** du thème:

:iuem20-imports.less:
  import des fonts du site ``fonts.googleapis.com``.

:iuem20-typo.less:
  déclarations des styles des différents formats de caractères et de textes.

:iuem20-general.less:
  Styles de la navbar et du footer  

:iuem20-home.less:
  Styles de la HOME Page

:iuem20-layout.less:
  Organisation des pages

:iuem20-plone.less:
  Ajouts spécifiques à certaines fonctionnalités de plone


Le fichier index.html
=====================

Ce fichier de thème est issu des différentes versions trouvées qui permettent d'implémenter
un thème basé sur `bootstrap`_.

* la partie ``<nav id="portal-globalnav-wrapper"...`` est là pour recevoir les items et
  menus déroulants pour la navigation dans le site. Cette partie est *nourie* avec les règles
  contenues dans le fichier ``navigation-rules.xml``. Tout ceci est mis en place afin
  que les données issues du module ``webcouturier.dropdownmenu`` soient placées dans
  la barre de navigation de *bootstrap*.

* la ``div`` ``#iuem20-global-content`` contient l'essentiel du contenu du site. 

* dans cette ``div``, la partie ``<div id="iuem20-home"...`` permet de recevoir les viewlets
  de la page home. Voir la section `home`_.

* la partie ``<main id="main-container"...`` peut contenir des portlets à droite
  et/ou à gauche. Voir la partie suivante sur les règles diazo.

* en fin de fichier, sont appelés les scripts ``bootstrap.js`` pour la partie *active*
  de `bootstrap`_ et le fichier ``iuem20-theme.js`` qui contient les principaux développements
  javascript du thème.

Les règles DIAZO, le fichier rules.xml
======================================

Ce fichier de règles est celui installé par défaut dans le module auquel aura été ajouté
la règle ``<replace css:content="#viewlet-iuem20-home" css:theme="#iuem20-home" />``
pour recevoir les viewlets de la home page.

Ce fichier de règles teste la présence des ``id`` des différentes colonnes et :

* adapte la classe de la colonne centrale en fonction de la présence de ou des colonnes
  de gauche et/ou de droite

* place les contenus des colonnes de gauche et de droite dans les ``<div id="column1-container">``
  et ``<div id="column2-container">`` du thème et leur attribue des classes de
  bootstrap afin de les rendre *responsive*.



