import tkinter as tk
from tkinter import ttk
from section_template import SectionFrame


def main():
    root = tk.Tk()
    root.title("Проект, Коллоквиум №1")
    root.geometry("1200x500") #900x400
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
        "N-1 Сравнение натуральных чисел": "1",
        "N-2 Проверка на ноль": "2",
        "N-3 Добавление 1 к натуральному числу": "3",
        "N-4 Сложение натуральных чисел": "4",
        "N-5 Вычитание из первого большего натурального числа второго меньшего или равного": "5",
        "N-6 Умножение натурального числа на цифру": "6",
        "N-7 Умножение натурального числа на 10^k, k-натуральное": "7",
        "N-8 Умножение натуральных чисел": "8",
        """N-9 Вычитание из натурального другого натурального, 
        умноженного на цифру для случая с неотрицательным результатом""": "9",
        "N-10 Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k": "10",
        "N-11 Неполное частное от деления первого натурального числа на второе с остатком ": "11",
        "N-12 Остаток от деления первого натурального числа на второе натуральное ": "12",
        "N-13 НОД натуральных чисел": "13",
        "N-14 НОК натуральных чисел": "14",
        "Z-1 Абсолютная величина числа": "15",
        "Z-2 Определение положительности числа ": "16",
        "Z-3 Умножение целого на (-1)": "17",
        "Z-4 Преобразование натурального в целое": "18",
        "Z-5 Преобразование целого неотрицательного в натуральное": "19",
        "Z-6 Сложение целых чисел": "20",
        "Z-7 Вычитание целых чисел": "21",
        "Z-8 Умножение целых чисел": "22",
        "Z-9 Частное от деления целого на целое ": "23",
        "Z-10 Остаток от деления целого на целое": "24",
        "Q-1 Сокращение дроби": "25",
        "Q-2 Проверка сокращенного дробного на целое": "26",
        "Q-3 Преобразование целого в дробное": "27",
        "Q-4 Преобразование сокращенного дробного в целое": "28",
        "Q-5 Сложение дробей": "29",
        "Q-6 Вычитание дробей": "30",
        "Q-7 Умножение дробей": "31",
        "Q-8 Деление дробей (делитель отличен от нуля)": "32",
        "P-1 Сложение многочленов": "33",
        "P-2 Вычитание многочленов": "34",
        "P-3 Умножение многочлена на рациональное число": "35",
        "P-4 Умножение многочлена на x^k, k-натуральное или 0": "36",
        "P-5 Старший коэффициент многочлена": "37",
        "P-6 Степень многочлена": "38",
        """P-7 Вынесение из многочлена НОК знаменателей 
        коэффициентов и НОД числителей""": "39",
        "P-8 Умножение многочленов": "40",
        "P-9 Частное от деления многочлена на многочлен при делении с остатком": "41",
        "P-10 Остаток от деления многочлена на многочлен при делении с остатком": "42",
        "P-11 НОД многочленов": "43",
        "P-12 Производная многочлена": "44",
        "P-13 Преобразование многочлена — кратные корни в простые": "45"
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
