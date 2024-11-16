import tkinter as tk
from tkinter import ttk
from section_template import SectionFrame


def main():
    root = tk.Tk()
    root.title("Проект, Коллоквиум №1")
    x = root.winfo_screenwidth()  # размер по горизонтали
    y = root.winfo_screenheight()  # размер по вертикали
    root.geometry('{}x{}'.format(int(x * 0.8), int(y * 0.5)))
    root.minsize(400, 300)

    # Установка темной темы
    root.tk_setPalette(background='#2e2e2e', foreground='#d3d3d3')
    style = ttk.Style()
    style.configure("TButton", background="#555", foreground="#d3d3d3", font=("Arial", 10))
    style.configure("TLabel", background="#2e2e2e", foreground="#d3d3d3", font=("Arial", 10))
    style.configure("TCombobox", fieldbackground="#555", background="#555", foreground="#d3d3d3")
    style.configure("TEntry", fieldbackground="#555", background="#555", foreground="#d3d3d3")
    style.configure("TFrame", background="#2e2e2e")

    # Словарь с названиями разделов и функциями
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

    # Контейнер для верхней панели поиска и списка
    top_frame = tk.Frame(root, background="#2e2e2e")
    top_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=5)

    # Кнопка для переключения темы
    def toggle_theme():
        if root.theme == "dark":
            # Переключение на светлую тему
            root.tk_setPalette(background="white", foreground="black")
            style.configure("TButton", background="#ddd", foreground="black", font=("Arial", 10))
            style.configure("TLabel", background="white", foreground="black", font=("Arial", 10))
            style.configure("TCombobox", fieldbackground="#fff", background="#fff", foreground="black")
            style.configure("TEntry", fieldbackground="#fff", background="#fff", foreground="black")
            style.configure("TFrame", background="white")
            theme_button.config(text="🌙", bg="white", fg="black")
            root.theme = "light"
        else:
            # Переключение на темную тему
            root.tk_setPalette(background="#2e2e2e", foreground="#d3d3d3")
            style.configure("TButton", background="#555", foreground="#d3d3d3", font=("Arial", 10))
            style.configure("TLabel", background="#2e2e2e", foreground="#d3d3d3", font=("Arial", 10))
            style.configure("TCombobox", fieldbackground="#555", background="#555", foreground="#d3d3d3")
            style.configure("TEntry", fieldbackground="#555", background="#555", foreground="#d3d3d3")
            style.configure("TFrame", background="#2e2e2e")
            theme_button.config(text="☀", bg="#2e2e2e", fg="#d3d3d3")
            root.theme = "dark"

    theme_button = tk.Button(top_frame, text="☀", font=("Arial", 10), command=toggle_theme, bg="#2e2e2e", fg="#d3d3d3")
    theme_button.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="nw")

    # Метка "Поиск:"
    search_label = tk.Label(top_frame, text="Поиск:", font=("Arial", 10, "bold"))
    search_label.grid(row=0, column=1, padx=(5, 0), pady=5, sticky="e")

    # Поле ввода для поиска
    search_entry = tk.Entry(top_frame, width=15)
    search_entry.grid(row=0, column=2, padx=(0, 10), pady=5, sticky="e")

    # Метка "Список функций:"
    list_label = tk.Label(top_frame, text="Список функций:", font=("Arial", 10, "bold"), fg="#D3D3D3")
    list_label.grid(row=0, column=3, padx=(5, 0), pady=5, sticky="e")

    # Выпадающий список
    selected_function = tk.StringVar(root)
    dropdown = ttk.Combobox(
        top_frame,
        textvariable=selected_function,
        values=list(sections_dict.keys()),
        state="readonly",
        width=70
    )
    dropdown.grid(row=0, column=4, padx=(0, 10), pady=5, sticky="e")
    dropdown.set("Информация")

    # Контейнер для отображения выбранного раздела
    container = tk.Frame(root, bd=2, relief="groove")
    container.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)

    # Лейбл для вывода результата
    result_label = tk.Label(root, text="", wraplength=500, fg="#d3d3d3")
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

        if func_number == "0":
            current_frame = tk.Frame(container)
            info_label = tk.Label(current_frame,
                                  text="Добро пожаловать в программу!\n"
                                       "Проект выполнили студенты группы 3382",
                                  font=("Arial", 14))
            info_label.pack(expand=True)
        else:
            current_frame = SectionFrame(container, func_number, func_name, result_label)

        current_frame.pack(fill="both", expand=True)

    def filter_dropdown(event=None):
        """Фильтрует список функций на основе введенного текста"""
        search_text = search_entry.get().strip().lower()
        filtered_sections = [section for section in sections_dict if search_text in section.lower()]
        dropdown['values'] = filtered_sections
        if filtered_sections:
            dropdown.set(filtered_sections[0])
        else:
            dropdown.set("Не найдено")

    dropdown.bind("<<ComboboxSelected>>", switch_section)
    search_entry.bind("<KeyRelease>", filter_dropdown)
    switch_section()

    root.theme = "dark"  # Начальная тема

    root.mainloop()


if __name__ == "__main__":
    main()
