import os
import tkinter
import tkinter.filedialog as fd
from tkinter import *

# Настройка окна приложения
window = Tk()
window.title("MADNESS sorter")
window.geometry('200x225')
window['bg'] = 'black'
window.resizable(True, True)


# Функция выбора файлов
def choose_files():
    global files, path
    # Кнопка выбора пути
    path = fd.askdirectory(title="Открыть папку", initialdir="/")

    # Список всех файлов в папке
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    # Список всех расширений у файлов
    extentions = list(set([file.split('.')[-1] for file in files]))

    # Настройка кнопки отображения пути до выбранной папки
    entry.insert(20, path)
    entry.config(background='white', width=30)
    intvar_dict.clear()

    for cb in checkbutton_list:
        cb.destroy()
    checkbutton_list.clear()

    # Цикл создания checkbutton для каждого расширения
    for exclusion in extentions:
        intvar_dict[exclusion] = tkinter.IntVar()
        c = tkinter.Checkbutton(window, text=exclusion, variable=intvar_dict[exclusion])
        c.pack()
        checkbutton_list.append(c)


# Функция сортировки файлов по папкам
def sort():
    # Цикл фильтра выбора нажатых расширений у файлов
    for key, value in intvar_dict.items():
        if value.get() > 0:
            try:
                for hold in key:
                    # Создание отдельной папки под каждое расширение
                    os.mkdir(os.path.join(path, key))
                    for bca in files:
                        try:
                            if bca.endswith(key):
                                # Перемещение файла с указанным расширением в соответствующую папку
                                os.replace(os.path.join(path, bca), os.path.join(path, key, bca))
                        except:
                            pass
            except:
                pass
        else:
            print("Не выбрано:", key)


intvar_dict = {}
checkbutton_list = []

# Кнопка выбора папки
qwer = tkinter.Button(window, text="Выбрать папку", command=choose_files)
qwer.pack()

# Окно отображения пути до выбранной папки
entry = tkinter.Entry(window, background='black', borderwidth=0)
entry.pack()

# Кнопка сортировки
btn1 = tkinter.Button(window, text="Рассортировать", command=sort)
btn1.pack()

window.mainloop()
window = tkinter.Tk()
