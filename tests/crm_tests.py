import os
import crm
import unittest
import tempfile
import sys

crm_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, crm_base)


class BaseTestCase(unittest.TestCase):
    """
    Base testcase
    """

    def setUp(self):
        """
        Setup
        """
        self.db_fd, crm.app.config['DATABASE'] = tempfile.mkstemp()
        crm.app.testing = True
        self.app = crm.app.test_client()
        
    
    def tearDown(self):
        """
        Teardown
        """
        os.close(self.db_fd)
        os.unlink(crm.app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()