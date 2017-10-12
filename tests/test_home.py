"""
Tests for home module
"""
import unittest
from crm_tests import BaseTestCase

class HomeTest(BaseTestCase):
    """
    Test for home module
    """
    def test_home(self):
        """
        Test home page
        """
        rv = self.app.get('/')
        assert b'Quick links' in rv.data


if __name__ == '__main__':
    unittest.main()