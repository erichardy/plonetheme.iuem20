# -*- coding: utf-8 -*-

from plonetheme.iuem20 import _
from plonetheme.iuem20.utils import getSettingValue
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('plonetheme.iuem20:moreCSS')


class moreCss(BrowserView):

    title = _(u'more css')

    def more_css(self):
        css = getSettingValue('more_css')
        if (not css) or (len(css) < 1):
            css = ''
        return '<style>' + css + '</style>'
