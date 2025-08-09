import tkinter as tk
from tkinter import Canvas, PhotoImage, messagebox
import requests
from datetime import datetime
from PIL import Image, ImageTk
import io

API_KEY = '9504325ebcb47c038114642f03b01e6e' 

# Global variable to keep references to images
icon_image_refs = [] 

def fetch_weather_by_city(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != "200":
            raise ValueError("City not found")

        hours, temps, icons = [], [], []
        for item in data['list'][:8]:
            time = datetime.fromtimestamp(item['dt']).strftime('%-I %p')
            temp = round(item['main']['temp'])
            icon_code = item['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

            hours.append(time)
            temps.append(temp)
            icons.append(icon_url)
        return hours, temps, icons
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
        return None, None, None

def draw_weather(city):
    hours, temps, icons = fetch_weather_by_city(city)
    if not hours or not temps or not icons:
        return

    for widget in frame.winfo_children():
        widget.destroy()

    canvas = Canvas(frame, width=800, height=150, bg="#1c2230", highlightthickness=0)
    canvas.pack()

    icon_images = []
    for url in icons:
        img_data = requests.get(url).content
        pil_image = Image.open(io.BytesIO(img_data)).resize((40, 40))
        icon_images.append(ImageTk.PhotoImage(pil_image))

    # Line graph
    for i in range(len(temps)-1):
        x1, y1 = i*100 + 50, 100 - (temps[i] - min(temps))*3
        x2, y2 = (i+1)*100 + 50, 100 - (temps[i+1] - min(temps))*3
        canvas.create_line(x1, y1, x2, y2, fill="#4DD0E1", width=2)
        canvas.create_oval(x1-5, y1-5, x1+5, y1+5, fill="#4DD0E1", outline="")

    x_final, y_final = (len(temps)-1)*100 + 50, 100 - (temps[-1] - min(temps))*3
    canvas.create_oval(x_final-5, y_final-5, x_final+5, y_final+5, fill="#4DD0E1", outline="")

    # Temperature labels
    for i, temp in enumerate(temps):
        x = i*100 + 50
        y = 100 - (temp - min(temps))*3 - 20
        canvas.create_text(x, y, text=f"{temp}°C", fill="white", font=("Arial", 10, "bold"))

    # Icons and time
    for i in range(len(hours)):
        x = i*100 + 30
        tk.Label(frame, image=icon_images[i], bg="#1c2230").place(x=x+15, y=150)
        tk.Label(frame, text=hours[i], fg="white", bg="#1c2230", font=("Arial", 10)).place(x=x+20, y=230)

    # Keep references to avoid garbage collection - store in global variable
    global icon_image_refs
    icon_image_refs = icon_images

def search_weather():
    city = city_entry.get().strip()
    if city:
        draw_weather(city)
    else:
        messagebox.showwarning("Input Needed", "Please enter a city name.")

# === GUI Setup ===
root = tk.Tk()
root.title("Live Weather Forecast")
root.geometry("820x320")
root.config(bg="#1c2230")

tk.Label(root, text="Enter City:", fg="white", bg="#1c2230", font=("Arial", 12)).place(x=10, y=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=20)
city_entry.place(x=100, y=10)
tk.Button(root, text="Search", command=search_weather, bg="#4DD0E1", fg="black", font=("Arial", 10, "bold")).place(x=300, y=8)

frame = tk.Frame(root, bg="#1c2230")
frame.place(x=0, y=50, width=820, height=270)

root.mainloop()