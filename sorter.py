import os
import tkinter
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import *

window = Tk()
window.title("MADNESS sorter")
window.geometry('200x225')
window['bg'] = 'black'
window.iconbitmap('E:\фото\l9Ttgvh43bQ (1).ico')


def choose_files():
    global files, path
    path = fd.askdirectory(title="Открыть папку", initialdir="/")
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    extentions = list(set([file.split('.')[-1] for file in files]))
    entry.insert(20, path)
    entry.config(background='white', width=30)
    intvar_dict.clear()

    for cb in checkbutton_list:
        cb.destroy()
    checkbutton_list.clear()

    for exclusion in extentions:
        intvar_dict[exclusion] = tkinter.IntVar()
        c = tkinter.Checkbutton(window, text=exclusion, variable=intvar_dict[exclusion])
        c.pack()
        checkbutton_list.append(c)


def sort():
    for key, value in intvar_dict.items():
        if value.get() > 0:
            try:
                for hold in key:
                    os.mkdir(os.path.join(path, key))
                    for bca in files:
                        try:
                            if bca.endswith(key):
                                os.replace(os.path.join(path, bca), os.path.join(path, key, bca))
                        except:
                            pass
            except:
                pass

        else:
            print("Не выбрано:", key)


intvar_dict = {}
checkbutton_list = []

qwer = tkinter.Button(window, text="Выбрать папку", command=choose_files)
qwer.pack()

entry = tkinter.Entry(window, background='black', borderwidth=0)
entry.pack()

btn1 = tkinter.Button(window, text="Рассортировать", command=sort)
btn1.pack()

window.mainloop()
window = tkinter.Tk()

