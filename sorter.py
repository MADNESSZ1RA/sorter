import os
import tkinter
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import *

window = Tk()
window.title("MADNESS sorter")
window.geometry('200x150')
window['bg'] = 'blue'


def choose_files():
    global files, path, extentions
    path = fd.askdirectory(title="Открыть папку", initialdir="/")
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    extentions = list(set([file.split('.')[-1] for file in files]))
    for exclusion in extentions:
        exclusion = tkinter.Checkbutton(window, text=exclusion, command=kiejgnbwek)
        exclusion.pack()


def kiejgnbwek():
    for abc in extentions:
        try:
            os.mkdir(os.path.join(path, abc))
        except:
            pass
        for bca in files:
            print(bca)
            print(abc)
            print(path)
            try:
                if bca.endswith(abc):
                    os.replace(os.path.join(path, bca, abc), os.path.join(path, abc, bca))
            except:
                pass

qwer = tkinter.Button(window, text='Выбрать файл', command=choose_files)
qwer.pack()

# sorter = tkinter.Button(window, text='Рассортировать', command=)
# sorter.pack()

if __name__ == "__main__":
    window.mainloop()
