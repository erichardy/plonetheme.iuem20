# -*- coding: utf-8 -*-

from os.path import abspath
from os.path import dirname
from os.path import join
# from operator import attrgetter
from plone import api
from plone.namedfile.file import NamedBlobImage
from plonetheme.iuem20.browser.data import lorem
from plonetheme.iuem20.utils import getSettingValue
# from zope.interface import alsoProvides
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('plonetheme.iuem20:home')
PREFIX = abspath(dirname(__file__))


def input_path(f):
    return join(PREFIX, './images/',  f)


class createContent(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.portal = api.portal.get()
        logger.info('create.__init__')

    def __call__(self):
        logger.info('create.__call__')
        self.carousel()
        self.homeNews()
        self.thumbnails()
        self.homeNews()
        self.about()
        url = self.portal.absolute_url() + '/folder_contents'
        self.request.response.redirect(url)
        return 'done...'

    def about(self):
        try:
            api.content.delete(obj=self.portal.get('about'))
        except Exception:
            pass
        docs = [u'A propos1', u'A propos2', u'A propos3']
        tag = getSettingValue('about_document_tag')
        fold = api.content.create(
                container=self.portal,
                type='Folder',
                title='About')
        api.content.transition(obj=fold,
                               transition='publish')
        fold.reindexObject()
        for doc in docs:
            d = api.content.create(
                    container=fold,
                    type='Document',
                    title=doc,
                    )
            d.subject = (tag, )
            api.content.transition(
                obj=d,
                transition='publish'
                )
            d.description = lorem
            d.reindexObject()

    def thumbnails(self):
        try:
            api.content.delete(obj=self.portal.get('mon-folder'))
        except Exception:
            pass
        thumbs = [u'IMGA0416.JPG', u'IMGA0417.JPG', u'IMGA0420.JPG',
                  u'IMGA0425.JPG', u'IMGA0465.JPG', u'IMGA0487.JPG',
                  u'IMGA0536.JPG', u'IMGA0537.JPG', u'IMGA0538.JPG']
        tag = getSettingValue('tag_home')
        fold = api.content.create(
                container=self.portal,
                type='Folder',
                title='Mon Folder')
        api.content.transition(obj=fold,
                               transition='publish')
        fold.subject = (tag,)
        fold.reindexObject()
        for t in thumbs:
            o = api.content.create(
                    container=fold,
                    type='Document',
                    title=t.replace('.', '-'),
                    )
            api.content.transition(
                obj=o,
                transition='publish'
                )
            o.subject = (tag, )
            pix = NamedBlobImage()
            fich = input_path(t)
            f = open(fich, 'r')
            data = f.read()
            filename = t
            pix.data = data
            pix.filename = filename
            o.thumbnail = pix
            o.description = (t + u' ') * 10
            o.reindexObject()

    def carousel(self):
        logger.info(self.portal)
        try:
            carousel_folder = self.portal['carousel']
        except Exception:
            carousel_folder = api.content.create(
                container=self.portal,
                type='Folder',
                title=u'carousel',)
        api.content.transition(obj=carousel_folder,
                               transition='publish')
        carousel_folder.reindexObject()
        images = [u'IMGA0042.JPG', u'IMGA0045.JPG',
                  u'IMGA0052.JPG', u'IMGA0054.JPG']
        logger.info('create carousel')
        for image in images:
            if not carousel_folder.get(image):
                img = api.content.create(
                    container=carousel_folder,
                    type='Image',
                    title=image)
                pix = NamedBlobImage()
                fich = input_path(image)
                f = open(fich, 'r')
                data = f.read()
                filename = image
                pix.data = data
                pix.filename = filename
                img.image = pix
                api.content.transition(obj=img,
                                       transition='publish')
                img.reindexObject()
        return 'carousel_folder'

    def homeNews(self):
        news_folder = self.portal.get('news')
        if not news_folder:
            news_folder = api.content.create(
                    container=self.portal,
                    type='Folder',
                    title='News')
            api.content.transition(obj=news_folder, transition='publish')
        news_folder.reindexObject()
        news = [u'IMGA0212', u'IMGA0214', u'IMGA0215',
                u'IMGA0217', u'IMGA0220', u'IMGA0224']
        for n in news:
            try:
                actu = news_folder.get(n)
                api.content.delete(actu)
            except Exception:
                pass
        for n in news:
            actu = api.content.create(
                    container=news_folder,
                    type='News Item',
                    title=n)
            pix = NamedBlobImage()
            fich = input_path(n + u'.JPG')
            f = open(fich, 'r')
            data = f.read()
            filename = n + u'.JPG'
            pix.data = data
            pix.filename = filename
            actu.image = pix
            tag = getSettingValue('tag_home_news')
            actu.subject = (tag, )
            actu.description = lorem
            api.content.transition(obj=actu, transition='publish')
            actu.reindexObject()
