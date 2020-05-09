# IoT Gateway

IoT gateway is a device that connects its client devices to a IoT platforms.

```plantuml
@startditaa                                        
+--------+        +---------+    I2     +----------+
|        |   I1   |         +<----------+   IoT    |
| Device +<------>+ Gateway +   Bridge  | Platform | 
|        |        |         |---------->|          |
+--------+        +---------+ telemetry +----------+
                                state
@endditaa
```



## Interface I1

Interface between Device and Gateway

Protocol: MQTT

Mqtt topics:
* Attach
* Unattach
* State
* Event
* Config

### Attach topic
* **Topic name:** /attach
* **Payload:** device id as string
* **Source:** device

### Unattach topic
* **Topic name:** /unattach
* **Payload:** device id as string
* **Source:** device

### State topic
* **Topic name:** /state/<device_id>
* **Payload:** device state
* **Source:** device

### Event topic
* **Topic name:** /event/<device_id>
* **Payload:** an event
* **Source:** device

## Interface I2

Interface between Gateway and Bridge

Protocol: MQTT
