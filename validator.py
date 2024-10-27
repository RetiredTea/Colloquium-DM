#Файл для отлова ошибок, что бы говорить что конретно не так, позже сделаю
import re

def validate_input(expression):
    # Проверка на допустимые символы (числа, операторы, скобки)
    allowed_chars = re.compile(r'^[\d\+\-\*/\^()sqrt\s]+$')
    if not allowed_chars.match(expression):
        return "Ошибка: Строка содержит недопустимые символы."

    # Проверка на корректность скобок
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "Ошибка: Закрывающая скобка без соответствующей открывающей."
            stack.pop()
    if stack:
        return "Ошибка: Есть незакрытая скобка."

    # Проверка на правильное расположение операторов
    operators_pattern = re.compile(r'[\+\-\*/\^]{2,}|[\+\-\*/\^]$|^[\+\*/\^]')
    if operators_pattern.search(expression):
        return "Ошибка: Неверное расположение операторов (например, 13^*15)."


    sqrt_pattern = re.compile(r'sqrt\(') # Проверка на корректное использование корня sqrt
    if 'sqrt' in expression and not sqrt_pattern.search(expression):
        return "Ошибка: Некорректное использование функции sqrt, пропущена скобка."

    return None  #се проверки пройдены
