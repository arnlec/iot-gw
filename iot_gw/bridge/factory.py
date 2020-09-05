import logging
from .gcp import MqttBridge as GCPMqttBridge

class BridgeAdapterFactory:
    """
    BridgeAdapter factory

    The factory instanciate a bridge adapter based on adapter property

    Supported adapter type:
      - gcp: Google Cloud Platform mqtt bridge
      - gcp: Google Cloud Platform mqtt bridge
    """
    
    def __init__(self):
        self.__adapters={
            'gcp': GCPMqttBridge,
            'gcp_mqtt': GCPMqttBridge
        }

    def create(self,config,on_config_handler=None,on_commands_handler=None):
        """
        Create a BridgeAdapter instance

        Parameters
        ----------
        config : dict
            dictionnary with properties which are used to establish the connection.

        Returns
        -------
            Bridge adapter instance

        Raises
        ------
            RuntimeError if adapter property is not defined in config 
            RuntimeError if adapter property value is not supported
        """
        try:
            adapter_id=config['adapter']
        except KeyError:
            raise RuntimeError("Undefined bridge adapter in configuration")
        adapter = None
        try:
            adapter = self.__adapters[adapter_id](config,
                on_config=on_config_handler,
                on_commands=on_commands_handler)
        except KeyError:
            raise RuntimeError("Unknown bridge adapter: %s" % adapter_id)
        return adapter

