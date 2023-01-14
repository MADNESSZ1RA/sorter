import os
from tkinter import *

window = Tk()
window.title("MADNESS sorter")
window.geometry('200x150')
window['bg'] = 'blue'


def com():
    path = edit.get()
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


def rabbit():
    pas = abc.get()
    try:
        if pas == "хуй":
            lbl.configure(text="Люблю тебя")
        else:
            pass
    except:
        pass


a = Label(window, font=15, width=25, text='Введите путь', fg='black', borderwidth=0, background='blue')
a.pack()

edit = Entry(window, width=30)
edit.pack()

abc = Entry(window, width=30, background='blue', borderwidth=0)
abc.pack()

but = Button(window, text='Ввод', command=com)
but.pack()

but2 = Button(window, text='      ', command=rabbit, background='blue', borderwidth=0)
but2.pack()

lbl = Label(window, text="", font=("Arial Bold", 20), background='blue', borderwidth=0)
lbl.pack()
window.mainloop()
