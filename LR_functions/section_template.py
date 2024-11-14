import tkinter as tk
from functions import functions_dict
from classes import *

class SectionFrame(tk.Frame):
    def __init__(self, parent, func_number, func_name, result_label):
        super().__init__(parent)

        # Создаем основной контейнер для размещения лейблов и полей ввода
        main_container = tk.Frame(self)
        main_container.pack(fill="both")

        # Левый фрейм для отображения доступных операций
        operations_frame = tk.Frame(main_container)
        operations_frame.pack(side="left", padx=10, pady=10, anchor="n")

        operations_label = tk.Label(operations_frame, text="Доступные операции:", font=("Arial", 10, "bold"))
        operations_label.pack(anchor="w")

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

        for operation in operations:
            op_label = tk.Label(operations_frame, text=operation, anchor="w")
            op_label.pack(anchor="w")

        # Центральный фрейм для ввода и вывода, который будет центрироваться в оставшемся пространстве
        central_frame = tk.Frame(main_container)
        central_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        # Центрируем содержимое central_frame по середине
        content_frame = tk.Frame(central_frame)
        content_frame.pack(expand=True)  # Делаем контентный фрейм центрированным

        # Лейбл для отображения названия функции
        self.label = tk.Label(content_frame, text=func_name, font=("Arial", 14), justify="center")
        self.label.pack(pady=(0, 10))

        # Определение категорий функций
        self.single_arg_funcs = ["2", "3", "15", "16", "17"
                                ,"18", "19", "25", "26", "27", "28"
                                ,"37", "38", "39", "44", "45"]
        self.dual_arg_funcs = {
            "+": ["4","20","29","33"],
            "-": ["5","21","30","34"],
            "*": ["6","7","8","22","31","35","36","40"],
            ":": ["11","23","32","41"],
            "%": ["12","24","42"],
            "?": ["1"],
            " ": ["13","14","43","10"]
        }
        self.trio_arg_funcs = ["9"]

        # Создание макета на основе функции
        if func_number in self.single_arg_funcs:
            self.single_input_entry = tk.Entry(content_frame, width=60)
            self.single_input_entry.pack(pady=5)
        elif func_number in self.trio_arg_funcs:
            self.create_trio_input_frame(content_frame)
        else:
            operator = self.get_operator(func_number)
            if operator:
                self.create_dual_input_frame(content_frame, operator)

        # Лейбл для вывода ошибок валидации
        self.error_label = tk.Label(content_frame, text="", fg="red")
        self.error_label.pack(pady=(0, 10))

        # Кнопка для выполнения функции
        self.run_button = tk.Button(content_frame, text="Выполнить",
                                    command=lambda: self.run_function(func_number, result_label))
        self.run_button.pack(pady=10)

        # Лейбл для отображения результата
        self.result_label = tk.Label(content_frame, text="", font=("Arial", 18), fg="#D3D3D3")
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

        self.first_input_entry = tk.Entry(dual_input_frame, width=24)
        self.first_input_entry.pack(side="left", padx=5)

        self.operator_label = tk.Label(dual_input_frame, text=operator, font=("Arial", 12))
        self.operator_label.pack(side="left", padx=5)

        self.second_input_entry = tk.Entry(dual_input_frame, width=24)
        self.second_input_entry.pack(side="left", padx=5)


    def create_trio_input_frame(self, parent):
        trio_input_frame = tk.Frame(parent)
        trio_input_frame.pack(pady=5)

        self.first_input_entry_in_trio = tk.Entry(trio_input_frame, width=24)
        self.first_input_entry_in_trio.pack(side="left", padx=5)

        tk.Label(trio_input_frame, text="-", font=("Arial", 12)).pack(side="left", padx=5)

        self.second_input_entry_in_trio = tk.Entry(trio_input_frame, width=24)
        self.second_input_entry_in_trio.pack(side="left", padx=5)

        tk.Label(trio_input_frame, text="*", font=("Arial", 12)).pack(side="left", padx=5)

        self.tree_input_entry_in_trio = tk.Entry(trio_input_frame, width=24)
        self.tree_input_entry_in_trio.pack(side="left", padx=5)

    def get_inputs(self, func_number):
        if func_number in self.single_arg_funcs:
            return [self.single_input_entry.get()]
        elif func_number in self.trio_arg_funcs:
            return [
                self.first_input_entry_in_trio.get(),
                self.second_input_entry_in_trio.get(),
                self.tree_input_entry_in_trio.get(),
            ]
        return [self.first_input_entry.get(), self.second_input_entry.get()]

    def run_function(self, func_number, result_label):
        """Выполняет функцию в зависимости от макета и отображает результат."""
        args = self.get_inputs(func_number)
        validation_error = self.validate_input(args)
        if validation_error:
            self.error_label.config(text=validation_error)
            self.error_label.config(text="")  # Очистка поля результата
            return
        if 0 <= int(func_number) <= 14: #N
            for arg in args:
                if not arg.isdigit() or int(arg) < 0:
                    self.result_label.config(text="")
                    self.error_label.config(text="")
                    self.error_label.config(text="Ошибка: Надо ввести натуральное число.")
                    return
            if int(func_number) == 6:
                if 0 <= int(args[1]) <= 9:
                    args = [NaturalNumber(arg) for arg in args]
                else:
                    self.result_label.config(text="")
                    self.error_label.config(text="")
                    self.error_label.config(text="Ошибка:во втором поле должна быть введена одна цифра (0-9).")
            else:
                self.result_label.config(text="")
                args = [NaturalNumber(arg) for arg in args]

        elif 15 <= int(func_number) <= 24:  # Z
            if int(func_number) == 18:
                args = [NaturalNumber(arg) for arg in args]
            for arg in args:
                if not (arg.lstrip('-').isdigit()):
                    self.result_label.config(text="")
                    self.error_label.config(text="")
                    self.error_label.config(text="Ошибка: Надо ввести целое число.")
                    return
            else:
                args = [IntegerNumber(arg) for arg in args]

        elif 25 <= int(func_number) <= 32: #Q
            if int(func_number) == 27:
                args = [IntegerNumber(arg) for arg in args]
            else:
                res = []
                for i in range(len(args)):
                    if args[i].count("/") == 0:
                        self.result_label.config(text="")
                        self.error_label.config(text="")
                        self.error_label.config(text="Ошибка: Надо ввести рациональное число.")
                        return
                    args[i] = args[i].split("/")
                    if args[i][1] == "0":
                        self.result_label.config(text="")
                        self.error_label.config(text="")
                        self.error_label.config(text="Знаменатель не может быть нулём")
                    res.append(RationalNumber(IntegerNumber(args[i][0]), NaturalNumber(args[i][1])))
                args = res

        elif 32 <= int(func_number) <= 45: #P
            res = []
            if int(func_number) == 35:
                res.append(makePolynomial(args[0]))
                rational_parts = args[1].split("/")
                if str(NaturalNumber(rational_parts[1])) == "0":
                    self.result_label.config(text="")
                    self.error_label.config(text="")
                    self.error_label.config(text="Знаменатель не может быть нулём")
                res.append(RationalNumber(IntegerNumber(rational_parts[0]), NaturalNumber(rational_parts[1])))
                args = res
            elif int(func_number) == 36:
                res.append(makePolynomial(args[0]))
                res.append(NaturalNumber(args[1]))
                args = res
            else:
                for i in range(len(args)):
                    res.append(makePolynomial(args[i]))
                args = res
        function = functions_dict.get(func_number)

        if function:
            validation_error = self.validate_input(args)
            if validation_error:
                self.error_label.config(text=validation_error)
                self.result_label.config(text="")  # Очистка поля результата
            else:
                if int(func_number) == 39:
                    self.error_label.config(text="")  # Очистка ошибок
                    try:
                        result_text = function(*args)  # Выполнение функции с аргументами
                        result_text = str(result_text)
                        self.result_label.config(text=result_text)  # Отображение результата
                    except Exception as e:
                        self.error_label.config(text=f"Ошибка выполнения: {e}")
                else:
                    self.error_label.config(text="")  # Очистка ошибок
                    try:
                        if int(func_number) == 2:
                            result_text = function(*args)  # Выполнение функции с аргументами
                            self.result_label.config(text=result_text)  # Отображение результата
                        else:
                            result_text = function(*args)  # Выполнение функции с аргументами
                            result_text = makePolynomial(str(result_text))
                            # Опционально чтобы сократить многочлен на константу
                            # result_text.setNiceCoeffs()
                            result_text = result_text.getNiceStr()
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
        elif len(args) == 3:
            if not str(args)[0].strip() or not str(args)[1].strip() or not str(args)[2].strip():
                return "Ошибка: все три поля должны быть заполнены."
        return None  # Нет ошибок
