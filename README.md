# Hiking Gear Recommendation App

## Overview
(no efforts were made for the design , only the idea) 
The Hiking Gear Recommendation App is a desktop application built using PyQt5 that provides users with personalized gear recommendations based on the current weather conditions for various outdoor activities, such as hiking, camping, and trekking.youcan try any location it's dynamic(using OpenWeatherMap) .

![image](https://github.com/user-attachments/assets/e82e0882-1f92-4c7c-aed8-3fba6a02fdca)
![redfg](https://github.com/user-attachments/assets/b0c8dbdd-a2aa-4356-a697-71922defda6d)
![image](https://github.com/user-attachments/assets/dfec9200-3898-4b7d-8135-cdcd25c51418)



## Features

- **Location Input**: Users can enter any location (e.g., city name) to fetch the current weather data.
- **Activity Selector**: Users can choose between hiking, camping, and trekking to get tailored gear recommendations.
- **Weather Information**: Displays the current temperature, weather description, wind speed, and cloud cover.
- **Personalized Recommendations**: Based on the weather conditions and selected activity, users receive a detailed list of recommended gear.

## Requirements

- Python 3.x
- PyQt5
- Requests library

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Set Up a Virtual Environment (Optional but recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install Required Packages**:
   ```bash
   pip install PyQt5 requests
   ```

## Usage

1. **Run the application**:
   ```bash
   python recommendation_gear_location.py
   ```

2. Enter a location in the input field (e.g., "Brezina").
3. Select an activity from the dropdown menu (Hiking, Camping, or Trekking).
4. Click on the "Get Weather and Recommendations" button to fetch the weather data and view gear recommendations based on the current weather.

## API Key

This application uses the OpenWeatherMap API to fetch weather data. You can use the provided API key or replace it with your own by modifying the `fetch_weather_data` method in the `WeatherApp` class:
```python
api_key = "YOUR_API_KEY"
```

## Contributing

Contributions are welcome! Please create a pull request or open an issue if you find any bugs or have suggestions for improvements.


