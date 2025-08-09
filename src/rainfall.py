class Rainfall:
    def __init__(self):
        pass
    
    def get_rain_chance_and_status(self, humidity, weather_desc, clouds):
        
        if humidity <= 30:
            base_chance = 5
        elif humidity <= 50:
            base_chance = 15
        elif humidity <= 70:
            base_chance = 35
        elif humidity <= 85:
            base_chance = 60
        else:
            base_chance = 80
        
        weather_lower = weather_desc.lower()
        if any(word in weather_lower for word in ['rain', 'drizzle', 'shower']):
            base_chance = min(90, base_chance + 40)
        elif any(word in weather_lower for word in ['storm', 'thunderstorm']):
            base_chance = min(95, base_chance + 50)
        elif any(word in weather_lower for word in ['cloud', 'overcast']):
            base_chance = min(70, base_chance + 20)
        elif any(word in weather_lower for word in ['clear', 'sunny']):
            base_chance = max(0, base_chance - 30)
        elif any(word in weather_lower for word in ['mist', 'fog']):
            base_chance = min(60, base_chance + 15)
        
        if clouds:
            if clouds >= 80:
                base_chance = min(85, base_chance + 15)
            elif clouds >= 60:
                base_chance = min(70, base_chance + 10)
            elif clouds <= 20:
                base_chance = max(5, base_chance - 15)
        
        rain_chance = max(0, min(100, base_chance))
        
        return rain_chance, self.get_rain_status(rain_chance)
    
    def get_rain_status(self, rain_chance):
        if rain_chance <= 10:
            return "NO RAIN"
        elif rain_chance <= 25:
            return "LOW CHANCE"
        elif rain_chance <= 45:
            return "POSSIBLE"
        elif rain_chance <= 65:
            return "LIKELY"
        elif rain_chance <= 80:
            return "SHOWERS"
        else:
            return "HEAVY RAIN"
    
    def get_rain_color(self, rain_chance):
        if rain_chance <= 10:
            return "#4CAF50"  
        elif rain_chance <= 25:
            return "#8BC34A"  
        elif rain_chance <= 45:
            return "#FFC107" 
        elif rain_chance <= 65:
            return "#FF9800"  
        elif rain_chance <= 80:
            return "#FF5722"  
        else:
            return "#F44336"  
    
    def create_rain_display(self, canvas, canvas_items, humidity, weather_desc, clouds, position, is_dark_mode):
        rain_x, rain_y = position
        
        rain_items = ['rain_title', 'rain_number', 'rain_level']
        for item in rain_items:
            if item in canvas_items:
                canvas.delete(canvas_items[item])
        
        if humidity is not None:
            rain_chance, rain_status = self.get_rain_chance_and_status(humidity, weather_desc or "", clouds or 0)
            rain_color = self.get_rain_color(rain_chance)
            
            if is_dark_mode:
                text_color = "#FFFFFF"
            else:
                text_color = "#2C3E50"
            
            canvas_items['rain_title'] = canvas.create_text(
                rain_x + 34, rain_y - 29, text="RAIN", 
                font=("Arial", 15, "bold"), 
                fill=text_color, anchor="center"
            )
            
            canvas_items['rain_number'] = canvas.create_text(
                rain_x, rain_y + 2, text=f"{rain_chance}%", 
                font=("Arial", 12, "bold"), 
                fill=rain_color, anchor="center" 
            )
            
            canvas_items['rain_level'] = canvas.create_text(
                rain_x, rain_y + 19, text=rain_status, 
                font=("Arial", 8, "bold"), 
                fill=text_color, anchor="center"
            )