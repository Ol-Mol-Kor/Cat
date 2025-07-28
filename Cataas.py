from bottle import response
from trinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def loade_image():
    try:
        response = requests.get(url)  # ответ = запросу с сайта
        response.raise_for_status()  # обработка исключений
        image_data = BytesIO(response.content)  #
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None


window = Tk()
window.title('Cats!')
window.geometry('600x480')

label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = loade_image(url)  # загрузка изображений

if img:
    label.config(image=img)
    label.image = img

window.mainloop()


