# -*- coding: utf-8 -*-

from plonetheme.iuem20.utils import getSettingValue
from plonetheme.iuem20.utils import make_voc
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory

import logging


logger = logging.getLogger('plonetheme.iuem20:vocabulary')


@implementer(IVocabularyFactory)
class _bg_classes(object):

    def __call__(self, context):
        bg = getSettingValue('css_backgrounds')
        terms = []
        voc = make_voc(terms, bg)
        return voc


bg_classes = _bg_classes()
