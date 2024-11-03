# Примеры использования алгоритма Евклида
# возвращает кортеж
# первое значение кортежа - коэффициенты полученные при расширенном алг. Евк. (например цепная дробь)
# второе значение кортежа - частное решение диофантового уравнения
# третье значение кортежа - общее решение диофантового уравнения
# четвёртое значение кортежа - НОД переданных чисел

#drob, ch_ans, ob_ans, nod = euclidean_algorithm(13, 5)
#     output = ([2, 1, 1, 2], (2, -5), (-5, 13)), 1

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
    # Функция меняющая между собой значения 2 переданных переменных
    def swap(a, b):
        return b, a
    
    # Коэффициенты алгоритма Евклида
    coeffs = []

    # Применяем алгоритм Евклида
    while(b != 0):
        coeffs.append(a//b)
        a = a%b
        a, b = swap(a, b)

    # Записываем результаты алгоритма Евклида
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
        
    # Возвращаем результаты
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


def function_2():
    print("Функция 2 была вызвана")

def function_3():
    print("Функция 3 была вызвана")
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

def func_q1(rational_number):
    if(rational_number.denomirator == 1):
        return rational_number
    nod = euclidean_algorithm(rational_number.numerator, rational_number.denomirator)[3]
    rational_number.numerator = rational_number.numerator//nod
    rational_number.denomirator = rational_number.denomirator//nod
    return class_rational_number

def func_q3(value):
    return rational_number(value, 1)

def func_q8(rational_number1, rational_number2):
    rational_number1.numerator *= rational_number2.denomirator
    rational_number1.denomirator *= rational_number2.numerator
    return func_q1(rational_number1)

def func_p2(pln1, pln2):
    arr1 = pln1.getDegrees()
    arr2 = pln2.getDegrees()
    for i in arr2:
        val = 0 - pln2.getCoeff(i)
        pln1.add(i, val)
    return pln1

def func_p4(pln, k):
    for i in pln.getDegrees():
        pln.changeDegree(i, i+k)
    return pln

def func_p8(pln1, pln2):
    arr1 = pln1.getDegrees()
    arr2 = pln2.getDegrees()
    pln = Polynomial()
    for i in arr2:
        val = pln2.getCoeff(i)
        for j in arr1:
            pln.add(j+i, val*pln1.getCoeff(j))
    return pln

def func_p9(pln1, pln2):
    pln = Polynomial()
    break_deg = pln2.getDegrees()[0]
    while(pln1.getDegrees()[0] >= break_deg):
        val = pln1.getCoeff(pln1.getDegrees()[0]) // pln2.getCoeff(pln2.getDegrees()[0])
        deg = pln1.getDegrees()[0] - pln2.getDegrees()[0]
        temp = Polynomial()
        temp.makePolynomial(f"{val}x^{deg}")
        pln1 = func_p2(pln1, func_p8(pln2, temp))
        pln.add(deg, val)
    return pln

def func_p10(pln1, pln2):
    break_deg = pln2.getDegrees()[0]
    while(pln1.getDegrees()[0] >= break_deg):
        val = pln1.getCoeff(pln1.getDegrees()[0]) // pln2.getCoeff(pln2.getDegrees()[0])
        deg = pln1.getDegrees()[0] - pln2.getDegrees()[0]
        temp = Polynomial()
        temp.makePolynomial(f"{val}x^{deg}")
        pln1 = func_p2(pln1, func_p8(pln2, temp))
    return pln1
    
def func_p13(pln1):
    def check_root(pln, val):
        temp = Polynomial()
        temp.makePolynomial(f"x - {val}")
        if(func_p10(pln, temp) == 0):
            return True
        return False
    
    
    pass

# Словарь для маппинга номеров на функции
functions_dict = {
    str(i): globals()[f'function_{i}'] for i in range(1, 20)
}