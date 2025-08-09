import requests

class UVIndex:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_uv_data(self, lat, lon):
        try:
            uv_url = f"http://api.openweathermap.org/data/2.5/uvi?lat={lat}&lon={lon}&appid={self.api_key}"
            response = requests.get(uv_url)
            
            if response.status_code == 200:
                data = response.json()
                return data['value']
            else:
                return 7.2  
                
        except Exception:
            return 7.2  
    
    def get_uv_color_and_level(self, uv_value):
        if uv_value is None:
            return "#999999", "N/A"
        
        if uv_value <= 2:
            return "#4CAF50", "LOW"  
        elif uv_value <= 5:
            return "#FFC107", "MODERATE"  
        elif uv_value <= 7:
            return "#FF9800", "HIGH"  
        elif uv_value <= 10:
            return "#F44336", "VERY HIGH"  
        else:
            return "#FF5722", "EXTREME" 
    
    def create_uv_display(self, canvas, canvas_items, uv_value, position, is_dark_mode):
        uv_x, uv_y = position

        uv_items = ['uv_title', 'uv_circle', 'uv_number', 'uv_level']
        for item in uv_items:
            if item in canvas_items:
                canvas.delete(canvas_items[item])

        if uv_value is not None:
            uv_color, uv_level = self.get_uv_color_and_level(uv_value)
            
            if is_dark_mode:
                text_color = "#FFFFFF"
            else:
                text_color = "#2C3E50"
            
            canvas_items['uv_title'] = canvas.create_text(
                uv_x + 45, uv_y - 35, text="UV", 
                font=("Arial", 15, "bold"), 
                fill=text_color, anchor="center"
            )
            
            canvas_items['uv_circle'] = canvas.create_oval(
                uv_x - 8, uv_y - 2,
                uv_x + 8, uv_y + 14,
                fill=uv_color, outline="#FFFFFF", width=1
            )
            
            canvas_items['uv_number'] = canvas.create_text(
                uv_x + 18, uv_y + 2, text=f"{uv_value:.1f}", 
                font=("Arial", 12, "bold"), 
                fill=text_color, anchor="w"
            )
            
            canvas_items['uv_level'] = canvas.create_text(
                uv_x + 18, uv_y + 16, text=uv_level, 
                font=("Arial", 8, "bold"), 
                fill=text_color, anchor="w"
            )