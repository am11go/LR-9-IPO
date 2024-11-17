import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Создание основного окна
root = tk.Tk()

# Надпись Label
label = tk.Label(root, text="Кликни")
label.grid(row=0, column=0)

# Кнопка Button
def on_button_click():
    print("Button clicked")
button = tk.Button(root, text="Кнопка", command=on_button_click)
button.grid(row=1, column=0)

# Поле ввода Entry
entry = tk.Entry(root)
entry.grid(row=2, column=0)

# Многострочное поле ввода Text
text = tk.Text(root)
text.grid(row=3, column=0)

# Рамка Frame
frame = tk.Frame(root)
frame.grid(row=4, column=0)

# Рамка с надписью LabelFrame
labelframe = tk.LabelFrame(root, text="Рамка")
labelframe.grid(row=5, column=0)

# Всплывающее окно messagebox
def show_messagebox():
    messagebox.showinfo("Напоминание", "Хорошего дня!")
messagebox_button = tk.Button(root, text="Что там?", command=show_messagebox)
messagebox_button.grid(row=6, column=0)

# Переключатель Radiobutton
v = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="1", variable=v, value=1)
radiobutton1.grid(row=7, column=0)
radiobutton2 = tk.Radiobutton(root, text="2", variable=v, value=2)
radiobutton2.grid(row=8, column=0)

# Независимый переключатель Checkbutton
checkbutton = tk.Checkbutton(root, text="Поставь галочку")
checkbutton.grid(row=9, column=0)

# Шкала Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.grid(row=11, column=0)

# Прокрутка Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=1, column=1, sticky='ns')

# Меню Menu
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Новый")
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Сохранить в файл..")
filemenu.add_command(label="Выход")

# Раскрывающийся список Combobox
combobox = ttk.Combobox(root, values=["Илья", "Евгений", "Максим", "Леша"])
combobox.grid(row=2, column=1)

# Поле ввода со стрелками приращения и уменьшения Spinbox
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.grid(row=3, column=1)

# Полоса прогресса Progressbar
progressbar = ttk.Progressbar(root, length=200, mode='indeterminate')
progressbar.grid(row=4, column=1)

# Диалоговые окна открытия и сохранения файлов filedialog
def open_file():
    filename = filedialog.askopenfilename()
open_file_button = tk.Button(root, text="Обзор...", command=open_file)
open_file_button.grid(row=5, column=1)

# Дочерние окна Toplevel
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Новое окно")
new_window_button = tk.Button(root, text="Открыть новое окно", command=open_new_window)
new_window_button.grid(row=6, column=1)

# Списки Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "1 пара")
listbox.insert(2, "2 пара")
listbox.insert(3, "3 пара")
listbox.insert(4, "4 пара")
listbox.grid(row=1, column=1)

root.mainloop()
