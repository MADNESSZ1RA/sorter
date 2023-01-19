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
    global check, extentions, exclusion, files, path, exclusion
    path = fd.askdirectory(title="Открыть папку", initialdir="/")
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    extentions = list(set([file.split('.')[-1] for file in files]))
    exclusion = IntVar()
    for exclusion in extentions:
        exclusion = tkinter.Checkbutton(window, text=exclusion, textvariable=exclusion, command=command).pack()
        print(exclusion)
        print(extentions)


def command():
    for abc in extentions:
        if exclusion.get() == 0:
            print('etylhknteythlketrryjnh')
            print(abc)
            print(exclusion.get)
        else:
            print('tlkhjnewrtylkhjretwnyhlkerwtnhlkertyjhnletkyjhnk')


qwer = tkinter.Button(window, text='Выбрать файл', command=choose_files)
qwer.pack()

# sorter = tkinter.Button(window, text='Рассортировать', command=)
# sorter.pack()

if __name__ == "__main__":
    window.mainloop()
