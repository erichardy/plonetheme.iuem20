# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plonetheme.iuem20.testing import PLONETHEME_IUEM20_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.iuem20 is properly installed."""

    layer = PLONETHEME_IUEM20_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.iuem20 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.iuem20'))

    def test_browserlayer(self):
        """Test that IPlonethemeIuem20Layer is registered."""
        from plonetheme.iuem20.interfaces import (
            IPlonethemeIuem20Layer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeIuem20Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_IUEM20_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.iuem20'])

    def test_product_uninstalled(self):
        """Test if plonetheme.iuem20 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.iuem20'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeIuem20Layer is removed."""
        from plonetheme.iuem20.interfaces import \
            IPlonethemeIuem20Layer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeIuem20Layer, utils.registered_layers())
