import tkinter as tk
from tkinter import ttk
from section_template import SectionFrame
import classes


def main():
    root = tk.Tk()
    root.title("Проект, Коллоквиум №1")
    root.geometry("600x400")
    root.minsize(400, 300)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # Словарь с названиями разделов и соответствующими номерами функций
    sections_dict = {
        "Информация": "0",
        "Проверка на ноль": "1",
        "Сложение натуральных чисел": "2",
        "Вычитание чисел": "3",
        "Сокращение дроби": "25",
        "Преобразование целого в дробное": "27",
        "Сложение дробей": "29",
        "Умножение дробей": "31",
        "Деление дробей (делитель отличен от нуля)": "32",
        "Вычитание многочленов": "34",
        "Умножение многочлена на x^k, k-натуральное или 0": "36",
        "Умножение многочленов": "40",
        "Частное от деления многочлена на многочлен при делении с остатком": "41",
        "Остаток от деления многочлена на многочлен при делении с остатком": "42",
        "Преобразование многочлена — кратные корни в простые": "45"
    }

    # Лейбл "Выберите функцию"
    label = tk.Label(root, text="Выберите функцию:")
    label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # Выпадающий список
    selected_function = tk.StringVar(root)
    dropdown = ttk.Combobox(root, textvariable=selected_function, values=list(sections_dict.keys()), state="readonly")
    dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
    dropdown.set("Информация")

    # Контейнер для отображения выбранного раздела
    container = tk.Frame(root, bd=2, relief="groove")
    container.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)

    # Лейбл для вывода результата
    result_label = tk.Label(root, text="", wraplength=500, fg="black")
    result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Переменная для текущего открытого фрейма
    current_frame = None

    def switch_section(event=None):
        """Переключает на выбранный раздел"""
        nonlocal current_frame
        if current_frame is not None:
            current_frame.destroy()

        func_name = selected_function.get()
        func_number = sections_dict[func_name]

        # Стартовый экран
        if func_number == "0":
            current_frame = tk.Frame(container)
            info_label = tk.Label(current_frame,
            text="Добро пожаловать в программу!\n"
            "Проект выполнили студенты группы 3382 ",
            font=("Arial", 14))
            info_label.pack(expand=True)
        else:
            current_frame = SectionFrame(container, func_number, func_name, result_label)

        current_frame.pack(fill="both", expand=True)

    dropdown.bind("<<ComboboxSelected>>", switch_section)
    switch_section()

    root.mainloop()

if __name__ == "__main__":
    main()
