# -*- coding: utf-8 -*-


from plone import api
from plone.app.layout.viewlets import common as base
from plonetheme.iuem20.utils import getHomeObject
from plonetheme.iuem20.utils import getSettingValue

import logging


logger = logging.getLogger('iuem20-home-thumbnails')


class iuem20HomeThumbnails(base.ViewletBase):

    def getCarouselThumbnails(self):
        """
        :return: la liste des ``Folder`` qui doivent apparaître
            comme thumbnail. Ces folders doivent avoir le mot clé
            enregistré dans ``tag_home``.
        """
        homeThumbnails = getHomeObject(registry_record='tag_home',
                                       obj_type=None,
                                       effective=True)
        if not homeThumbnails:
            return False
        return homeThumbnails[:6]

    def getThumbSRC(self, thumb):
        """
        :returns: src attributes of a thumbnail field
        """
        default_thumb = getSettingValue('default_thumb')
        image = None
        image_field = 'thumbnail'
        # image_field['Folder'] = 'image'
        # image_field['News Item'] = 'image'
        # image_field['Event'] = 'image'
        try:
            field = image_field
            image = eval('thumb.' + field)
            filename = image.filename
        except Exception:
            portal = api.portal.get()
            return portal.absolute_url() + '/images/' + default_thumb
        url = thumb.absolute_url() + '/@@download/' + field + '/'
        url += filename
        return url
