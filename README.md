# IoT Environmental Station Dashboard

A web-based dashboard application for monitoring environmental sensor data (temperature, humidity, and CO2) from IoT devices using ThingSpeak as the data storage platform.


## Overview

This project is a Flask web application that connects to a ThingSpeak channel to retrieve and display environmental sensor data. It provides a modern, responsive dashboard interface with real-time data visualization. The application has the following features:

- **Home Dashboard:** Displays the latest readings from all sensors in a card-based layout
- **Sensor-Specific Views:** Detailed historical data views for each sensor type
- **Auto-Refresh:** Automatically updates data every 60 seconds
- **Visual Indicators:** Color-coded status indicators based on sensor value ranges
- **Responsive Design:** Works across desktop and mobile devices

## Prerequisites

- Python 3.6 or higher
- Flask web framework
- Requests library
- A ThingSpeak account with a channel configured for sensor data
- Internet connection to access the ThingSpeak API

## Installation

1. Clone this repository or download the source code:
   ```
   git clone https://github.com/yourusername/iot-environmental-station.git
   cd iot-environmental-station
   ```

2. Install the required dependencies:
   ```
   pip install flask requests
   ```

3. Configure your ThingSpeak credentials:
   - Create a `config.py` file based on the `config_template.py` provided:
   ```
   cp config_template.py config.py
   ```
   - Edit `config.py` and add your ThingSpeak credentials:
   ```python
   # ThingSpeak API Configuration
   CHANNEL_ID = "YOUR_CHANNEL_ID"  # Your ThingSpeak channel ID
   READ_API_KEY = "YOUR_READ_API_KEY"  # Your ThingSpeak read API key
   WRITE_API_KEY = "YOUR_WRITE_API_KEY"  # Your ThingSpeak write API key
   ```
   - This file is included in `.gitignore` to prevent accidentally committing your API keys

## Running the Application

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5001/
   ```

3. The dashboard will load and display any available sensor data from your ThingSpeak channel.

## Sending Data to ThingSpeak

You can use the `send_test_data.py` script to simulate sensor data for testing purposes:

```
python send_test_data.py
```

This script will send random temperature, humidity, and CO2 values to your ThingSpeak channel.

For production use, you'll need to:

1. Configure your IoT sensors to send data to your ThingSpeak channel 
2. Use your ThingSpeak Write API Key (available in your ThingSpeak channel settings)
3. Set up your sensors to publish to the correct fields:
   - Field 1: Temperature (°C)
   - Field 2: Humidity (%)
   - Field 3: CO2 (ppm)

### MQTT Configuration

For IoT devices using MQTT protocol, use this format:

```
Topic: channels/YOUR_CHANNEL_ID/publish/YOUR_WRITE_API_KEY
Payload: field1=24.5&field2=45&field3=550
```

## Application Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates for the web pages
  - `home.html`: Dashboard main page
  - `sensor.html`: Sensor-specific historical data
- `static/`: Static assets
  - `css/styles.css`: Styling for the application
  - `js/dashboard.js`: JavaScript for interactive features
- `send_test_data.py`: Script to send test data to ThingSpeak

## Customization

You can customize the application by:

1. Modifying the CSS in `static/css/styles.css` to change the appearance
2. Adjusting the sensor ranges in `static/js/dashboard.js` to change the status indicators
3. Adding more sensor types by extending the application logic

## Troubleshooting

If you encounter any issues:

1. **No data appears**: Make sure your ThingSpeak channel has data. Use `send_test_data.py` to add test data.
2. **API errors**: Verify your Channel ID and API keys are correct.
3. **Port in use**: If port 5001 is already in use, modify the port number in `app.py`.

## Future Enhancements

- Add data visualization charts for historical trends
- Implement user authentication
- Add alerting capabilities for out-of-range sensor values
- Support for additional sensor types
- Mobile app integration


## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [ThingSpeak](https://thingspeak.com/) - IoT Analytics Platform
- [Font Awesome](https://fontawesome.com/) - Icons used in the UI 