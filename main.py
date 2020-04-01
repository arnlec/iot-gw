from iot_gw.gateway import run as run_gateway
import logging

config={
    'storage':{
        'key_pair_path' : './tests/data'
    },
    'bridge':{
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
    }
}

logging.basicConfig(level=logging.DEBUG)
run_gateway(config)