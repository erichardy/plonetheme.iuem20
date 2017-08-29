# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import common as base

import logging


logger = logging.getLogger('iuem20-home-carousel')


class iuem20AltLanguages(base.ViewletBase):

    def displayAlt1(self):
        try:
            return self.context.display_one
        except Exception:
            return False

    def getLabel1(self):
        try:
            return self.context.label_one
        except Exception:
            return u'None'

    def getTextAlt1(self):
        richtext = u'<p />'
        try:
            richtext = self.context.presentation_one.raw
        except Exception:
            return False
        if richtext < 6:
            return False
        return richtext

    def displayAlt2(self):
        try:
            return self.context.display_two
        except Exception:
            return False

    def getLabel2(self):
        try:
            return self.context.label_two
        except Exception:
            return u'None'

    def getTextAlt2(self):
        richtext = u'<p />'
        try:
            richtext = self.context.presentation_two.raw
        except Exception:
            return False
        if richtext < 6:
            return False
        return richtext
