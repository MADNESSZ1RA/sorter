import os
import tkinter
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import *

window = Tk()
window.title("MADNESS sorter")
window.geometry('200x150')
window['bg'] = 'blue'

exclusion = ""


def choose_files():
    path = fd.askdirectory(title="Открыть папку", initialdir="/")
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    extention = list(set([file.split('.')[-1] for file in files]))
    for exclusion in extention:
        exclusion = tkinter.Checkbutton(window, text=exclusion, variable=exclusion)
        exclusion.pack()
        print(exclusion)

    if

        try:
            os.mkdir(os.path.join(path, b))
        except:
            pass
        for bca in files:
            try:
                if bca.endswith(b):
                    os.replace(os.path.join(path, bca), os.path.join(path, b, bca))
            except:
                pass


qwer = tkinter.Button(window, text='Выбрать файл', command=choose_files)
qwer.pack()

if __name__ == "__main__":
    window.mainloop()
