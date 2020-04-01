import time
import json
from flask import Flask, request
from .bridge.gcp import MqttBridge
from .device import DeviceManager


app = Flask(__name__)
bridge = None
device_manager = None

@app.route('/',methods = ['GET'])
def index():
    return 'OK'

@app.route('/device/<device_id>',methods = ['GET'])
def get_device(device_id):
    device = device_manager.get_device(device_id)
    return json.dumps(device.toJson())

def attach(device_id):
    device = device_manager.get_device(device_id)
    bridge.attach(device_id,device.get_token())

def run(config):
    global bridge, device_manager
    bridge = MqttBridge(config['bridge'])
    device_manager = DeviceManager(config['storage'])
    bridge.connect()
    app.run(
        config['server']['http']['host'],
        config['server']['http']['port']
    )
    

def publish_event(device_id,event):
    pass

def publish_state(self,device_id,state):
    pass

    

