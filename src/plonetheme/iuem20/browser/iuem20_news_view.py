# -*- coding: utf-8 -*-


from plone import api
# from operator import attrgetter
from plonetheme.iuem20 import _
from plonetheme.iuem20.utils import getSettingValue
# from plonetheme.iuem20.utils import getSettingValue
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('plonetheme.iuem20:NewsView')
months = {}
months['01'] = u'Janvier'
months['02'] = u'Février'
months['03'] = u'Mars'
months['04'] = u'Avril'
months['05'] = u'Mai'
months['06'] = u'Juin'
months['07'] = u'Juillet'
months['08'] = u'Aout'
months['09'] = u'Septembre'
months['10'] = u'Octobre'
months['11'] = u'Novembre'
months['12'] = u'Décembre'


class iuem20NewsView(BrowserView):

    title = _(u'iuem20-news-view')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def _date_fr(self, date, display_time=False):
        """
        :param date: une date à convertir en ``str`` au format présenté
          habituellement en france
        :type date: objet python ``date``
        :param display_time: on inclu ou non l'heure
        :type display_time: Bolean
        :return: une chaine de caractères représentant une date,
          éventuellement avec l'heure
        """
        j = date.strftime('%d')
        m = date.strftime('%m')
        y = date.strftime('%Y')
        M = months[m]
        str_date = j + ' ' + M + ' ' + y
        # import pdb;pdb.set_trace()
        if display_time:
            H = date.strftime('%H')
            M = date.strftime('%M')
            str_date = str_date + ' ' + H + ':' + M
        return str_date

    def getRichText(self):
        """
        :return: retourne, en format *raw* le ``RichText`` anglais
        """
        try:
            return self.context.text.raw
        except Exception:
            return ''

    def getDates(self):
        """
        On obtient les dates si le behavior ``IStartEndDates`` est actif.

        :return: ``False`` si on ne peut obtenir une date, sinon, renvoie
          les dates début et fin sous forme de ``string`` pour affichage dans
          la vue.
        """
        try:
            start = self.context.start_date
            end = self.context.end_date
        except Exception:
            return False
        if (start is None) or (end is None):
            return False
        display_time = False
        try:
            display_time = self.context.display_time
        except Exception:
            pass
        start = self._date_fr(start, display_time=display_time)
        end = self._date_fr(end, display_time=display_time)
        return start + ' - ' + end

    def getOtherNews(self):
        """
        Méthode utilisée pour l'affichage des autres actus dans le cartouche
        à droite

        :return: une liste d'objets de type ``News Item``, triés par
          date de publication inversée. Le nombre max d'éléments est déterminé
          par la valeur ``max_news`` du controlpanel
        """
        portal = api.portal.get()
        founds = api.content.find(portal_type='News Item',
                                  path='/'.join(portal.getPhysicalPath()),
                                  depth=9,
                                  )
        news = []
        n_uuid = api.content.get_uuid(obj=self.context)
        for found in founds:
            n = found.getObject()
            if api.content.get_uuid(obj=n) != n_uuid:
                news.append(n)
        if len(news) == 0:
            return False
        max_news = getSettingValue('max_news')
        return sorted(news,
                      key=lambda obj: obj.effective(),
                      reverse=True)[:max_news]
