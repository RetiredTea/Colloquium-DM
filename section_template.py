import tkinter as tk
from functions import functions_dict


class SectionFrame(tk.Frame):
    def __init__(self, parent, func_number, func_name):
        super().__init__(parent)

        # Создаём левую панель с инструкциями по вводу
        instructions_frame = tk.Frame(self, width=200, bg="#f0f0f0", bd=2, relief="sunken")
        instructions_frame.pack(side="left", fill="y")

        instructions_label = tk.Label(instructions_frame, text="Формат ввода операций:", font=("Arial", 10, "bold"))
        instructions_label.pack(pady=5)

        # Список доступных операций
        operations = [
            "+  - сложение",
            "-  - вычитание",
            "^  - возведение в степень",
            "sqrt - квадратный корень"
        ]

        # Отображение операций
        for op in operations:
            label = tk.Label(instructions_frame, text=op, bg="#f0f0f0", anchor="w")
            label.pack(anchor="w", padx=10, pady=2)

        # Основная часть фрейма для раздела
        main_frame = tk.Frame(self)
        main_frame.pack(side="right", fill="both", expand=True)

        # Заголовок с названием раздела
        title_label = tk.Label(main_frame, text=f"{func_name} (Раздел {func_number})", font=("Arial", 14))
        title_label.pack(pady=10)

        # Поле ввода
        self.input_label = tk.Label(main_frame, text=f"Введите данные для {func_name}:")
        self.input_label.pack(pady=5)

        self.input_field = tk.Entry(main_frame)
        self.input_field.pack(pady=5)

        # Поле вывода
        self.output_label = tk.Label(main_frame, text="Результат:")
        self.output_label.pack(pady=5)

        self.output_field = tk.Label(main_frame, text="", bg="white", relief="solid", width=20)
        self.output_field.pack(pady=5)

        # Кнопка для выполнения функции
        self.run_button = tk.Button(main_frame, text="Выполнить", command=lambda: self.run_function(func_number))
        self.run_button.pack(pady=10)

    def run_function(self, func_number):
        # Выполнение соответствующей функции из functions.py
        input_data = self.input_field.get()
        result = functions_dict.get(str(func_number), lambda: "Функция не найдена")()
        self.output_field.config(text=f"{result} для ввода: {input_data}")
