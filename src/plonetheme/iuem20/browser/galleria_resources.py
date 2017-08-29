# -*- coding: utf-8 -*-


# from operator import attrgetter
from plonetheme.iuem20.utils import getSettingValue
# from plone import api
# from plonetheme.iuem20.utils import getSettingValue
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('plonetheme.iuem20:galleria')


class galleriaResources(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.installed = self._installed()
        self.css = self._css()
        self.js = self._js()
        self.galleria_code = self._galleria_code()

    def _installed(self):
        galleria_installed = getSettingValue('galleria_installed')
        return galleria_installed

    def _css(self):
        css_resources = getSettingValue('galleria_css')
        return css_resources

    def _js(self):
        js_resources = getSettingValue('galleria_js')
        return js_resources

    def _galleria_code(self):
        js_code = getSettingValue('galleria_code')
        return js_code
