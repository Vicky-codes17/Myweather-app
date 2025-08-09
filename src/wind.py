class Wind:
    def __init__(self):
        pass
    
    def get_wind_color_and_level(self, wind_speed):
        if wind_speed is None:
            return "#999999", "N/A"
        
        if wind_speed <= 1.5:
            return "#4CAF50", "CALM" 
        elif wind_speed <= 3.3:
            return "#8BC34A", "LIGHT AIR"  
        elif wind_speed <= 5.5:
            return "#CDDC39", "LIGHT BREEZE"  
        elif wind_speed <= 7.9:
            return "#FFC107", "GENTLE BREEZE"  
        elif wind_speed <= 10.7:
            return "#FF9800", "MODERATE" 
        elif wind_speed <= 13.8:
            return "#FF5722", "FRESH BREEZE"  
        elif wind_speed <= 17.1:
            return "#F44336", "STRONG BREEZE" 
        elif wind_speed <= 20.7:
            return "#E91E63", "NEAR GALE"  
        elif wind_speed <= 24.4:
            return "#9C27B0", "GALE"  
        elif wind_speed <= 28.4:
            return "#673AB7", "STRONG GALE" 
        else:
            return "#3F51B5", "STORM" 
    
    def get_wind_description(self, wind_speed):
        if wind_speed is None:
            return "NO DATA"
        
        if wind_speed <= 1.5:
            return "CALM CONDITIONS"
        elif wind_speed <= 3.3:
            return "LIGHT AIR"
        elif wind_speed <= 5.5:
            return "LIGHT BREEZE"
        elif wind_speed <= 7.9:
            return "GENTLE BREEZE"
        elif wind_speed <= 10.7:
            return "MODERATE BREEZE"
        elif wind_speed <= 13.8:
            return "FRESH BREEZE"
        elif wind_speed <= 17.1:
            return "STRONG BREEZE"
        elif wind_speed <= 20.7:
            return "NEAR GALE"
        elif wind_speed <= 24.4:
            return "GALE FORCE"
        elif wind_speed <= 28.4:
            return "STRONG GALE"
        else:
            return "STORM FORCE"
    
    def create_wind_display(self, canvas, canvas_items, wind_speed, position, is_dark_mode):
        wind_x, wind_y = position
        
        wind_items = ['wind_title', 'wind_number', 'wind_level']
        for item in wind_items:
            if item in canvas_items:
                canvas.delete(canvas_items[item])
        
        if wind_speed is not None:
            wind_color, wind_level = self.get_wind_color_and_level(wind_speed)
            
            if is_dark_mode:
                text_color = "#FFFFFF"
            else:
                text_color = "#2C3E50"
            
            canvas_items['wind_title'] = canvas.create_text(
                wind_x + 5, wind_y - 40, text="WIND", 
                font=("Arial", 15, "bold"), 
                fill=text_color, anchor="center"
            )
            
            canvas_items['wind_number'] = canvas.create_text(
                wind_x - 16, wind_y - 6, text=f"{wind_speed:.1f}", 
                font=("Arial", 20, "bold"), 
                fill=wind_color, anchor="center"  
            )
            
            canvas_items['wind_level'] = canvas.create_text(
                wind_x - 10, wind_y + 20, text=wind_level, 
                font=("Arial", 10), 
                fill=text_color, anchor="center"
            )