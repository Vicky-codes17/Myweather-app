from PIL import Image

img = Image.open("assets/icon.png")
img.save("assets/icon.ico", sizes=[(32, 32), (64, 64), (128, 128), (256, 256)])