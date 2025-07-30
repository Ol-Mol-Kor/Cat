from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

Allowed_tags = ['sleep', 'jump', 'smile', 'fight', 'black', 'white', 'siamese']

def load_image(url):
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
    img = load_image(url_tag)  # получаем изображения с тегом (кладем изобрадение сюда из функции loade_image)
    if img:
        new_window = Toplevel()  # Создаем новое вторичное окно
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)  # Добавляем изображение в новое окно
        label.pack()
        label.image = img


def random_cat_in_new_window():
    img = load_image('https://cataas.com/cat')
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

menu_bar = Menu(window)  # создаем меню в окне
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)  # чтобы меню не отклеивалось
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command = open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_app)

main_frame = ttk.Frame(window)  # делаем рамку для компановки
main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Настройка сетки
# main_frame.columnconfigure(0, weight=1)  # Первая колонка растягивается
# main_frame.columnconfigure(1, weight=1)  # Вторая колонка растягивается
# main_frame.rowconfigure(1, weight=1)     # Последняя строка растягивается

ttk.Label(main_frame, text='Выбери тег').grid(row=0, column=0, pady=5)
# tag_label.pack()  - не нужен, так как используем grid

tag_combobox = ttk.Combobox(main_frame, values=Allowed_tags)   #  комбобокс (открывающийся список) для выбора тегов
tag_combobox.grid(row=1, column=0, padx=5)
# tag_combobox.pack()

random_cat_button = ttk.Button(main_frame, text='Случайный котик', command=random_cat_in_new_window)
random_cat_button.grid(row=1, column=1, padx=50, pady=5)

load_button = ttk.Button(main_frame, text='Загрузить по тегу', command=open_new_window)
load_button.grid(row=2, column=0, sticky='ew', pady=5)
# load_button.pack()


window.mainloop()




