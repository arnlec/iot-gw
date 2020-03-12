from .bridge.gcp import MqttBridge
import time


class Gateway:
    def __init__(self,config):
        self.__config=config
        self.bridge=MqttBridge(self.__config['bridge'])

    def run(self):
        self.bridge.connect()
        while True:
            time.sleep(1)
        