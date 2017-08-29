
.. include:: links.rst



==================================
Documentation de plonetheme.iuem20
==================================
.. _IUEM: http://www-iuem.univ-brest.fr
.. _DocPlone: http://docs.plone.org/about/documentation_styleguide_addons.html
.. _Sphinx: http://sphinx-doc.org/

Documentation de ``plonetheme.iuem20`` dévéloppé par Eric Hardy.

Voir les recommandations pour la documentation à `DocPlone`_

Voir aussi Sphinx : `Sphinx`_


Installation
============
Ajouter *plonetheme.iuem20* à la liste définie par la variable ``eggs`` dans la
section ``[instance]`` du fichier *buildout.cfg*

et la source dans la section ``[sources]``::

   plonetheme.iuem20 = git gitiuem:plonetheme.iuem20.git

Motivation
==========

Le module plonetheme.iuem20 a été développé pour servir de base graphique au site web du
projet **PADDLE** géré par Marie Bonnin.

Il comprend le thème graphique à proprement parlé basé sur `bootstrap`_ (version 3.3.7) et géré
par `Diazo`_.

Toute la documentation
======================

.. toctree::
    :maxdepth: 2

    La mise en place du module <init_module>
    Le thème <theme>
    Les behaviors <behaviors>
    La vue HOME PAGE <home>
    LICENCE <LICENSE>
    
