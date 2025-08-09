import requests
from datetime import datetime, timedelta
import json

class HourlyForecast:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_hourly_data(self, lat, lon):
        try:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                hourly_data = []
                
                for i in range(min(8, len(data['list']))):
                    forecast = data['list'][i]
                    
                    timestamp = forecast['dt']
                    time_obj = datetime.fromtimestamp(timestamp)
                    
                    hourly_item = {
                        'time': time_obj.strftime("%H:%M"),
                        'hour': time_obj.hour,
                        'temperature': int(forecast['main']['temp']),
                        'feels_like': int(forecast['main']['feels_like']),
                        'humidity': forecast['main']['humidity'],
                        'description': forecast['weather'][0]['description'],
                        'icon': forecast['weather'][0]['icon'],
                        'main_weather': forecast['weather'][0]['main'],  
                        'wind_speed': forecast['wind']['speed'],
                        'pressure': forecast['main']['pressure'],
                        'clouds': forecast['clouds']['all'],
                        'rain_chance': self.calculate_rain_chance(forecast)
                    }
                    hourly_data.append(hourly_item)
                
                return hourly_data
            else:
                return self.get_mock_hourly_data()
                
        except Exception as e:
            print(f"Error fetching hourly data: {e}")
            return self.get_mock_hourly_data()
    
    def calculate_rain_chance(self, forecast_data):
        if 'rain' in forecast_data:
            rain_volume = forecast_data['rain'].get('3h', 0)
            if rain_volume > 0:
                return min(100, int(rain_volume * 20))  
        
        humidity = forecast_data['main']['humidity']
        clouds = forecast_data['clouds']['all']
        
        if humidity > 80 and clouds > 70:
            return 80
        elif humidity > 60 and clouds > 50:
            return 60
        elif humidity > 40 and clouds > 30:
            return 30
        else:
            return 10
    
    def get_mock_hourly_data(self):
        mock_data = []
        current_time = datetime.now()

        base_temps = [22, 21, 20, 19, 18, 19, 21, 23, 25, 24, 23, 22, 20, 19, 18]
        base_weather = ["Clear", "Clouds", "Clouds", "Rain", 
                       "Clear", "Clear", "Clouds", "Clear",
                       "Clear", "Clouds", "Rain", "Clear",
                       "Clouds", "Rain", "Clear"]

        for i in range(15):  
            time_obj = current_time + timedelta(hours=i*3)
            mock_data.append({
                'time': time_obj.strftime("%H:%M"),
                'hour': time_obj.hour,
                'temperature': base_temps[i],
                'feels_like': base_temps[i] + 2,
                'humidity': 50 + (i * 2),
                'description': base_weather[i].lower(),
                'icon': '01d',
                'main_weather': base_weather[i],
                'wind_speed': 3.5 + (i * 0.2),
                'pressure': 1013 + (i * 1),
                'clouds': 20 + (i * 6),
                'rain_chance': 10 + (i * 3)
            })

        return mock_data
    
    def get_weather_emoji_logo(self, main_weather, icon_code, hour):
        is_day = 'd' in icon_code or (6 <= hour <= 18)

        if hasattr(self, '_is_dark_mode_display') and self._is_dark_mode_display:
            weather_logos = {
                'Clear': '☀' if is_day else '☾',
                'Clouds': '☁',                    
                'Rain': '🌧',                     
                'Drizzle': '🌦',                 
                'Thunderstorm': '⛈',               
                'Snow': '❄',                      
                'Mist': '≡',                      
                'Smoke': '≡',                     
                'Haze': '≡',                        
                'Dust': '≡',                      
                'Fog': '≡',                       
                'Sand': '≡',                      
                'Ash': '≡',                       
                'Squall': '~',                   
                'Tornado': '🌪'                  
            }
        else:
            weather_logos = {
                'Clear': '☀️' if is_day else '🌙',
                'Clouds': '☁️',
                'Rain': '🌧️', 
                'Drizzle': '🌦️',
                'Thunderstorm': '⛈️',
                'Snow': '🌨️',
                'Mist': '🌫️',
                'Smoke': '🌫️',
                'Haze': '🌫️',
                'Dust': '🌫️',
                'Fog': '🌫️',
                'Sand': '🌫️',
                'Ash': '🌫️',
                'Squall': '💨',
                'Tornado': '🌪️'
            }

        return weather_logos.get(main_weather, '☁' if hasattr(self, '_is_dark_mode_display') and self._is_dark_mode_display else '☁️')

    def create_hourly_display(self, canvas, canvas_items, lat, lon, position, is_dark_mode):
        start_x, start_y = position

        self._is_dark_mode_display = is_dark_mode

        hourly_items = []
        for i in range(10): 
            hourly_items.extend([
                f'hourly_time_{i}', f'hourly_temp_{i}', f'hourly_icon_{i}',
                f'hourly_desc_{i}', f'hourly_rain_{i}'
            ])

        for item in hourly_items:
            if item in canvas_items:
                canvas.delete(canvas_items[item])

        # hourly data
        hourly_data = self.get_hourly_data(lat, lon)

        if is_dark_mode:
            text_color = "#FFFFFF"
            temp_color = "#FFFFFF"       
            rain_color = "#FFFFFF"         
            icon_color = "#FFFFFF"         
        else:
            text_color = "#000000"        
            temp_color = "#000000"        
            rain_color = "#333333"        
            icon_color = "#000000"        

        item_width = 100  
        for i, hour_data in enumerate(hourly_data[:7]):  
            x_offset = start_x + (i * item_width)

            canvas_items[f'hourly_time_{i}'] = canvas.create_text(
                x_offset, start_y - 20, text=hour_data['time'], 
                font=("Arial", 13, "bold"),
                fill=text_color, anchor="center"
            )

            weather_logo = self.get_weather_emoji_logo(
                hour_data['main_weather'], 
                hour_data['icon'], 
                hour_data['hour']
            )
            canvas_items[f'hourly_icon_{i}'] = canvas.create_text(
                x_offset, start_y + 16, text=weather_logo, 
                font=("Arial", 25), 
                fill=icon_color,  
                anchor="center"
            )

            canvas_items[f'hourly_temp_{i}'] = canvas.create_text(
                x_offset, start_y + 70, text=f"{hour_data['temperature']}°", 
                font=("Arial", 19, "bold"),
                fill=temp_color, anchor="center"
            )

            canvas_items[f'hourly_rain_{i}'] = canvas.create_text(
                x_offset, start_y + 45, text=f"{hour_data['rain_chance']}%", 
                font=("Arial", 10),
                fill=rain_color, anchor="center"
            )