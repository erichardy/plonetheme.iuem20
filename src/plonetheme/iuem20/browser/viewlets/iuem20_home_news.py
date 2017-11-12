# -*- coding: utf-8 -*-


from plone.app.layout.viewlets import common as base
from plonetheme.iuem20.utils import getHomeObject
from plonetheme.iuem20.utils import getSettingValue

import logging


logger = logging.getLogger('iuem20-home-news')


class iuem20HomeNews(base.ViewletBase):

    def getHomeNews(self):
        """
        :return: la liste des ``News Item`` qui ont le mot clé
          enregistré dans ``tag_home``.
        """
        tag_reg = 'tag_home_news'
        homeNews = getHomeObject(registry_record=tag_reg,
                                 obj_type='News Item',
                                 effective=True)
        if not homeNews:
            return False
        try:
            max_news = int(getSettingValue('max_news'))
        except Exception:
            max_news = 6
        return homeNews[:max_news]

    def getCarouselInterval(self):
        interval = getSettingValue('carousel_interval')
        return interval
