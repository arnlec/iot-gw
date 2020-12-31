import unittest
from iot_gw.device import DeviceManager

config = {
    'key_pair_path' : './tests/data'
}

class TestDeviceManager(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_devices(self):
        devices = DeviceManager(config).get_devices()
        self.assertEqual(2,len(devices))
        self.assertTrue('dev-1' in devices)
        self.assertTrue('gw' in devices)