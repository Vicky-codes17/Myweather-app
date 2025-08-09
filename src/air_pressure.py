class AirPressure:
    def __init__(self):
        pass
    
    def get_pressure_status_and_trend(self, pressure_hpa):
        if pressure_hpa is None:
            return "N/A", "NO DATA", "#999999"
        
        if pressure_hpa < 980:
            status = "STORMY"
            trend = "FALLING"
            color = "#F44336"  
        elif pressure_hpa < 1000:
            status = "RAINY"
            trend = "LOW"
            color = "#FF9800"  
        elif pressure_hpa < 1013:
            status = "CHANGING"
            trend = "VARIABLE"
            color = "#FFC107"  
        elif pressure_hpa < 1020:
            status = "FAIR"
            trend = "STABLE"
            color = "#4CAF50"  
        elif pressure_hpa < 1030:
            status = "CLEAR"
            trend = "RISING"
            color = "#2196F3"  
        else:
            status = "HIGH"
            trend = "VERY HIGH"
            color = "#9C27B0"  
        
        return status, trend, color
    
    def get_pressure_description(self, pressure_hpa):
        if pressure_hpa is None:
            return "NO DATA"
        
        if pressure_hpa < 980:
            return "SEVERE WEATHER"
        elif pressure_hpa < 1000:
            return "POOR WEATHER"
        elif pressure_hpa < 1013:
            return "UNSETTLED"
        elif pressure_hpa < 1020:
            return "FAIR WEATHER"
        elif pressure_hpa < 1030:
            return "CLEAR SKIES"
        else:
            return "VERY DRY"
    
    def create_pressure_display(self, canvas, canvas_items, pressure_hpa, position, is_dark_mode):
        pressure_x, pressure_y = position
        
        pressure_items = ['pressure_title', 'pressure_number', 'pressure_level']
        for item in pressure_items:
            if item in canvas_items:
                canvas.delete(canvas_items[item])
        
        if pressure_hpa is not None:
            status, trend, pressure_color = self.get_pressure_status_and_trend(pressure_hpa)
            
            if is_dark_mode:
                text_color = "#FFFFFF"
            else:
                text_color = "#2C3E50"
            
            canvas_items['pressure_title'] = canvas.create_text(
                pressure_x + 30, pressure_y - 37, text="PRESSURE", 
                font=("Arial", 10, "bold"), 
                fill=text_color, anchor="center"
            )
            
            canvas_items['pressure_number'] = canvas.create_text(
                pressure_x, pressure_y - 9, text=f"{int(pressure_hpa)}", 
                font=("Arial", 15, "bold"), 
                fill=pressure_color, anchor="center"  
            )
            
            canvas_items['pressure_level'] = canvas.create_text(
                pressure_x, pressure_y + 16, text=status, 
                font=("Arial", 8, "bold"), 
                fill=text_color, anchor="center"
            )