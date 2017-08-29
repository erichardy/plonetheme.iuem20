# -*- coding: utf-8 -*-


from plone.app.layout.viewlets import common as base
from plonetheme.iuem20.utils import getHomeObject
from plonetheme.iuem20.utils import getSettingValue

import logging


logger = logging.getLogger('iuem20-home-about')


class iuem20HomeAbout(base.ViewletBase):

    def getAboutTitle(self):
        """
        :return: le titre de la section About.
        """
        title = getSettingValue('about_title')
        return title

    def getAboutBgImage(self):
        """
        :return: le nom du fichier image (qui doit être
            présent dans ``portal_skins/custom/images``) qui décore
            la section *About*
        """
        bg_image = getSettingValue('about_bg_image')
        return bg_image

    def getAboutUsDocuments(self):
        """
        :return: une liste des trois derniers documents publiés
            qui ont le mot clé enregistré dans ``about_document_tag``.
            De ces documents, on affiche que la description dans la
            *home page*.
        """
        reg = 'about_document_tag'
        aboutUsDocuments = getHomeObject(
            registry_record=reg,
            obj_type='Document',
            effective=True)
        if aboutUsDocuments:
            return aboutUsDocuments[:3]
        else:
            return False

    def getAboutContainerClass(self, nb):
        if nb == 3:
            return 'container-fluid'
        return 'container'

    def getAboutClasses(self, nb):
        """
        :return: les classes des items de la section *About*
            dependent du nombre de ceux-ci...
        """
        base = 'col-xs-12 col-sm-10 col-sm-offset-1 '
        classesAbout = []
        if nb == 1:
            classesAbout.append(base + 'col-md-8 col-md-offset-2')
        if nb == 2:
            classesAbout.append(base + 'col-md-5 col-md-offset-0')
            classesAbout.append(base + 'col-md-5 col-md-offset-2')
        if nb == 3:
            classesAbout.append(base + 'col-md-4 col-md-offset-0')
            classesAbout.append(classesAbout[0])
            classesAbout.append(classesAbout[0])
        return classesAbout
