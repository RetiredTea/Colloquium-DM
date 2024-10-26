import tkinter as tk
from tkinter import ttk
from section_template import SectionFrame

def main():
    root = tk.Tk()
    root.title("Выбор функции")
    root.geometry("600x400")  #размеры окна

    functions_dict = {      # Словарь с названиями разделов и соответствующими номерами функций
        "Проверка на ноль": 1,
        "Сложение натуральных чисел": 2,
        "Вычитание чисел": 3,
        #и тд, потом добавлю
        "Умножение чисел": 40
    }


    label = tk.Label(root, text="Выберите функцию:") # Выпадающий список для выбора раздела
    label.pack(pady=10)

    selected_function = tk.StringVar(root)
    dropdown = ttk.Combobox(root, textvariable=selected_function, values=list(functions_dict.keys()), state="readonly")
    dropdown.pack(pady=10)
    dropdown.set("Проверка на ноль")  # Начальное значение


    container = tk.Frame(root) # Контейнер для основного раздела
    container.pack(fill="both", expand=True)

    current_frame = None

    # Функция для переключения разделов
    def switch_section():
        nonlocal current_frame
        if current_frame is not None:
            current_frame.destroy()

        func_name = selected_function.get()
        func_number = functions_dict[func_name]


        current_frame = SectionFrame(container, func_number, func_name) # Создаём фрейм с нужным номером функции
        current_frame.pack(fill="both", expand=True)


    tk.Button(root, text="Перейти", command=switch_section).pack(pady=10) # Кнопка для перехода к выбранному разделу

    root.mainloop()

if __name__ == "__main__":
    main()
