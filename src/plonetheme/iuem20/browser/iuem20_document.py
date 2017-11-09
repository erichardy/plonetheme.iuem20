# -*- coding: utf-8 -*-


# from operator import attrgetter
from plonetheme.iuem20 import _
from plonetheme.iuem20.utils import getGalleryImages as ggi
from plonetheme.iuem20.utils import getObjThumbnailSrc as gots
from plonetheme.iuem20.utils import getRelatedItems as gri
# from plone import api
# from plonetheme.iuem20.utils import getSettingValue
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('plonetheme.iuem20:document')


class iuem20Document(BrowserView):

    title = _(u'iuem20_document')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getGalleryImages(self):
        logger.info('getGalleryImages iuem20 Document')
        return ggi(self.context)

    def getRelatedItems(self):
        return gri(self.context)

    def getObjThumbnailSrc(self, obj):
        return gots(obj)
