from bottle import response
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from pygame.display import update


def loade_image(url):
    try:
        response = requests.get(url)  # ответ = запросу с сайта
        response.raise_for_status()  # обработка исключений
        image_data = BytesIO(response.content)  #  берем обработанное изображение
        img = Image.open(image_data)  # превращаем в нормальное изображение
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)  # регулировка размера изображения
        return ImageTk.PhotoImage(img)  # возвращаем изображение
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None


def set_image():  # функция обновления изображений
    img = loade_image(url)  # загрузка изображений (кладем изобрадение сюда из функции loade_image)
    if img:
        label.config(image=img)  # передаем полученное изображение на метку
        label.image = img

window = Tk()
window.title('Cats!')
window.geometry('600x480')

label = Label()
label.pack()
update_button = Button(text='Обновить', command=set_image)
update_button.pack()

url = 'https://cataas.com/cat'

set_image()

window.mainloop()


