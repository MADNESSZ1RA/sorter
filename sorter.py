import os
import tkinter
import tkinter.filedialog as fd
from tkinter import *

window = Tk()
window.title("MADNESS sorter")
window.geometry('200x150')
window['bg'] = 'blue'

def com():
    path = fd.askdirectory(title="Открыть папку", initialdir="/")
    if path:
        print(path)

    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    extention = list(set([file.split('.')[-1] for file in files]))

    for abc in extention:
        try:
            os.mkdir(os.path.join(path, abc))
        except:
            pass
        for bca in files:
            try:
                if bca.endswith(abc):
                    os.replace(os.path.join(path, bca), os.path.join(path, abc, bca))
            except:
                pass


qwer = tkinter.Button(window, text='Выбрать файл', command=com)
qwer.pack()

window.mainloop()
