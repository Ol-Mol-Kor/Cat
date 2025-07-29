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


def open_new_window():  # функция обновления изображений
    img = loade_image(url)  # загрузка изображений (кладем изобрадение сюда из функции loade_image)
    if img:
        new_window = Toplevel()
        new.window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img


def exit():
    window.destroy()

window = Tk()
window.title('Cats!')
window.geometry('600x480')

# update_button = Button(text='Обновить', command=set_image)
# update_button.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_cascade(label='Загрузить фото', command = open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)

url = 'https://cataas.com/cat'

set_image()

window.mainloop()


