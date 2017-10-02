# -*- coding: utf-8 -*-

from plone.supermodel import model
from plonetheme.iuem20 import _
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import Bool
from zope.schema import Int
from zope.schema import List
from zope.schema import Text
from zope.schema import TextLine


class IPlonethemeIuem20Layer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


portfolioBGClasses = []
portfolioBGClasses.append(u'bg-dark')
portfolioBGClasses.append(u'bg-light')
galleriaCode = u"""
      Galleria.loadTheme('++plone++iuem20.galleria/galleria/themes/twelve/galleria.twelve.min.js');
      Galleria.configure({
        autoplay: 5000,
        imageCrop: true,
        responsive: true,
        swipe: 'auto',
        lightbox: true,
        idleMode: 'hover',
        pauseOnInteraction: true,
        carousel: false,
        easing: 'galleriaIn',
        imagePan: true,
        showInfo: true,
        variation: 'light',
        transition: 'fade',
        // Toggles the fullscreen button
        _showFullscreen: true,

        // Toggles the lightbox button
        _showPopout: true,

        // Toggles the progress bar when playing a slideshow
        _showProgress: true,

        // Toggles tooltip
        _showTooltip: true,

        // Localized strings, modify these if you want
        // tooltips in your language
        _locale: {
            show_thumbnails: "Show thumbnails",
            hide_thumbnails: "Hide thumbnails",
            play: "Play slideshow",
            pause: "Pause slideshow",
            enter_fullscreen: "Enter fullscreen",
            exit_fullscreen: "Exit fullscreen",
            popout_image: "Popout image",
            showing_image: "Showing image %s of %s"
        }
      });
      Galleria.run('.galleria');

"""
galleriaCSS = u'++plone++iuem20.galleria/galleria/'
galleriaCSS += u'themes/twelve/galleria.twelve.css'


class IPlonethemeIuem20Settings(model.Schema):

    model.fieldset('css overrides',
                   label=_(u'css overrides'),
                   fields=['more_css',
                           ]
                   )
    more_css = Text(
        title=_(u'more css'),
        description=_(u'will overrides all other CSS'),
        required=False)

    model.fieldset('home-page',
                   label=_(u'home page settings'),
                   fields=['carousel_label',
                           'carousel_logo',
                           'carousel_interval',
                           'tag_home',
                           'default_thumb',
                           'about_title',
                           'about_bg_image',
                           'about_document_tag',
                           'tag_home_news',
                           'max_news',
                           'display_document_title',
                           'display_document_description'
                           ])

    carousel_label = TextLine(title=_(u'carousel label'),
                              description=_(u'for carousel at home page'),
                              default=u'Joint laboratory in benthic ecology',
                              )
    carousel_interval = TextLine(title=_(u'carousel interval'),
                                 description=_(u'milliseconds'),
                                 default=u'4000',
                                 )
    carousel_logo = TextLine(title=_(u'Logo filename, should be in'),
                             description=_(u'portal_skins/custom/images'),
                             default=u'logoblanc.svg',
                             )
    tag_home = TextLine(title=_(u'Tag used for thumbnails on home page'),
                        description=_(u'Only One word'),
                        default=u'iuem20-home',
                        )
    default_thumb = TextLine(title=_(u'Name of the default thumb image'),
                             description=_(u'in portal_skins/custom/images'),
                             default=u'default_thumbnail.jpg',
                             )
    about_title = TextLine(title=_(u'title for about section'),
                           default=u'About us',
                           )
    about_bg_image = TextLine(title=_(u'Background image for about section'),
                              description=_(u'in portal_skins/custom/images'),
                              default=u'csj-soft.png',
                              )
    about_document_tag = TextLine(title=_(u'Tag used for about items'),
                                  description=_(u'for home page'),
                                  default=u'iuem20-home',
                                  )
    tag_home_news = TextLine(title=_(u'Tag used for news on home page'),
                             description=_(u'Only One word, used for news'),
                             default=u'iuem20-home-news',
                             )

    max_news = Int(title=_(u'max news to display'),
                   min=1,
                   max=300,
                   default=8,
                   )
    display_document_title = Bool(
        title=_(u'display document title for Home page'),
        default=True)
    display_document_description = Bool(
        title=_(u'display document description for Home page'),
        default=True)

    model.fieldset('alt_languages',
                   label=_(u'Alternates languages'),
                   fields=['default_alt_lang_one_label',
                           'default_alt_lang_two_label',
                           ],)
    default_alt_lang_one_label = TextLine(
        title=_(u'default_alt_lang_one_label'),
        default=u'English',
        )
    default_alt_lang_two_label = TextLine(
        title=_(u'default_alt_lang_two_label'),
        default=u'Spanish',
        )
    model.fieldset('galleria',
                   label=_(u'Galleria params'),
                   fields=['galleria_installed',
                           'galleria_css',
                           'galleria_js',
                           'galleria_code'
                           ],)
    galleria_installed = Bool(
        title=_(u'Check if galleria is installed'),
        description=_(u'used for images galleries'),
        default=True
        )
    galleria_css = TextLine(
        title=_(u'URL of the CSS resource for galleria'),
        description=_(u''),
        default=galleriaCSS)
    galleria_js = TextLine(
        title=_(u'URL of the Javascript resource for galleria'),
        description=_(u''),
        default=u'++plone++iuem20.galleria/galleria/galleria-1.4.2.min.js')
    galleria_code = Text(
        title=_(u'Javascript code needed to display a gallery'),
        description=_(u'Must be a valid javascript code'),
        default=galleriaCode)
    model.fieldset('misc_css',
                   label=_(u'Misc CSS'),
                   fields=[
                       'news_collection_label',
                       'css_backgrounds',
                       ])
    news_collection_label = TextLine(
        title=_(u'Label for the News Collection view'),
        description=_(u''),
        default=u'Actualités / News'
        )
    css_backgrounds = List(
        title=_(u'CSS classes for background'),
        description=_(u'i.e. for portfolio background. One class per line'),
        value_type=TextLine(),
        default=portfolioBGClasses,
        required=True,
        )
