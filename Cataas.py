from tkinter import *
from PIL import ImageTk
import requests
from io import BytesIO


def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

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
