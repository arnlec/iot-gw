from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.backends import default_backend as crypto_default_backend
import jwt
import datetime

class Device:
    def __init__(self,device_id,private_key=None,public_key=None):
        self.device_id = device_id
        self.__token = None
        if private_key == None or public_key ==None:
            key = rsa.generate_private_key(
                backend=crypto_default_backend(),
                public_exponent=65537,
                key_size=2048
            )
            self.__public_key = key.public_key().public_bytes(
                crypto_serialization.Encoding.OpenSSH,
                crypto_serialization.PublicFormat.OpenSSH
            )
            self.__private_key = key.private_bytes(
                crypto_serialization.Encoding.PEM,
                crypto_serialization.PrivateFormat.PKCS8,
                crypto_serialization.NoEncryption()
            )
        else:
            self.__public_key = public_key
            self.__private_key = private_key

    def get_public_key(self):
        return self.__public_key

    def get_private_key(self):
        return self.__private_key

    def get_token(self,project_id,minutes=60):
        if not self.__token_is_available():
            self.__generate_token(project_id,minutes)
        return self.__encrypted_token

    def __token_is_available(self):
        now = datetime.datetime.now()
        exp = datetime.datetime.fromtimestamp(self.__token['exp'] if self.__token != None else 0)
        if (self.__token) is None or ( now >= exp):
            is_available = False
        else:
            is_available = True
        return is_available

    def __generate_token(self,project_id,minutes):
        self.__token = {
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes),
            'aud' : project_id
        }
        self.__encrypted_token=jwt.encode(
            self.__token,
            self.get_private_key(),
            algorithm='RS256')

    