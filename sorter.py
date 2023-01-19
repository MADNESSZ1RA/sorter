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
    global check, extentions, exclusion, files, path
    path = fd.askdirectory(title="Открыть папку", initialdir="/")
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    extentions = list(set([file.split('.')[-1] for file in files]))
    check = IntVar()
    for exclusion in extentions:
        exclusion = tkinter.Checkbutton(window, text=exclusion, command=kiejgnbwek, variable=check)
        exclusion.pack()
        print(exclusion)
        print(extentions)
        print(check)


def kiejgnbwek():
    for abc in extentions:
        if check.get() == 1:
            for abc in extentions:
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
        else:
            print('ne robit')


qwer = tkinter.Button(window, text='Выбрать файл', command=choose_files)
qwer.pack()

# sorter = tkinter.Button(window, text='Рассортировать', command=)
# sorter.pack()

if __name__ == "__main__":
    window.mainloop()
