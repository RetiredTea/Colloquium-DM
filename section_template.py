import tkinter as tk
from functions import functions_dict

class SectionFrame(tk.Frame):
    def __init__(self, parent, func_number, func_name, result_label):
        super().__init__(parent)

        # Список операций для вывода слева
        operations = [
            "+  - сложение",
            "-  - вычитание",
            "*  - умножение",
            "/  - деление",
            "^  - возведение в степень",
            "sqrt - квадратный корень"
        ]

        # Фрейм для списка доступных операций
        operations_frame = tk.Frame(self)
        operations_frame.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky="n")

        operations_label = tk.Label(operations_frame, text="Доступные операции:", font=("Arial", 10, "bold"))
        operations_label.pack(anchor="w")

        for operation in operations:
            op_label = tk.Label(operations_frame, text=operation, anchor="w")
            op_label.pack(anchor="w")

        # Центральный фрейм для размещения лейблов и поля ввода
        central_frame = tk.Frame(self)
        central_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        # Лейбл для названия текущего раздела
        self.label = tk.Label(central_frame, text=func_name, font=("Arial", 14))
        self.label.pack(pady=(0, 10))  # Отступ снизу для отделения от поля ввода

        # Поле ввода для данных пользователя
        self.input_entry = tk.Entry(central_frame, width=30)
        self.input_entry.pack(pady=5)

        # Лейбл для вывода ошибок валидации под полем ввода
        self.error_label = tk.Label(central_frame, text="", fg="red")
        self.error_label.pack(pady=(0, 10))

        # Кнопка для выполнения функции
        self.run_button = tk.Button(central_frame, text="Выполнить", command=lambda: self.run_function(func_number, result_label))
        self.run_button.pack(pady=10)

        # Лейбл для отображения результата под кнопкой
        self.result_label = tk.Label(central_frame, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=5)

    def run_function(self, func_number, result_label):
        """Выполняет функцию с номером func_number и отображает результат в result_label."""
        user_input = self.input_entry.get()
        function = functions_dict.get(func_number)  # Получаем функцию по номеру

        if function:
            # Валидация входных данных перед выполнением
            validation_error = self.validate_input(user_input)
            if validation_error:
                self.error_label.config(text=validation_error)  # Вывод ошибки
                self.result_label.config(text="")  # Очищаем поле результата
            else:
                # Вызов функции и отображение результата
                self.error_label.config(text="")
                result_text = function(user_input)  # Выполнение функции с пользовательским вводом
                self.result_label.config(text=result_text)  # Отображение результата

    def validate_input(self, user_input):
        """Валидация данных, введённых пользователем, перед отправкой в функцию."""
        if not user_input.strip():
            return "Ошибка: введите данные."
        return None  # Нет ошибок
