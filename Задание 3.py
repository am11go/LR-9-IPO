import tkinter as tk

def calculate():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
    except ValueError:
        result_label.config(text="Пожалуйста, введите все значения")
        return

    perimeter = 2 * (length + width)
    area = length * width

    if perimeter > area:
        result_label.config(text=f"Периметр больше и равен {perimeter}")
    elif area > perimeter:
        result_label.config(text=f"Площадь больше и равна {area}")
    else:
        result_label.config(text="Периметр и площадь равны")

root = tk.Tk()
root.title("Оконное приложение")

length_label = tk.Label(root, text="Введите длину:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

width_label = tk.Label(root, text="Введите ширину:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
