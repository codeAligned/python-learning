import unittest
from station_api import *


class TestN2(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_drives_success(self):
        pass

    def test_drives_wrong_auth(self):
        pass

    def test_drives_no_auth(self):
        pass

if __name__ == '__main__':
    nas = N2('10.5.51.58')
    print nas.url
    print nas.get_user_uuid('admin')
