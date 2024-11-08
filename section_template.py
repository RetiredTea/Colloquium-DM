import tkinter as tk
from functions import functions_dict
from classes import *


class SectionFrame(tk.Frame):
    def __init__(self, parent, func_number, func_name, result_label):
        super().__init__(parent)

        # Список операций для вывода слева
        operations = [
            "+  - сложение",
            "-  - вычитание",
            "*  - умножение",
            ":  - деление",
            "^  - возведение в степень",
            "%  - остаток",
            "?  - сравнение",
            """　　　　　　　　 　　　 ／ ¯¯｀フ
　　　　　　　　　,　'' ｀ ｀ / 　 　 　 !　 　
　　　　　　　 , ' 　　　　 レ　 _,　 -' ミ
　　　　　　　 ; 　 　 　 　 　`ミ __,xノﾞ､
　　　 　　 　 i　 　　　ﾐ　　　; ,､､､、　ヽ ¸
　　　 　　,.-‐! 　 　 　 ﾐ　　i　　　　｀ヽ.._,,))
　　 　　//´｀｀､　　　　 ミ　ヽ　　　　　(¯`v´¯)
　　　　| l　　 　｀ ｰｰ -‐''ゝ､,,)).　 　　 　 ..`·.¸.·´
　　　 　ヽ.ー─'´)　"""
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

        # Определение категорий функций
        self.single_arg_funcs = ["1", "24", "26", "44","26"]
        self.dual_arg_funcs = {
            "+": ["2", "32","28"],
            "-": ["3","33"],
            "*": ["30", "35", "39"],
            ":": ["31", "40"],
            "%": ["41"],
            "?": ["1"]
        }

        # Создание макета на основе функции
        if func_number in self.single_arg_funcs:
            self.single_input_entry = tk.Entry(central_frame, width=30)
            self.single_input_entry.pack(pady=5)
        else:
            operator = self.get_operator(func_number)
            if operator:
                self.create_dual_input_frame(central_frame, operator)

        # Лейбл для вывода ошибок валидации
        self.error_label = tk.Label(central_frame, text="", fg="red")
        self.error_label.pack(pady=(0, 10))

        # Кнопка для выполнения функции
        self.run_button = tk.Button(central_frame, text="Выполнить",
                                    command=lambda: self.run_function(func_number, result_label))
        self.run_button.pack(pady=10)

        # Лейбл для отображения результата
        self.result_label = tk.Label(central_frame, text="", font=("Arial", 18), fg="White")
        self.result_label.pack(pady=5)


    def get_operator(self, func_number):
        """Определяет оператор для двух аргументов на основе номера функции."""
        for operator, func_list in self.dual_arg_funcs.items():
            if func_number in func_list:
                return operator
        return None

    def create_dual_input_frame(self, parent, operator): #Создает макет с двумя полями ввода и оператором между ними.
        dual_input_frame = tk.Frame(parent)
        dual_input_frame.pack(pady=5)

        self.first_input_entry = tk.Entry(dual_input_frame, width=14)
        self.first_input_entry.pack(side="left", padx=5)

        self.operator_label = tk.Label(dual_input_frame, text=operator, font=("Arial", 12))
        self.operator_label.pack(side="left", padx=5)

        self.second_input_entry = tk.Entry(dual_input_frame, width=14)
        self.second_input_entry.pack(side="left", padx=5)

    def get_inputs(self, func_number): #Возвращает входные данные в зависимости от количества полей ввода.
        if func_number in self.single_arg_funcs:
            return [self.single_input_entry.get()]
        return [self.first_input_entry.get(), self.second_input_entry.get()]

    def run_function(self, func_number, result_label):
        """Выполняет функцию в зависимости от макета и отображает результат."""
        args = self.get_inputs(func_number)
        if 0 <= int(func_number) <= 13:
            args = [NaturalNumber(arg) for arg in args]
        elif 14 <= int(func_number) <= 23:
            args = [IntegerNumber(arg) for arg in args]
        elif 24 <= int(func_number) <= 31:
            res = []
            for i in range(len(args)):
                args[i] = args[i].split("/")
                res.append(RationalNumber(IntegerNumber(args[i][0]), NaturalNumber(args[i][1])))
            args = res
        elif 32 <= int(func_number) <= 44:
            pass

        function = functions_dict.get(func_number)

        if function:
            validation_error = self.validate_input(args)
            if validation_error:
                self.error_label.config(text=validation_error)
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
        if len(args) == 1:
            if not str(args)[0].strip():
                return "Ошибка: введите значение."
        elif len(args) == 2:
            if not str(args)[0].strip() or not str(args)[1].strip():
                return "Ошибка: оба поля должны быть заполнены."
        return None  # Нет ошибок
