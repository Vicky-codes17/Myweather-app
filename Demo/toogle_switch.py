from tkinter import *

root = Tk()
root.title("Toggle Switch")
root.geometry("600x300")
root.config(bg="#CDCCCC")

button_mode = True

def customize(event):
    global button_mode
    if button_mode:
        canvas.itemconfig(toggle_image, image=off)
        root.config(bg="#0C1331")
        canvas.config(bg="#0C1331")  
        button_mode = False
    else:
        canvas.itemconfig(toggle_image, image=on)
        root.config(bg="#CDCCCC") 
        canvas.config(bg="#CDCCCC")  
        button_mode = True

on = PhotoImage(file="assets/light.png")
off = PhotoImage(file="assets/dark.png")

canvas = Canvas(
    root, 
    width=on.width(), 
    height=on.height(),
    bg="#CDCCCC",  
    highlightthickness=0,
    bd=0
)

toggle_image = canvas.create_image(
    on.width()//2, 
    on.height()//2, 
    image=on
)

canvas.bind("<Button-1>", customize)
canvas.bind("<Enter>", lambda e: canvas.config(cursor="hand2"))
canvas.bind("<Leave>", lambda e: canvas.config(cursor=""))

canvas.pack(padx=20, pady=50)

root.mainloop()