# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.iuem20


class PlonethemeIuem20Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.iuem20)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.iuem20:default')


PLONETHEME_IUEM20_FIXTURE = PlonethemeIuem20Layer()


PLONETHEME_IUEM20_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_IUEM20_FIXTURE,),
    name='PlonethemeIuem20Layer:IntegrationTesting'
)


PLONETHEME_IUEM20_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_IUEM20_FIXTURE,),
    name='PlonethemeIuem20Layer:FunctionalTesting'
)


PLONETHEME_IUEM20_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_IUEM20_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeIuem20Layer:AcceptanceTesting'
)
