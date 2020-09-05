from iot_gw.gateway import init 
import logging

config={
    'storage':{
        'key_pair_path' : './tests/data'
    },
    'bridge':{
        'adapter': 'gcp',
        'project_id': 'iot-dev-260617',
        'region': 'europe-west1',
        'registry_id': 'mylab',
        'device_id': 'gw-dev',
        'private_key_file': './tests/data/gw_private.pem',
        'ca_certs_file': './tests/data/mqtt.googleapis.com.pem',
        'bridge_hostname': 'mqtt.googleapis.com',
        'bridge_port': 443
    },
    'server':{
        'http':{
            'host':'0.0.0.0',
            'port':'8080'
        }
    },
    'mqtt':{
        'login': 'gateway',
        'password': 'P@ssw0rd',
        'hostname': '192.168.99.11',
        'port': '8883',
        'ca_certs_file':'./tests/data/ca.crt'
    }
}

logging.basicConfig(level=logging.DEBUG)
init(config_path=None,default_config=config).run(
    config['server']['http']['host'],
    config['server']['http']['port']
)