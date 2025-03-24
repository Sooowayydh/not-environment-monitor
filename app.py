from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

# Import configuration - if config.py doesn't exist, use default values
try:
    from config import CHANNEL_ID, READ_API_KEY
except ImportError:
    # Default fallback values (for development only)
    CHANNEL_ID = "YOUR_CHANNEL_ID"
    READ_API_KEY = "YOUR_READ_API_KEY"
    print("Warning: Using default API credentials. Create a config.py file for production use.")

app = Flask(__name__)

@app.route('/')
def home():
    """
    Display the latest sensor data from the environmental station.
    """
    # Retrieve the latest feed (assuming one station posting data)
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"
    
    try:
        response = requests.get(url)
        print("Response status:", response.status_code)
        print("Response content:", response.text)
        
        # Check if the response is valid JSON
        if response.status_code == 200:
            data = response.json()
            print("Parsed data type:", type(data))
            print("Parsed data:", data)
            
            # Get the channel information
            channel_info = data.get('channel', {})
            channel_name = channel_info.get('name', 'Unknown')
            
            # Handle the case where data might not be a dictionary
            if isinstance(data, dict) and 'feeds' in data and data['feeds']:
                latest_feed = data['feeds'][0]
                has_data = True
            else:
                latest_feed = {}
                has_data = False
                print("No feeds found in data")
        else:
            latest_feed = {}
            channel_name = 'Unknown'
            has_data = False
            print(f"Error: Received status code {response.status_code}")
    except Exception as e:
        print(f"Exception occurred: {e}")
        latest_feed = {}
        channel_name = 'Unknown'
        has_data = False
    
    return render_template('home.html', feed=latest_feed, channel_name=channel_name, has_data=has_data)

@app.route('/sensor')
def sensor():
    """
    Display sensor data for the last five hours for a specified sensor type.
    Accepts a query parameter 'type' (temperature, humidity, or co2).
    """
    sensor_type = request.args.get('type', 'temperature').lower()
    # Map sensor type to ThingSpeak field numbers: field1=temperature, field2=humidity, field3=co2
    field = 1
    if sensor_type == 'humidity':
        field = 2
    elif sensor_type == 'co2':
        field = 3

    # Calculate the time range: current time and five hours ago (UTC)
    now = datetime.utcnow()
    five_hours_ago = now - timedelta(hours=5)

    # Retrieve a larger set of results to ensure we cover the last 5 hours
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{field}.json?api_key={READ_API_KEY}&results=8000"
    response = requests.get(url)
    print("Raw response:", response.text)  # Debug output
    data = response.json()

    
    # Filter feeds based on the created_at timestamp
    feeds_filtered = []
    if 'feeds' in data:
        for feed in data['feeds']:
            try:
                feed_time = datetime.strptime(feed['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                if five_hours_ago <= feed_time <= now:
                    feeds_filtered.append(feed)
            except Exception as e:
                print("Error parsing time:", e)
    
    return render_template('sensor.html', feeds=feeds_filtered, sensor_type=sensor_type)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
