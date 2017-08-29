# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'plonetheme.iuem20:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    po = api.portal.get()
    wf = po.portal_workflow
    wf.setChainForPortalTypes(('File', 'Image',),
                              ('simple_publication_workflow',))


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
