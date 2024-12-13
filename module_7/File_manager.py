import tkinter
import os
from tkinter import filedialog,messagebox


def file_select():
    filename = filedialog.askopenfilename(initialdir="/",title="Выберите файл", filetypes=(('Текстовый файл', '.txt'),
                                                                                           ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)

def show_info():
    messagebox.showinfo("Информация", "Чтобы использовать этот проводник, нажмите кнопку 'Выбрать файл', "
                                        "чтобы открыть текстовый файл. Файл откроется в ассоциированной программе.")

def show_about():
    messagebox.showinfo("О программе", "Автор: Тур Иван\nВерсия: 1.0\nОписание: Простой проводник для"
                                       " открытия текстовых файлов.")

window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black')
window.resizable(False, False)

menu = tkinter.Menu(window)
window.config(menu=menu)

file_menu = tkinter.Menu(menu)
menu.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Выбрать файл', command=file_select)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=window.quit)

help_menu = tkinter.Menu(menu)
menu.add_cascade(label='Справка', menu=help_menu)
help_menu.add_command(label='Информация', command=show_info)
help_menu.add_command(label='О программе', command=show_about)

text = tkinter.Label(window, text='Файл', height=5, width=65, background='silver',foreground='blue')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', foreground='blue',command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()
