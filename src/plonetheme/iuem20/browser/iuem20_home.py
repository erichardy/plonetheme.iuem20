# -*- coding: utf-8 -*-

# from operator import attrgetter
# from plone import api
# from plonetheme.iuem20.utils import getSettingValue
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('plonetheme.iuem20:home')


class iuem20Home(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
