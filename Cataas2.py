from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

Allowed_tags = ['sleep', 'jump', 'smile', 'fight', 'black', 'white', 'siamese']

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


def open_new_window():  # функция открытия изображений каждое в новом окне
    tag = tag_combobox.get()   # получаем тег от пользователя
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'  # склеиваем УРЛ и введенный тег, если тег существует. добавили тернарный оператор: если тег пустой, то просто переходим на сайт (иначе / мешается)
    img = loade_image(url_tag)  # получаем изображения с тегом (кладем изобрадение сюда из функции loade_image)
    if img:
        new_window = Toplevel()  # Создаем новое вторичное окно
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)  # Добавляем изображение в новое окно
        label.pack()
        label.image = img


def exit_app():
    window.destroy()

window = Tk()
window.title('Cats!')
window.geometry('600x480')

# tag_entry = Entry()    #поле ввода для тегов
# tag_entry.pack()

# update_button = Button(text='Обновить', command=set_image)
# update_button.pack()

menu_bar = Menu(window)  # создаем меню в окне
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)  # чтобы меню не отклеивалось
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command = open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_app)

url = 'https://cataas.com/cat'
tag_label = Label(text='Выбери тег')
tag_label.pack()

tag_combobox = ttk.Combobox(values=Allowed_tags)   #  комбобокс (открывающийся список) для выбора тегов
tag_combobox.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()

window.mainloop()


