import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QTextEdit, QComboBox)

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # Create UI elements
        self.location_input = QLineEdit(self)
        self.location_input.setPlaceholderText("Enter location (e.g., Brezina)")

        self.activity_selector = QComboBox(self)
        self.activity_selector.addItems(["Hiking", "Camping", "Trekking"])

        self.get_weather_button = QPushButton("Get Weather and Recommendations", self)
        self.get_weather_button.clicked.connect(self.get_weather)

        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hiking Gear Recommendation App"))
        layout.addWidget(self.location_input)
        layout.addWidget(QLabel("Select Activity:"))
        layout.addWidget(self.activity_selector)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.result_area)
        
        self.setLayout(layout)
        self.setWindowTitle("Weather Gear Recommendations")
        self.setGeometry(100, 100, 400, 400)
        
    def get_weather(self):
        location = self.location_input.text().strip()
        if location:
            weather_data = self.fetch_weather_data(location)
            if weather_data:
                recommendations = self.get_recommendations(weather_data)
                self.result_area.setPlainText(recommendations)
            else:
                self.result_area.setPlainText("Error fetching weather data.")
        else:
            self.result_area.setPlainText("Please enter a location.")
    
    def fetch_weather_data(self, location):
        api_key = "03fee1e2c12b2697860332d5c1a0e113"  # Your API key i used openweathermap
        #algerianlocations
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location},DZ&appid={api_key}&units=metric"
        #worldwideresearch
        """
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        """
        try:
            response = requests.get(url)
            data = response.json()
            if data["cod"] == 200:  # Successful response
                return {
                    "temperature": data["main"]["temp"],
                    "weather": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"],
                    "clouds": data["clouds"]["all"]
                }
            else:
                print("Error:", data.get("message", "Unknown error"))
                return None
        except Exception as e:
            print("Error fetching weather data:", e)
            return None

    def get_recommendations(self, weather_data):
        activity = self.activity_selector.currentText()
        temp = weather_data["temperature"]
        wind_speed = weather_data["wind_speed"]
        clouds = weather_data["clouds"]
        weather_description = weather_data["weather"]
        
        # Output temperature and weather first
        recommendations = [
            f"Current Temperature: {temp}°C",
            f"Current Weather: {weather_description}",
            f"Activity: {activity}",
        ]

        # Detailed gear recommendations based on activity
        if activity == "Hiking":
            recommendations.append("Hiking Gear Recommendations:")
            recommendations.append("- Hiking shoes")
            recommendations.append("- Backpack")
            recommendations.append("- Hydration system (water bladder or bottles)")
            recommendations.append("- Hiking poles (for steep terrain)")
            recommendations.append("- Snacks (trail mix, energy bars)")
            recommendations.append("- Map and compass/GPS")
            recommendations.append("- First-aid kit")
            recommendations.append("- Sun protection (sunscreen, hat, sunglasses)")
            recommendations.append("- Light jacket (for cooler temperatures)")

            if temp > 30:
                recommendations.append(" - Lightweight clothing and a cooling towel.")
            elif temp < 10:
                recommendations.append(" - Warm layers including thermal base layers.")

            if clouds > 50:
                recommendations.append(" - Bring a waterproof jacket, it might rain.")
        
        elif activity == "Camping":
            recommendations.append("Camping Gear Recommendations:")
            recommendations.append("- Tent and footprint")
            recommendations.append("- Sleeping bag (appropriate for the season)")
            recommendations.append("- Sleeping pad or air mattress")
            recommendations.append("- Camping stove or portable grill")
            recommendations.append("- Cooking utensils and food")
            recommendations.append("- Lantern or headlamp with extra batteries")
            recommendations.append("- Portable charger for devices")
            recommendations.append("- Bug spray and insect repellent")
            recommendations.append("- Camping chair")

            if temp > 30:
                recommendations.append(" - Lightweight tent for ventilation.")
            elif temp < 10:
                recommendations.append(" - Insulated sleeping bag and warm clothing.")
            
            if clouds > 50:
                recommendations.append(" - Bring a waterproof cover for the tent.")
        
        elif activity == "Trekking":
            recommendations.append("Trekking Gear Recommendations:")
            recommendations.append("- Trekking shoes or boots")
            recommendations.append("- Trekking poles")
            recommendations.append("- Hydration pack")
            recommendations.append("- Lightweight and breathable clothing")
            recommendations.append("- Navigation tools (map, compass, GPS)")
            recommendations.append("- Snacks (energy gels, bars)")
            recommendations.append("- First-aid kit")
            recommendations.append("- Sun protection (sunscreen, hat)")

            if temp > 30:
                recommendations.append(" - Quick-dry and breathable clothing.")
            elif temp < 10:
                recommendations.append(" - Thermal layers and insulated gloves.")
            
            if clouds > 50:
                recommendations.append(" - Waterproof jacket and pants.")

        # Wind speed-based recommendations
        if wind_speed > 15:
            recommendations.append(" - Windbreaker jacket is recommended due to high winds.")

        return "\n".join(recommendations)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WeatherApp()
    ex.show()
    sys.exit(app.exec_())
