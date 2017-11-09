# -*- coding: utf-8 -*-


# from operator import attrgetter
from plonetheme.iuem20 import _
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
