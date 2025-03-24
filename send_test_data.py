import requests
import time
import random

# Import configuration - if config.py doesn't exist, use default values
try:
    from config import CHANNEL_ID, WRITE_API_KEY
except ImportError:
    # Default fallback values (for development only)
    CHANNEL_ID = "YOUR_CHANNEL_ID"
    WRITE_API_KEY = "YOUR_WRITE_API_KEY"
    print("Warning: Using default API credentials. Create a config.py file for production use.")

def send_data_to_thingspeak(temp, humidity, co2):
    """
    Send sensor data to ThingSpeak channel
    """
    url = "https://api.thingspeak.com/update"
    
    payload = {
        'api_key': WRITE_API_KEY,
        'field1': temp,       # Temperature
        'field2': humidity,   # Humidity
        'field3': co2         # CO2
    }
    
    response = requests.post(url, data=payload)
    print(f"Data sent: Temp={temp}°C, Humidity={humidity}%, CO2={co2}ppm")
    print(f"Response: {response.status_code} - {response.text}")
    
    # ThingSpeak has a rate limit of 15 seconds between updates
    # The response will be the entry ID if successful
    return response.status_code == 200

def generate_mock_sensor_data():
    """
    Generate realistic mock sensor data
    """
    # Generate realistic values
    temp = round(random.uniform(18.0, 25.0), 1)       # Temperature between 18-25°C
    humidity = round(random.uniform(30.0, 60.0), 1)   # Humidity between 30-60%
    co2 = round(random.uniform(400, 1200))            # CO2 between 400-1200 ppm
    
    return temp, humidity, co2

# Main execution
if __name__ == "__main__":
    print("Starting to send test data to ThingSpeak...")
    print(f"Channel ID: {CHANNEL_ID}")
    print(f"Using Write API Key: {'*' * len(WRITE_API_KEY)}")  # Mask the API key in logs
    
    # Send a few data points
    for i in range(3):
        temp, humidity, co2 = generate_mock_sensor_data()
        success = send_data_to_thingspeak(temp, humidity, co2)
        
        if not success:
            print("Failed to send data. Check your API key and internet connection.")
        
        # Wait for 15 seconds (ThingSpeak rate limit)
        if i < 2:  # Don't wait after the last message
            print("Waiting 15 seconds for ThingSpeak rate limit...")
            time.sleep(15)
    
    print("Test data sent! Check your ThingSpeak channel or refresh your web application.")
    print("Your Flask application should now display the latest sensor readings.") 