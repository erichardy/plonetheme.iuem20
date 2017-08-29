# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import common as base
from plonetheme.iuem20.utils import getSettingValue

import logging


logger = logging.getLogger('iuem20-home-carousel')


class iuem20HomeRichText(base.ViewletBase):

    def getRichText(self):
        """
        :return: Le contenu richText du document
        """
        try:
            richtext = self.context.text.raw
        except Exception:
            # dans le cas ou on n'a pas de champ richText
            return None
        if richtext < 6:
            return False
        return richtext

    def displayTitle(self):
        return getSettingValue('display_document_title')

    def displayDescription(self):
        return getSettingValue('display_document_description')

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
