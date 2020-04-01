import time
from flask import Flask, request
from .bridge.gcp import MqttBridge
from .device import DeviceManager


server = Flask(__name__)


@server.route('/',methods=['GET'])
def __index():
    return 'OK' 

class Gateway:
    def __init__(self,config):
        self.__config = config
        self.__bridge = MqttBridge(self.__config['bridge'])
        self.__device_manager = DeviceManager(self.__config['storage'])

    def run(self):
        self.__bridge.connect()
        server.run(
            self.__config['server']['http']['host'],
            self.__config['server']['http']['port']
            )
    
    def attach(self,device_id):
        device = self.__device_manager.get_device(device_id)
        self.__bridge.attach(device_id,device.get_token())

    def publish_event(self,device_id,event):
        pass

    def publish_state(self,device_id,state):
        pass

