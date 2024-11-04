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

        # Левый фрейм для отображения доступных операций
        operations_frame = tk.Frame(self)
        operations_frame.pack(side="left", padx=10, pady=10, anchor="n")

        operations_label = tk.Label(operations_frame, text="Доступные операции:", font=("Arial", 10, "bold"))
        operations_label.pack(anchor="w")

        for operation in operations:
            op_label = tk.Label(operations_frame, text=operation, anchor="w")
            op_label.pack(anchor="w")

        # Центральный фрейм для ввода и вывода
        central_frame = tk.Frame(self)
        central_frame.pack(side="left", padx=10, pady=10, anchor="n")

        # Лейбл для отображения названия функции
        self.label = tk.Label(central_frame, text=func_name, font=("Arial", 14))
        self.label.pack(pady=(0, 10))  # Отступ снизу для отделения от поля ввода


        arr_for_one_arg = ["1", "25", "27", "45"]
        arr_for_two_subtraction = ["2", "34"]
        arr_for_two_аddition = ["3", "29"]
        arr_for_two_multiplication = ["40", "31", "36", "40"]
        arr_for_two_division = ["1", "32", "41"]
        arr_for_two_remainder_of_devision = ["42"]
        arr_for_two_comparison = ["1"]


# -----------------------------------------------------------------------------------------------------------------
        # Определение макета в зависимости от функции
        if  func_number in arr_for_one_arg:                                                   # Макет с одним полем ввода
            self.single_input_entry = tk.Entry(central_frame, width=30)
            self.single_input_entry.pack(pady=5)
        elif func_number in arr_for_two_subtraction:                                                  # Макет с двумя полями ввода "+"
            dual_input_frame = tk.Frame(central_frame)
            dual_input_frame.pack(pady=5)

            self.first_input_entry = tk.Entry(dual_input_frame, width=14)
            self.first_input_entry.pack(side="left", padx=5)

            self.operator_label = tk.Label(dual_input_frame, text="+",
                                           font=("Arial", 12))
            self.operator_label.pack(side="left", padx=5)

            self.second_input_entry = tk.Entry(dual_input_frame, width=14)
            self.second_input_entry.pack(side="left", padx=5)

        elif func_number in arr_for_two_аddition:                                                 # Макет с двумя полями ввода "-"
            dual_input_frame = tk.Frame(central_frame)
            dual_input_frame.pack(pady=5)

            self.first_input_entry = tk.Entry(dual_input_frame, width=14)
            self.first_input_entry.pack(side="left", padx=5)

            self.operator_label = tk.Label(dual_input_frame, text="-",
                                           font=("Arial", 12))
            self.operator_label.pack(side="left", padx=5)

            self.second_input_entry = tk.Entry(dual_input_frame, width=14)
            self.second_input_entry.pack(side="left", padx=5)

        elif func_number in arr_for_two_multiplication:                                           # Макет с двумя полями ввода "*"
            dual_input_frame = tk.Frame(central_frame)
            dual_input_frame.pack(pady=5)

            self.first_input_entry = tk.Entry(dual_input_frame, width=14)
            self.first_input_entry.pack(side="left", padx=5)

            self.operator_label = tk.Label(dual_input_frame, text="*",
                                           font=("Arial", 12))
            self.operator_label.pack(side="left", padx=5)

            self.second_input_entry = tk.Entry(dual_input_frame, width=14)
            self.second_input_entry.pack(side="left", padx=5)

        elif func_number in arr_for_two_division:                                                               # Макет с двумя полями ввода "/"
            dual_input_frame = tk.Frame(central_frame)
            dual_input_frame.pack(pady=5)

            self.first_input_entry = tk.Entry(dual_input_frame, width=14)
            self.first_input_entry.pack(side="left", padx=5)

            self.operator_label = tk.Label(dual_input_frame, text="/",
                                           font=("Arial", 12))
            self.operator_label.pack(side="left", padx=5)

            self.second_input_entry = tk.Entry(dual_input_frame, width=14)
            self.second_input_entry.pack(side="left", padx=5)

        elif func_number in  arr_for_two_comparison:                                         # Макет с двумя полями ввода "?"
            dual_input_frame = tk.Frame(central_frame)
            dual_input_frame.pack(pady=5)

            self.first_input_entry = tk.Entry(dual_input_frame, width=14)
            self.first_input_entry.pack(side="left", padx=5)

            self.operator_label = tk.Label(dual_input_frame, text="?",
                                           font=("Arial", 12))
            self.operator_label.pack(side="left", padx=5)

            self.second_input_entry = tk.Entry(dual_input_frame, width=14)
            self.second_input_entry.pack(side="left", padx=5)

        elif func_number in  arr_for_two_remainder_of_devision:                                         # Макет с двумя полями ввода "?"
            dual_input_frame = tk.Frame(central_frame)
            dual_input_frame.pack(pady=5)

            self.first_input_entry = tk.Entry(dual_input_frame, width=14)
            self.first_input_entry.pack(side="left", padx=5)

            self.operator_label = tk.Label(dual_input_frame, text="%",
                                           font=("Arial", 12))
            self.operator_label.pack(side="left", padx=5)

            self.second_input_entry = tk.Entry(dual_input_frame, width=14)
            self.second_input_entry.pack(side="left", padx=5)


    #-----------------------------------------------------------------------------------------------------------------

        # Лейбл для вывода ошибок валидации
        self.error_label = tk.Label(central_frame, text="", fg="red")
        self.error_label.pack(pady=(0, 10))

        # Кнопка для выполнения функции
        self.run_button = tk.Button(central_frame, text="Выполнить",
                                    command=lambda: self.run_function(func_number, result_label))
        self.run_button.pack(pady=10)

        # Лейбл для отображения результата
        self.result_label = tk.Label(central_frame, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=5)

    def run_function(self, func_number, result_label):
        """Выполняет функцию в зависимости от макета и отображает результат."""
        if func_number == "1":  # Проверка на ноль с одним полем
            user_input = self.single_input_entry.get()
            args = [user_input]
        else:  # Два поля ввода
            first_input = self.first_input_entry.get()
            second_input = self.second_input_entry.get()
            args = [first_input, second_input]

        function = functions_dict.get(func_number)

        if function:
            # Валидация входных данных перед выполнением
            validation_error = self.validate_input(args)
            if validation_error:
                self.error_label.config(text=validation_error)  # Отображение ошибки
                self.result_label.config(text="")  # Очистка поля результата
            else:
                self.error_label.config(text="")  # Очистка ошибок
                try:
                    result_text = function(*args)  # Выполнение функции с аргументами
                    self.result_label.config(text=result_text)  # Отображение результата
                except Exception as e:
                    self.error_label.config(text=f"Ошибка выполнения: {e}")

    def validate_input(self, args):
        """Валидация данных, введённых пользователем, перед отправкой в функцию."""
        if len(args) == 1:  # Проверка для одного аргумента
            if not args[0].strip():
                return "Ошибка: введите значение."
        else:  # Проверка для двух аргументов
            if not args[0].strip() or not args[1].strip():
                return "Ошибка: оба поля должны быть заполнены."
        return None  # Нет ошибок
