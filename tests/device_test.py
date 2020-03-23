import unittest
import jwt
import time
from iot_gw.device import Device
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.backends import default_backend as crypto_default_backend

class TestDevice(unittest.TestCase):

    def test_get_token(self):
        device = Device('device_id')
        # check token is well-formatted
        token = device.get_token('project_id',1)
        self.assertIsNotNone(token)
        decodedToken = jwt.decode(
            token,
            device.get_public_key(),
            algorithms='RS256',
            options={'verify_aud': False}
        )
        self.assertEqual(decodedToken['aud'],'project_id')
        self.assertEqual(decodedToken['exp'] - decodedToken['iat'], 60)
        # check token is not generated each time
        token2 = device.get_token('project_id')
        self.assertEqual(token,token2)
        
    def test_get_token_expired(self):
        device = Device('device_id')
        token = device.get_token('project_id',1)
        # check a new token is generated when the previous is expired
        time.sleep(60)
        token2 = device.get_token('project_id')
        self.assertNotEqual(token,token2)

    def test_get_token_with_key_pair_provided(self):
        key = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=2048
        )
        public_key = key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH
        )
        private_key = key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption()
        )
        device = Device('device_id',private_key,public_key)
        token = device.get_token('project_id',1)
        self.assertIsNotNone(token)
        decodedToken = jwt.decode(
            token,
            public_key,
            algorithms='RS256',
            options={'verify_aud': False}
        )
        self.assertEqual(decodedToken['aud'],'project_id')
        self.assertEqual(decodedToken['exp'] - decodedToken['iat'], 60)

        

if __name__ == '__main__':
    unittest.main()
