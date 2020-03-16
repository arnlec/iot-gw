from .bridge.gcp import MqttBridge
from .proxy.http import proxy
import time


class Gateway:
    def __init__(self,config):
        self.__config=config
        self.__bridge=MqttBridge(self.__config['bridge'])
        proxy.on_attach=self.attach
        proxy.on_event=self.publish_event
        proxy.on_state=self.publish_state

    def run(self):
        self.__bridge.connect()
        proxy.run(
            self.__config['proxy']['http']['host'],
            self.__config['proxy']['http']['port']
            )
    
    def attach(self,device_id):
        pass

    def publish_event(self,device_id,event):
        pass

    def publish_state(self,device_id,state):
        pass