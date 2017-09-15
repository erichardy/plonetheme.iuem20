# -*- coding: utf-8 -*-

from OFS.interfaces import IOrderedContainer
from plone import api
from plone.i18n.normalizer.interfaces import INormalizer
from plonetheme.iuem20 import _
from string import strip
from zope.component import getUtility
from zope.interface import Invalid
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import logging
import re


# from plonetheme.iuem20 import _


logger = logging.getLogger('plonetheme.iuem20:utils')


def getSettingValue(record, prefix=None):
    """
    :param record: une clé du registre de configuration
    :type record: str
    :return: la valeur enregistrée par le control panel
    """
    if not prefix:
        prefix = 'plonetheme.iuem20.interfaces.IPlonethemeIuem20Settings.'
    prefix += record
    try:
        reg = api.portal.get_registry_record(prefix)
        return reg
    except Exception:
        logger.info('Cannot get Registry record:' + record)
        return u''


def getHomeObject(registry_record,
                  obj_type,
                  effective=True):
    """
    méthode qui permet de trouver des objets selon les critères suivants :

    * un des mots clé de l'objet contient le mot clé enregistré dans
      le registre donné en paramètre

    * le type de contenu

    * la liste est retournée triée en fonction de la date de publication

    :param registry_record: le registre où aller chercher une valeur.
        Dernier élément après
        'plonetheme.iuem20.interfaces.IPlonethemeIuem20Settings'
    :type registry_record: str
    :param obj_type: type de contenu recherché
    :type obj_type: str
    :param effective: si ``True``, la liste est triée en fonction
       de la date de publication
    :type effective: Boolean
    :return: une liste d'objets ou ``False`` si on n'a rien trouvé
    """
    tag = getSettingValue(registry_record)
    portal = api.portal.get()
    if obj_type:
        founds = api.content.find(context=portal,
                                  portal_type=obj_type,
                                  state='published'
                                  )
    else:
        founds = api.content.find(context=portal,
                                  state='published'
                                  )
    if len(founds) == 0:
        return False
    objs = []
    for found in founds:
        obj = found.getObject()
        state = api.content.get_state(obj)
        if (tag in obj.Subject()) and (state == 'published'):
            # if tag in obj.Subject():
            objs.append(obj)
    if len(objs) == 0:
        return False
    if effective:
        sortedObjs = sorted(objs,
                            key=lambda obj: obj.effective(),
                            reverse=True)
        return sortedObjs
    return objs


def altLangOneLabel():
    return getSettingValue('default_alt_lang_one_label')


def altLangTwoLabel():
    return getSettingValue('default_alt_lang_two_label')


checkEmail = re.compile(
    r'[a-zA-Z0-9._%-]+@([a-zA-Z0-9-]+\.)*[a-zA-Z]{2,4}').match


def validateEmail(value):
    if not checkEmail(value):
        raise Invalid(_(u'Invalid adress email'))
    return True


def reverse_email(email):
    """return a transformed email string : nom.prenom@domaine.fr
       monerp_mon__rf_eniamod
    """
    # email = strip(email)
    try:
        email = strip(email)
        lemail = email.split('@')
    except Exception:
        return 'on__liam'
    if len(lemail) < 2:
        return 'on__liam'
    user_email = lemail[0]
    domain = lemail[1]
    rev_user_email = ''
    rev_domain = ''
    for u in user_email.split('.'):
        uu = u[::-1]
        rev_user_email = rev_user_email + uu + '_'
    for d in domain.split('.'):
        dd = d[::-1]
        rev_domain = rev_domain + dd + '_'
    rev_domain = rev_domain[0:len(rev_domain) - 1]
    return rev_user_email + '_' + rev_domain


def make_terms(terms, termsList):
    normalizer = getUtility(INormalizer)
    for term in termsList:
        norm = normalizer.normalize(term)
        terms.append(SimpleTerm(value=norm, token=norm, title=term))
    return terms


def make_voc(terms, linesstr):
    return SimpleVocabulary(make_terms(terms, linesstr))


def make_voc_with_blank(terms, linesstr):
    terms.append(SimpleTerm(None, '', u''))
    # import pdb;pdb.set_trace()
    return SimpleVocabulary(make_terms(terms, linesstr))


def getTitleFromVoc(vocabulary, value):
    """
    Utilitaire qui permet d'obtenir le
    libellé (``title``) d'une valeur d'un vocabulaire. Essentiellement destiné
    aux affichages dans les templates.

    :param vocabulary: nom du vocabulaire tel qu'il est défini en tant \
    qu'utilitaire
    :type vocabulary: string
    :param value: valeur pour laquelle on recherche un libellé (``title``)
    :type value: string
    :returns: une chaîne de caractères qui est le ``title`` correspondant à la
        valeur passée en paramètre pour le vocabulaire donné. Si la valeur
        n'existe pas dans le vocabulaire, retourne la valeur elle-même
        passée en paramètre.
    """
    portal = api.portal.get()
    factory = getUtility(IVocabularyFactory, vocabulary)
    types_voc = factory(portal)
    try:
        term = types_voc.getTerm(value).title
    except Exception:
        term = value
    return term


# from http://docs.plone.org/develop/plone/content/listing.html
def get_position_in_parent(obj):
    parent = obj.aq_inner.aq_parent
    ordered = IOrderedContainer(parent, None)
    if ordered is not None:
        return ordered.getObjectPosition(obj.getId())
    return 0


def sort_by_position(a, b):
    """
    Usage :
    sortedMyList = sorted(myList, sort_by_position)
    """
    return get_position_in_parent(a) - get_position_in_parent(b)


def isPublished(obj):
    return api.content.get_state(obj.getObject()) == 'published'


def getGalleryImages(context):
    c = context
    try:
        carousel = c['carousel']
        if api.content.get_state(carousel) != 'published':
            return False
    except Exception:
        return False
    founds = api.content.find(context=carousel,
                              portal_type='Image',
                              path='/'.join(carousel.getPhysicalPath())
                              )
    if len(founds) == 0:
        return False
    images = [i.getObject() for i in founds
              if api.content.get_state(i.getObject()) == 'published']
    return sorted(images, sort_by_position)
