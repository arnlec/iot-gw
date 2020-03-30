from .bridge.gcp import MqttBridge
from .device import DeviceManager
import time


class Gateway:
    def __init__(self,config):
        self.__config = config
        self.__bridge = MqttBridge(self.__config['bridge'])
        self.__device_manager = DeviceManager(self.config['storage'])

    def run(self):
        self.__bridge.connect()
    
    def attach(self,device_id):
        device = self.__device_manager.get_device(device_id)
        self.__bridge.attach(device_id,device.get_token())

    def publish_event(self,device_id,event):
        pass

    def publish_state(self,device_id,state):
        pass