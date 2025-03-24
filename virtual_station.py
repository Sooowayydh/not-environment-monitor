import time
import random
import paho.mqtt.client as mqtt

# Unique identifier for the station
STATION_ID = "station_001"

# Import configuration - if config.py doesn't exist, use default values
try:
    from config import CHANNEL_ID, WRITE_API_KEY
except ImportError:
    # Default fallback values (for development only)
    CHANNEL_ID = "YOUR_CHANNEL_ID"
    WRITE_API_KEY = "YOUR_WRITE_API_KEY"
    print("Warning: Using default API credentials. Create a config.py file for production use.")

# MQTT Broker details (for ThingSpeak, use your specific channel details)
BROKER = "mqtt.thingspeak.com"
PORT = 1883

# Create MQTT client and set credentials (ThingSpeak requires a username and MQTT password)
client = mqtt.Client()
client.username_pw_set("mwa0000036829630", "1N44LDR6OZ2VYL5X")
client.connect(BROKER, PORT, 60)

def generate_sensor_data():
    """Generate random sensor data within the specified ranges."""
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": round(random.uniform(300, 2000), 2)
    }

while True:
    data = generate_sensor_data()
    # Construct the payload according to ThingSpeak's required format:
    # field1=temperature, field2=humidity, field3=co2
    payload = f"field1={data['temperature']}&field2={data['humidity']}&field3={data['co2']}"
    topic = f"channels/{CHANNEL_ID}/publish/{WRITE_API_KEY}"
    client.publish(topic, payload)
    print(f"Published data from {STATION_ID}: {data}")
    time.sleep(10)  # Publish every 10 seconds (adjust as needed)
