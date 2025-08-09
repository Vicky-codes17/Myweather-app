import math
from datetime import datetime, timezone
import requests
from tkinter import PhotoImage
from pathlib import Path

class SunTimes:
    def __init__(self, api_key):
        self.api_key = api_key
        self.sun_icon = None
        self.moon_icon = None
        self.load_icons()
    
    def load_icons(self):
        try:
            self.sun_icon = PhotoImage(file="assets/sun_icon.png")
            self.moon_icon = PhotoImage(file="assets/moon_icon.png")
        except:
            self.sun_icon = None
            self.moon_icon = None
    
    def get_sun_times(self, lat, lon):
        """Get sunrise and sunset times from API"""
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                sunrise_timestamp = data['sys']['sunrise']
                sunset_timestamp = data['sys']['sunset']
                timezone_offset = data['timezone'] 
                
                sunrise = datetime.fromtimestamp(sunrise_timestamp + timezone_offset, tz=timezone.utc)
                sunset = datetime.fromtimestamp(sunset_timestamp + timezone_offset, tz=timezone.utc)
                
                return sunrise, sunset
            else:
                return self.get_default_times()
                
        except Exception:
            return self.get_default_times()
    
    def get_default_times(self):
        now = datetime.now()
        sunrise = now.replace(hour=6, minute=30, second=0, microsecond=0)
        sunset = now.replace(hour=18, minute=45, second=0, microsecond=0)
        return sunrise, sunset
    
    def get_current_sun_position(self, sunrise, sunset, current_time=None):
        if current_time is None:
            current_time = datetime.now()
        
        sunrise_minutes = sunrise.hour * 60 + sunrise.minute
        sunset_minutes = sunset.hour * 60 + sunset.minute
        current_minutes = current_time.hour * 60 + current_time.minute
        
        if current_minutes < sunrise_minutes or current_minutes > sunset_minutes:
            return None  
        
        daylight_duration = sunset_minutes - sunrise_minutes
        elapsed_time = current_minutes - sunrise_minutes
        
        return max(0.0, min(1.0, elapsed_time / daylight_duration))
    
    def is_daytime(self, sunrise, sunset, current_time=None):
        if current_time is None:
            current_time = datetime.now()
        
        current_minutes = current_time.hour * 60 + current_time.minute
        sunrise_minutes = sunrise.hour * 60 + sunrise.minute
        sunset_minutes = sunset.hour * 60 + sunset.minute
        
        return sunrise_minutes <= current_minutes <= sunset_minutes
    
    def create_sun_timeline(self, canvas, canvas_items, lat, lon, position, is_dark_mode):
        sun_x, sun_y = position

        sun_items = ['sun_line', 'sun_current', 'sun_sunrise_time', 
                    'sun_sunset_time', 'sun_title', 'sun_position_dot']
        for item in sun_items:
            if item in canvas_items:
                canvas.delete(canvas_items[item])

        sunrise, sunset = self.get_sun_times(lat, lon)
        current_position = self.get_current_sun_position(sunrise, sunset)
        is_day = self.is_daytime(sunrise, sunset)

        if is_dark_mode:
            text_color = "#FFFFFF"
            line_color = "#4A90E2"
            position_color = "#FFD700" if is_day else "#C0C0C0"  
        else:
            text_color = "#2C3E50"
            line_color = "#3498DB"
            position_color = "#FF6B35" if is_day else "#6B7280"  

        # Title
        # canvas_items['sun_title'] = canvas.create_text(
        #     sun_x, sun_y - 30, text="SUN TIMES", 
        #     font=("Arial", 10, "bold"), 
        #     fill=text_color, anchor="center"
        # )

        line_width = 350
        line_start_x = sun_x - 175
        line_end_x = sun_x + 175

        canvas_items['sun_line'] = canvas.create_line(
            line_start_x, sun_y,
            line_end_x, sun_y,
            fill=line_color, width=3
        )

        if current_position is not None:
            sun_pos_x = line_start_x + (line_width * current_position)

            canvas_items['sun_position_dot'] = canvas.create_oval(
                sun_pos_x - 5, sun_y - 5,
                sun_pos_x + 5, sun_y + 5,
                fill=position_color, outline="#FFFFFF", width=2
            )

        sunrise_time = sunrise.strftime("%H:%M")
        sunrise_x = line_start_x

        canvas_items['sun_sunrise_time'] = canvas.create_text(
            sunrise_x, sun_y + 18, text=f"↑ {sunrise_time}", 
            font=("Arial", 9, "bold"), 
            fill=text_color, anchor="center"
        )

        sunset_time = sunset.strftime("%H:%M")
        sunset_x = line_end_x

        canvas_items['sun_sunset_time'] = canvas.create_text(
            sunset_x, sun_y + 18, text=f"↓ {sunset_time}", 
            font=("Arial", 9, "bold"), 
            fill=text_color, anchor="center"
        )

        current_time = datetime.now().strftime("%H:%M")
        status_text = "DAY" if is_day else "NIGHT"
        status_color = "#4CAF50" if is_day else "#9E9E9E"

        canvas_items['sun_current'] = canvas.create_text(
            sun_x, sun_y + 35, text=f"{current_time} • {status_text}", 
            font=("Arial", 8,"bold"), 
            fill=status_color, anchor="center"
        )