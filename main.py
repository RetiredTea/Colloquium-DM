import tkinter as tk
from tkinter import ttk
from section_template import SectionFrame


def main():
    root = tk.Tk()
    root.title("Проект, Коллоквиум №1")
    root.geometry("900x500") #900x400
    root.minsize(400, 300)

    # Установка темной темы
    root.tk_setPalette(background='#2e2e2e', foreground='#d3d3d3')  # Темный фон, светлый текст
    style = ttk.Style()

    # Настройка стилей для ttk виджетов
    style.configure("TButton", background="#555", foreground="#d3d3d3", font=("Arial", 10))
    style.configure("TLabel", background="#2e2e2e", foreground="#d3d3d3", font=("Arial", 10))
    style.configure("TCombobox", fieldbackground="#555", background="#555", foreground="#d3d3d3")
    style.configure("TEntry", fieldbackground="#555", background="#555", foreground="#d3d3d3")
    style.configure("TFrame", background="#2e2e2e")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # Словарь с названиями разделов и соответствующими номерами функций
    sections_dict = {
        "Информация": "0",
        "Проверка на ноль": "1",
        "Сложение натуральных чисел": "2",
        "Вычитание чисел": "3",
        "Сокращение дроби": "24",
        "Преобразование целого в дробное": "26",
        "Сложение дробей": "28",
        "Умножение дробей": "30",
        "Деление дробей (делитель отличен от нуля)": "31",
        "Вычитание многочленов": "33",
        "Умножение многочлена на x^k, k-натуральное или 0": "35",
        "Умножение многочленов": "39",
        "Частное от деления многочлена на многочлен при делении с остатком": "40",
        "Остаток от деления многочлена на многочлен при делении с остатком": "41",
        "Преобразование многочлена — кратные корни в простые": "44"
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
    result_label = tk.Label(root, text="", wraplength=500, fg="#d3d3d3")  # Белый текст для результата
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
