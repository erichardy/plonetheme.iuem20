# -*- coding: utf-8 -*-


# from operator import attrgetter
from plonetheme.iuem20 import _
# from plone import api
# from plonetheme.iuem20.utils import getSettingValue
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('plonetheme.iuem20:home')


class iuem20Home(BrowserView):

    title = _(u'iuem20_home')

    def __init__(self, context, request):
        self.context = context
        self.request = request
