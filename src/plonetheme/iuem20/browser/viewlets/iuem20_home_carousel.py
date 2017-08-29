# -*- coding: utf-8 -*-


from plone import api
from plone.app.layout.viewlets import common as base
from plonetheme.iuem20.utils import getSettingValue

import logging


logger = logging.getLogger('iuem20-home-carousel')


class iuem20HomeCarousel(base.ViewletBase):

    def getCarouselImages(self, context):
        """
        :return: la liste des images qui doivent défiler dans le carousel.
          Ces images doivent être placées dans un ``Folder`` ayant pour
          id : ``iuem20-home-carousel``
        """
        """
        layout = context.getLayout()
        if context.portal_type != 'Folder':
            context = context.aq_parent
        """
        parent_context = context.aq_parent
        # logger.info(parent_context)
        # logger.info(context)
        objs = []
        try:
            images = api.content.find(context=parent_context['carousel'],
                                      depth=1,
                                      portal_type='Image')
            for image in images:
                objs.append(image.getObject())
            # logger.info(len(images))
        except Exception:
            logger.info('0 images !...')
        # logger.info(str(len(objs)) + ' images dans le carousel')
        if len(objs) == 0:
            return False
        return objs

    def getCarouselInterval(self):
        """
        :return: En millisecondes, le temps de défilement des
          images du carousel
        """
        interval = getSettingValue('carousel_interval')
        return interval

    def getCarouselLogoName(self):
        """
        :return: le nom du fichier image qui s'affiche en overlay
          sur le carousel. Ce fichier image doit être présent
          dans ``portal_skins/custom/images``. généralement une image
          *png*.
        """
        logo_name = getSettingValue('carousel_logo')
        return logo_name

    def getCarouselText(self):
        """
        :return: la valeur du registre ``carousel_label`` pour
          afficher par dessus le carousel
        """
        label = getSettingValue('carousel_label')
        return label
