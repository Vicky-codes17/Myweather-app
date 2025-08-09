from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage, messagebox
import requests
import json

from src.uv_index import UVIndex
from src.temperature import Temperature
from src.rainfall import Rainfall
from src.air_pressure import AirPressure
from src.wind import Wind
from src.sun_times import SunTimes
from src.hourly_forecast import HourlyForecast


class SimpleWeatherApp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1200x600")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        
        self.is_dark_mode = False
        
        self.current_weather_data = None
        
        # Weather API key
        self.api_key = "9504325ebcb47c038114642f03b01e6e"

        self.uv_handler = UVIndex(self.api_key)
        self.temp_handler = Temperature()
        self.rain_handler = Rainfall()
        self.pressure_handler = AirPressure()
        self.wind_handler = Wind()
        self.sun_handler = SunTimes(self.api_key)
        self.hourly_handler = HourlyForecast(self.api_key)

        # Paths for the resources
        self.output_path = Path(__file__).parent
        self.light_assets = self.output_path / Path(r"assets/Light_Mode")
        self.dark_assets = self.output_path / Path(r"assets/Dark_Mode")
        
        self.canvas = Canvas(
            self.window, bg="#FFFFFF",
            height=600, width=1200, bd=0, highlightthickness=0, relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        self.images = {}
        self.canvas_items = {}
        
        try:
            self.light_toggle = PhotoImage(file="assets/light.png")
            self.dark_toggle = PhotoImage(file="assets/dark.png")
        except:
            self.light_toggle = None
            self.dark_toggle = None
        
        self.load_theme()
        self.setup_click_handlers()
    
    def relative_to_assets(self, path: str) -> Path:
        assets_path = self.dark_assets if self.is_dark_mode else self.light_assets
        return assets_path / Path(path)
    
    def load_theme(self):
        self.canvas.delete("all")
        self.images.clear()
        self.canvas_items.clear()
        self.load_images()
        self.create_ui_elements()
        
        if self.current_weather_data:
            self.display_weather_data(self.current_weather_data)
    
    def load_images(self):
        for i in range(1, 22):
            try:
                self.images[f'image_{i}'] = PhotoImage(
                    file=self.relative_to_assets(f"image_{i}.png")
                )
            except:
                pass
        
        try:
            self.images['entry_1'] = PhotoImage(
                file=self.relative_to_assets("entry_1.png")
            )
        except:
            pass
    
    def create_ui_elements(self):
        # background
        if 'image_1' in self.images:
            self.canvas_items['bg'] = self.canvas.create_image(600, 300, image=self.images['image_1'])
        
        if self.is_dark_mode:
            self.entry = Entry(
                bd=0, bg="#1A1A2E", fg="#FFFFFF", 
                highlightthickness=1, highlightcolor="#4A90E2",
                font=("Arial", 16), relief="flat",
                insertbackground="#FFFFFF"
            )
            self.entry.place(x=120, y=110, width=260, height=40)
            text_color = "#FFFFFF"
            
            # positions for darkmode
            positions = [
                (830.0, 264.0), (832.0, 470.0), (613.0, 63.0), (252.0, 251.0),
                (107.0, 377.0), (255.0, 503.0), (107.0, 503.0), (395.0, 377.0),
                (255.0, 377.0), (420.0, 55.0), (1135.0, 52.0), (88.0, 131.0), 
                (250.0, 248.0), (216.0, 354.0), (371.0, 357.0), (74.0, 483.0),
                (216.0, 483.0), (580.0, 409.0), (570.0, 137.0), (69.0, 354.0)
            ]
        else:
            self.entry = Entry(
                bd=0, bg="#F8F9FA", fg="#2C3E50", 
                highlightthickness=1, highlightcolor="#4A90E2",
                font=("Arial", 16), relief="flat",
                insertbackground="#2C3E50"
            )
            self.entry.place(x=120, y=110, width=260, height=40)
            text_color = "#2C3E50"
            
            # positions for light mode
            positions = [
                (83.0, 131.0), (826.0, 470.0), (613.0, 63.0), (560.0, 136.0),
                (252.0, 251.0), (107.0, 377.0), (255.0, 503.0), (107.0, 503.0),
                (395.0, 377.0), (255.0, 377.0), (420.0, 55.0), None,  
                (830.0, 264.0), (250.0, 253.0), (74.0, 355.0), (218.0, 355.0),
                (369.0, 354.0), (77.0, 481.0), (217.0, 485.0), (580.0, 407.0)
            ]
        
        for i, pos in enumerate(positions, 2):
            if pos is not None and f'image_{i}' in self.images:
                self.canvas_items[f'img_{i}'] = self.canvas.create_image(pos[0], pos[1], image=self.images[f'image_{i}'])
        
        self.create_search_button()
        self.create_toggle_switch()
        self.add_placeholder()
        
        if self.is_dark_mode:
            self.window.configure(bg="#0C1331")
            self.canvas.configure(bg="#0C1331")
        else:
            self.window.configure(bg="#FFFFFF")
            self.canvas.configure(bg="#FFFFFF")
    
    def create_search_button(self):
        search_x, search_y = 400, 130
        
        self.canvas_items['search_bg'] = self.canvas.create_oval(
            search_x - 18, search_y - 18,
            search_x + 18, search_y + 18,
            fill="#4A90E2", outline="#357ABD", width=1
        )
        
        self.canvas_items['search_btn'] = self.canvas.create_text(
            search_x, search_y, text="🔍", font=("Arial", 14), fill="#FFFFFF"
        )
        
        self.search_area = {
            'x1': search_x - 18,
            'y1': search_y - 18,
            'x2': search_x + 18,
            'y2': search_y + 18
        }
    
    def add_placeholder(self):
        #PlaceHolder
        self.entry.insert(0, "Enter city name...")
        self.entry.config(fg="gray")
        
        self.entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.entry.bind("<FocusOut>", self.on_entry_focus_out)
        self.entry.bind("<Return>", lambda e: self.search_weather())
    
    def on_entry_focus_in(self, event):
        if self.entry.get() == "Enter city name...":
            self.entry.delete(0, "end")
            if self.is_dark_mode:
                self.entry.config(fg="#FFFFFF")
            else:
                self.entry.config(fg="#2C3E50")
    
    def on_entry_focus_out(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, "Enter city name...")
            self.entry.config(fg="gray")
    
    def search_weather(self):
        city = self.entry.get().strip()
        
        # Name Correction
        if not city or city == "Enter city name...":
            messagebox.showwarning("Warning", "Please enter a city name!")
            return
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                lat = data['coord']['lat']
                lon = data['coord']['lon']
                
                uv_value = self.uv_handler.get_uv_data(lat, lon)
            
            if response.status_code == 200:
                self.current_weather_data = {
                    'city': city,
                    'country': data['sys']['country'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                    'feels_like': data['main']['feels_like'],
                    'uv_index': uv_value,
                    'clouds': data.get('clouds', {}).get('all', 0),
                    'pressure': data['main']['pressure'],
                    'lat': lat,  
                    'lon': lon 
                }
                
                self.display_weather_data(self.current_weather_data)
                
            else:
                messagebox.showerror("Error", f"City '{city}' not found!\nPlease check the spelling and try again.")
                
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No internet connection!\nPlease check your connection and try again.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong!\nError: {str(e)}")
    
    def display_weather_data(self, weather_data):
        if self.is_dark_mode:
            text_color = "#FFFFFF"
            temp_color = "#4A90E2"
            detail_color = "#E3F2FD"  # Light blue for details in dark mode
            center_x, center_y = 830.0, 264.0
            uv_position = (70.0, 390.0)
            temp_position = (270.0, 395.0) 
            rain_position = (390.0, 385.0)
            pressure_position = (100.0, 520.0)
            wind_position = (270.0, 520.0)
            sun_position = (250.0, 260.0)
            hourly_position = (530.0, 455.0)
        else:
            text_color = "#1A1A1A"  # Darker text for light mode
            temp_color = "#2E7D32"  # Darker green for temperature
            detail_color = "#424242"  # Dark gray for details in light mode
            center_x, center_y = 830.0, 270.0
            uv_position = (70.0, 390.0)
            temp_position = (270.0, 395.0)
            rain_position = (390.0, 385.0)
            pressure_position = (100.0, 520.0)
            wind_position = (270.0, 520.0)  
            sun_position = (250.0, 260.0)
            hourly_position = (530.0, 455.0)

        # UPDATE: Add new weather detail items to cleanup list
        weather_items = ['city_display', 'temp_display', 'desc_display', 'details_display', 
                        'uv_title', 'uv_circle', 'uv_number', 'uv_level',
                        'temp_title', 'temp_number', 'temp_level', 
                        'rain_title', 'rain_number', 'rain_level',
                        'pressure_title', 'pressure_number', 'pressure_level',
                        'wind_title', 'wind_number', 'wind_level',
                        'sun_line', 'sun_current', 'sun_sunrise_time', 'sun_sunset_time', 'sun_title', 'sun_position_dot',
                        'now_label', 'main_temp',
                        'feels_like_label', 'feels_like_temp',
                        'precipitation_label', 'precipitation_value',
                        'humidity_label', 'humidity_value',
                        'wind_label', 'wind_value',
                        'air_quality_label', 'air_quality_value']
        for i in range(7):
            weather_items.extend([
                f'hourly_time_{i}', f'hourly_temp_{i}', f'hourly_icon_{i}',
                f'hourly_desc_{i}', f'hourly_rain_{i}'
        ])

        for item in weather_items:
            if item in self.canvas_items:
                self.canvas.delete(self.canvas_items[item])

        #left side
        left_x = center_x - 180  
        
        self.canvas_items['now_label'] = self.canvas.create_text(
            left_x - 100, center_y - 80, text="Now", 
            font=("Arial", 16, "bold"), 
            fill=text_color, anchor="w"
        )
        
        main_temp = f"{int(weather_data['temperature'])}°"
        self.canvas_items['main_temp'] = self.canvas.create_text(
            left_x - 100, center_y - 30, text=main_temp, 
            font=("Arial", 48, "bold"), 
            fill=temp_color, anchor="w"
        )
        
        feels_like_temp = f"{int(weather_data['feels_like'])}°"
        self.canvas_items['feels_like_label'] = self.canvas.create_text(
            left_x - 75, center_y, text="Feels like", 
            font=("Arial", 12), 
            fill=detail_color, anchor="w"
        )
        self.canvas_items['feels_like_temp'] = self.canvas.create_text(
            left_x + 5, center_y, text=feels_like_temp, 
            font=("Arial", 12, "bold"), 
            fill=temp_color, anchor="w"
        )

        # Right Side
        right_x = center_x + 80  
        
        rain_chance, _ = self.rain_handler.get_rain_chance_and_status(
            weather_data['humidity'], 
            weather_data.get('description', ''), 
            weather_data.get('clouds', 0)
        )
        
        air_quality, air_color = self.get_air_quality_status(
            weather_data.get('pressure', 1013), 
            weather_data.get('humidity', 50)
        )
        
        if not self.is_dark_mode and air_color in ["#F44336", "#FF9800"]:
            pass
        elif not self.is_dark_mode and air_color == "#4CAF50":
            air_color = "#2E7D32"  
        elif not self.is_dark_mode and air_color == "#2196F3":
            air_color = "#1565C0"  
        
        value_color = "#1565C0" if not self.is_dark_mode else "#4A90E2"
        
        # Precipitation
        self.canvas_items['precipitation_label'] = self.canvas.create_text(
            right_x + 65, center_y - 50, text="Precipitation", 
            font=("Arial", 11), 
            fill=detail_color, anchor="w"
        )
        self.canvas_items['precipitation_value'] = self.canvas.create_text(
            right_x + 165, center_y - 50, text=f"{rain_chance}%", 
            font=("Arial", 11, "bold"), 
            fill=value_color, anchor="w"
        )
        
        # Humidity
        self.canvas_items['humidity_label'] = self.canvas.create_text(
            right_x + 65, center_y - 25, text="Humidity", 
            font=("Arial", 11), 
            fill=detail_color, anchor="w"
        )
        self.canvas_items['humidity_value'] = self.canvas.create_text(
            right_x + 165, center_y - 25, text=f"{weather_data['humidity']}%", 
            font=("Arial", 11, "bold"), 
            fill=value_color, anchor="w"
        )
        
        # Wind
        wind_speed = f"{weather_data['wind_speed']:.1f} m/s"
        self.canvas_items['wind_label'] = self.canvas.create_text(
            right_x + 65, center_y, text="Wind", 
            font=("Arial", 11), 
            fill=detail_color, anchor="w"
        )
        self.canvas_items['wind_value'] = self.canvas.create_text(
            right_x + 165, center_y, text=wind_speed, 
            font=("Arial", 11, "bold"), 
            fill=value_color, anchor="w"
        )
        
        # Air Quality
        self.canvas_items['air_quality_label'] = self.canvas.create_text(
            right_x + 65, center_y + 25, text="Air Quality", 
            font=("Arial", 11), 
            fill=detail_color, anchor="w"
        )
        self.canvas_items['air_quality_value'] = self.canvas.create_text(
            right_x + 165, center_y + 25, text=air_quality, 
            font=("Arial", 11, "bold"), 
            fill=air_color, anchor="w"
        )

        #Center
        city_text = f"{weather_data['city']}, {weather_data['country']}"
        self.canvas_items['city_display'] = self.canvas.create_text(
            center_x, center_y - 70, text=city_text, 
            font=("Arial", 20, "bold"), 
            fill=text_color, anchor="center"
        )

        # Display weather description
        desc_text = weather_data['description'].title()
        self.canvas_items['desc_display'] = self.canvas.create_text(
            center_x, center_y + 40, text=desc_text, 
            font=("Arial", 16,"bold"), 
            fill=detail_color, anchor="center"
        )

        # Top
        if 'uv_index' in weather_data:
            self.uv_handler.create_uv_display(
                self.canvas, 
                self.canvas_items, 
                weather_data['uv_index'], 
                uv_position, 
                self.is_dark_mode
            )
        if 'temperature' in weather_data:
            self.temp_handler.create_temp_display(
                self.canvas, 
                self.canvas_items, 
                weather_data['temperature'], 
                temp_position, 
                self.is_dark_mode
            )
        if 'humidity' in weather_data:
            self.rain_handler.create_rain_display(
                self.canvas, 
                self.canvas_items, 
                weather_data['humidity'],
                weather_data.get('description', ''),
                weather_data.get('clouds', 0),
                rain_position, 
                self.is_dark_mode
            )
        if 'pressure' in weather_data:
            self.pressure_handler.create_pressure_display(
                self.canvas, 
                self.canvas_items, 
                weather_data['pressure'], 
                pressure_position, 
                self.is_dark_mode
            )
        if 'wind_speed' in weather_data:
            self.wind_handler.create_wind_display(
                self.canvas, 
                self.canvas_items, 
                weather_data['wind_speed'], 
                wind_position, 
                self.is_dark_mode
            )
        if 'lat' in weather_data and 'lon' in weather_data:
            self.sun_handler.create_sun_timeline(
                self.canvas, 
                self.canvas_items, 
                weather_data['lat'], 
                weather_data['lon'], 
                sun_position, 
                self.is_dark_mode
            )
        if 'lat' in weather_data and 'lon' in weather_data:
            self.hourly_handler.create_hourly_display(
            self.canvas, 
            self.canvas_items, 
            weather_data['lat'], 
            weather_data['lon'], 
            hourly_position, 
            self.is_dark_mode
        )

    
    def create_toggle_switch(self):
        """Create simple toggle switch"""
        toggle_x, toggle_y = 1132, 52
        
        if self.light_toggle and self.dark_toggle:
            current_image = self.dark_toggle if self.is_dark_mode else self.light_toggle
            self.canvas_items['toggle'] = self.canvas.create_image(
                toggle_x, toggle_y, image=current_image
            )
            self.toggle_area = {
                'x1': toggle_x - current_image.width()//2,
                'y1': toggle_y - current_image.height()//2,
                'x2': toggle_x + current_image.width()//2,
                'y2': toggle_y + current_image.height()//2
            }
        else:
            icon = "☀️" if self.is_dark_mode else "🌙"
            bg_color = "#4A5568" if self.is_dark_mode else "#E2E8F0"
            
            self.canvas_items['toggle_bg'] = self.canvas.create_oval(
                toggle_x - 25, toggle_y - 15,
                toggle_x + 25, toggle_y + 15,
                fill=bg_color, outline="#333333", width=1
            )
            self.canvas_items['toggle'] = self.canvas.create_text(
                toggle_x, toggle_y, text=icon, font=("Arial", 20)
            )
            self.toggle_area = {
                'x1': toggle_x - 25, 'y1': toggle_y - 15,
                'x2': toggle_x + 25, 'y2': toggle_y + 15
            }

    
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.load_theme()  
    
    def setup_click_handlers(self):
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Motion>", self.on_mouse_move)
    
    def on_mouse_move(self, event):
        x, y = event.x, event.y
        
        if (hasattr(self, 'toggle_area') and 
            self.toggle_area['x1'] <= x <= self.toggle_area['x2'] and 
            self.toggle_area['y1'] <= y <= self.toggle_area['y2']) or \
           (hasattr(self, 'search_area') and 
            self.search_area['x1'] <= x <= self.search_area['x2'] and 
            self.search_area['y1'] <= y <= self.search_area['y2']):
            self.canvas.config(cursor="hand2")
        else:
            self.canvas.config(cursor="")
    
    def on_click(self, event):
        x, y = event.x, event.y
        
        if hasattr(self, 'toggle_area'):
            if (self.toggle_area['x1'] <= x <= self.toggle_area['x2'] and 
                self.toggle_area['y1'] <= y <= self.toggle_area['y2']):
                self.toggle_theme()
                return
        
        if hasattr(self, 'search_area'):
            if (self.search_area['x1'] <= x <= self.search_area['x2'] and 
                self.search_area['y1'] <= y <= self.search_area['y2']):
                self.search_weather()
                return
    
    def get_air_quality_status(self, pressure, humidity):
      
        if pressure < 1000 or humidity > 80:
            return "Poor", "#F44336"  # Red
        elif 1000 <= pressure <= 1020 and 40 <= humidity <= 60:
            return "Good", "#4CAF50"  # Green
        elif pressure > 1020 and humidity < 40:
            return "Moderate", "#2196F3"  # Blue
        else:
            return "Fair", "#FF9800"  # Orange

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = SimpleWeatherApp()
    app.run()