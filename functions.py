# Примеры использования алгоритма Евклида
# возвращает кортеж
# первое значение кортежа - коэффициенты полученные при расширенном алг. Евк. (например цепная дробь)
# второе значение кортежа - частное решение диофантового уравнения
# третье значение кортежа - общее решение диофантового уравнения
# четвёртое значение кортежа - НОД переданных чисел

#drob, ch_ans, ob_ans, nod = euclidean_algorithm(13, 5)
#     output = ([2, 1, 1, 2], (2, -5), (-5, 13))

#drob = euclidean_algorithm(13, 5)[0]
#     output = [2, 1, 1, 2]

#ch_ans = euclidean_algorithm(13, 5)[1]
#     output = (2, -5)

#ob_ans = euclidean_algorithm(13, 5)[2]
#     output = (-5, 13)

#ob_ans = euclidean_algorithm(13, 5)[3]
#     output = 1

#Алгоритм Евклида
def euclidean_algorithm(a, b):
    def swap(a, b):
        temp = a
        a = b
        b = temp
        return a, b
    coeffs = []
    while(b != 0):
        coeffs.append(a//b)
        a = a%b
        a, b = swap(a, b)
    NOD = a
    a1 = 1
    a2 = 0
    b1 = 0
    b2 = 1
    for i in coeffs:
        a1 -= i*b1
        a2 -= i*b2
        a1, b1 = swap(a1, b1)
        a2, b2 = swap(a2, b2)
    return coeffs, (a1, a2), (b1, b2), NOD

def function_1(input_str):
    """Проверка на ноль"""
    try:
        number = float(input_str)
        if number == 0:
            return "Эта штука работает!!!!"
        else:
            return "Число не равно нулю."
    except ValueError:
        return "Ошибка: введите корректное число."


def trans_n_z(natural_num):
    """Преобразование натурального числа в целое"""
    if type(natural_num) == NaturalNumber: # Проверка типа поданных данных
        int_num = IntegerNumber(natural_num.__str__())
        return int_num
    else:
        raise ValueError("На вход должно подаваться натуральное число.")

def trans_z_n(integer_num):
    """Преобразование целого числа в натуральное"""
    if type(integer_num) == IntegerNumber: # Проверка типа поданных данных
        if integer_num.get_sign()==0: # Проверка знака числа
            natural_num = NaturalNumber(natural_num.__str__())
            return natural_num
        else:
            raise ValueError("Число должно быть неотрицательным")
    else:
        raise ValueError("На вход должно подаваться целое неотрицательное число.")

def function_4():
    print("Функция 4 была вызвана")
def function_5():
    print("Функция 5 была вызвана")
def function_6():
    print("Функция 6 была вызвана")
def function_7():
    print("Функция 7 была вызвана")
def function_8():
    print("Функция 8 была вызвана")
def function_9():
    print("Функция 9 была вызвана")
def function_10():
    print("Функция 10 была вызвана")
def function_11():
    print("Функция 11 была вызвана")
def function_12():
    print("Функция 12 была вызвана")
def function_13():
    print("Функция 13 была вызвана")
def function_14():
    print("Функция 14 была вызвана")
def function_15():
    print("Функция 15 была вызвана")
def function_15():
    print("Функция 15 была вызвана")
def function_16():
    print("Функция 16 была вызвана")
def function_17():
    print("Функция 17 была вызвана")
def function_18():
    print("Функция 18 была вызвана")
def function_19():
    print("Функция 19 была вызвана")
def function_20():
    print("Функция 20 была вызвана")

    #Впишите свое
def function_40():
    print("Функция 45 была вызвана")

# Словарь для маппинга номеров на функции
functions_dict = {
    str(i): globals()[f'function_{i}'] for i in range(1, 20)
}