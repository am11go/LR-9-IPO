import tkinter as tk
from tkinter import ttk

def on_button_click():
    progressbar.start()
    label.config(text=f"Уважаемый {entry.get()}, идет обработка ваших данных")

root = tk.Tk()
root.title("Оконное приложение")
root.configure(bg='orange')

tk.Label(root, text="Ваше ФИО:").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

tk.Label(root, text="Увлечения:").grid(row=1, column=0)
checkbutton = tk.Checkbutton(root)
checkbutton.grid(row=1, column=1)

progressbar = ttk.Progressbar(root, length=200, mode='indeterminate')
progressbar.grid(row=2, column=0, columnspan=2)

button = tk.Button(root, text="Кнопка", command=on_button_click)
button.grid(row=3, column=0, columnspan=2)

label = tk.Label(root, text="Жми на кнопку!")
label.grid(row=4, column=0, columnspan=2)

root.mainloop()
