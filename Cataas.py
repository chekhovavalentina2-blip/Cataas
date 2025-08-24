from tkinter import *
from PIL import ImageTk
import requests
from io import BytesIO

window = Tk()
window.title("Cats")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://cataas.com/cat"
ing = load_image(url)

if ing:
    label.config(image=ing)
    label.image = ing

window.mainloop()
