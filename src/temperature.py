class Temperature:
    def __init__(self):
        pass
    
    def get_temp_color_and_level(self, temp_value):
        if temp_value is None:
            return "#999999", "N/A"
        
        if temp_value <= 0:
            return "#00BFFF", "FREEZING"  
        elif temp_value <= 10:
            return "#4169E1", "COLD"  
        elif temp_value <= 20:
            return "#32CD32", "COOL"  
        elif temp_value <= 25:
            return "#FFD700", "MILD"  
        elif temp_value <= 30:
            return "#FF8C00", "WARM"  
        elif temp_value <= 35:
            return "#FF4500", "HOT"  
        else:
            return "#DC143C", "EXTREME"  
    
    def create_temp_display(self, canvas, canvas_items, temp_value, position, is_dark_mode):
        temp_x, temp_y = position
        
        temp_items = ['temp_title', 'temp_number', 'temp_level']
        for item in temp_items:
            if item in canvas_items:
                canvas.delete(canvas_items[item])
        
        if temp_value is not None:
            temp_color, temp_level = self.get_temp_color_and_level(temp_value)
            
            if is_dark_mode:
                text_color = "#FFFFFF"
            else:
                text_color = "#2C3E50"
            
            canvas_items['temp_title'] = canvas.create_text(
                temp_x, temp_y - 40, text="TEMP", 
                font=("Arial", 15, "bold"), 
                fill=text_color, anchor="center"
            )
            
            canvas_items['temp_number'] = canvas.create_text(
                temp_x - 8, temp_y - 6, text=f"{int(temp_value)}°", 
                font=("Arial", 15, "bold"), 
                fill=temp_color, anchor="center"  
            )
            
            canvas_items['temp_level'] = canvas.create_text(
                temp_x - 10, temp_y + 12, text=temp_level, 
                font=("Arial", 9, "bold"), 
                fill=text_color, anchor="center"
            )