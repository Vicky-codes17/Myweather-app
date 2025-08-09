from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1200x600")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=1200,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(600.0, 300.0, image=image_image_1)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(251.0, 130.5, image=entry_image_1)
entry_1 = Entry(
    bd=2,
    bg="#0D101B",
    fg="#F9F9FA",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_1.place(
    x=115.5,
    y=105.0,
    width=320.0,
    height=50.0
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(830.0, 264.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(832.0, 470.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(613.0, 63.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(252.0, 251.0, image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(107.0, 377.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(255.0, 503.0, image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(107.0, 503.0, image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(395.0, 377.0, image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(255.0, 377.0, image=image_image_10)

image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(408.0, 52.0, image=image_image_11)

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(1135.0, 52.0, image=image_image_12)

image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(88.0, 131.0, image=image_image_13)

image_image_14 = PhotoImage(file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(250.0, 248.0, image=image_image_14)

canvas.create_text(
    129.0,
    121.0,
    anchor="nw",
    text="Find Location..",
    fill="#AFAFAF",
    font=("Arial", 18)
)

image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(216.0, 354.0, image=image_image_15)

image_image_16 = PhotoImage(file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(371.0, 357.0, image=image_image_16)

image_image_17 = PhotoImage(file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(74.0, 483.0, image=image_image_17)

image_image_18 = PhotoImage(file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(216.0, 483.0, image=image_image_18)

image_image_19 = PhotoImage(file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(580.0, 409.0, image=image_image_19)

image_image_20 = PhotoImage(file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(580.0, 137.0, image=image_image_20)

image_image_21 = PhotoImage(file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(69.0, 354.0, image=image_image_21)

window.resizable(False, False)
window.mainloop()
