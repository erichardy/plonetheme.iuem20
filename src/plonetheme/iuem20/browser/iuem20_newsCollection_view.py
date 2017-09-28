# -*- coding: utf-8 -*-

from plone.app.contenttypes.browser.collection import CollectionView
from plonetheme.iuem20 import _
from plonetheme.iuem20.utils import getSettingValue


class iuem20NewsCollection(CollectionView):

    title = _(u'iuem20_newsCollection')

    def getLabel(self):
        label = getSettingValue('news_collection_label')
        return label
