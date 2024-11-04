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

def function_q1(input_str):
    if '/' in input_str:
        num, denom = input_str.split('/')
        rational_number = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
    else:
        rational_number = RationalNumber(IntegerNumber(input_str))
        
    if(rational_number.denominator == 1):
        return rational_number
    
    nod = euclidean_algorithm(int(rational_number.numerator), int(rational_number.denominator))[3]
    rational_number.numerator = IntegerNumber(str(int(rational_number.numerator)//nod))
    rational_number.denominator = NaturalNumber(str(int(rational_number.denominator)//nod))

    return str(rational_number)

def function_q3(input_str):
    return str(RationalNumber(str(IntegerNumber(input_str))))

def function_q5(input_str1: str, input_str2: str):
    if '/' in input_str1:
        num, denom = input_str1.split('/')
        rational_num1 = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
    else:
        rational_num1 = RationalNumber(IntegerNumber(input_str1))
        
    if '/' in input_str2:
        num, denom = input_str2.split('/')
        rational_num2 = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
    else:
        rational_num2 = RationalNumber(IntegerNumber(input_str2))

    # Сложение рациональных чисел:
    # (a/b) + (c/d) = (a*d + b*c) / (b*d)
    
    # Получаем числители и знаменатели
    a = int(rational_num1.numerator)
    b = int(rational_num1.denominator)
    c = int(rational_num2.numerator)
    d = int(rational_num2.denominator)

    # Вычисляем новый числитель и знаменатель
    new_numerator_value = IntegerNumber(str(a * d + b * c))
    new_denominator_value = NaturalNumber(str(b * d))

    # Возвращаем новый объект RationalNumber
    return str(RationalNumber(new_numerator_value, new_denominator_value))

def function_q7(input_str1, input_str2):
    if '/' in input_str1:
        num, denom = input_str1.split('/')
        rational_number1 = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
    else:
        rational_number1 = RationalNumber(IntegerNumber(input_str1))

    if '/' in input_str2:
        num, denom = input_str2.split('/')
        rational_number2 = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
    else:
        rational_number2 = RationalNumber(IntegerNumber(input_str2))

    if rational_number2.numerator != '0':
        rational_number1.numerator = IntegerNumber(str(int(rational_number1.numerator) * int(rational_number2.numerator)))
        rational_number1.denominator = NaturalNumber(str(int(rational_number1.denominator) * int(rational_number2.denominator)))
    else:
        raise ValueError("Знаменатель не может быть нулём")
    
    return str(rational_number1)

def function_q8(input_str1, input_str2):
    if '/' in input_str1:
        num, denom = input_str1.split('/')
        rational_number1 = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
    else:
        rational_number1 = RationalNumber(IntegerNumber(input_str1))

    if '/' in input_str2:
        num, denom = input_str2.split('/')
        rational_number2 = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
    else:
        rational_number2 = RationalNumber(IntegerNumber(input_str2))

    if(rational_number2.numerator.get_sign() == 1):
        rational_number2.numerator = IntegerNumber(str(int(rational_number2.numerator) * (-1)))
        rational_number1.numerator = IntegerNumber(str(int(rational_number1.numerator) * (-1)))

    if rational_number2.numerator != '0':
        rational_number1.numerator = IntegerNumber(str(int(rational_number1.numerator) * int(rational_number2.denominator)))
        rational_number1.denominator = NaturalNumber(str(int(rational_number1.denominator) * int(rational_number2.numerator)))
    else:
        raise ValueError("Знаменатель не может быть нулём")
    
    return str(rational_number1)

def function_p2(input_str1, input_str2):
    pln1 = Polynomial()
    pln1.makePolynomial(input_str1)
    pln2 = Polynomial()
    pln2.makePolynomial(input_str2)
    arr2 = pln2.getDegrees()

    for i in arr2:
        num, denom = function_q8(str(pln2.getCoeff(NaturalNumber(str(i)))), str(RationalNumber("-1"))).split('/')
        val = RationalNumber(IntegerNumber(num), NaturalNumber(denom))

        pln1.add(i, val)

    return str(pln1)

def function_p4(input_str1, input_str2):
    pln = Polynomial()
    pln.makePolynomial(input_str1)
    k = NaturalNumber(input_str2)

    for i in pln.getDegrees():
        pln.changeDegree(i, NaturalNumber(str(int(i)+int(k))))

    return str(pln)

def function_p8(input_str1, input_str2):
    pln1 = Polynomial()
    pln1.makePolynomial(input_str1)
    pln2 = Polynomial()
    pln2.makePolynomial(input_str2)

    arr1 = pln1.getDegrees()
    arr2 = pln2.getDegrees()
    pln = Polynomial()

    for i in arr2:
        val = pln2.getCoeff(NaturalNumber(str(i)))
        for j in arr1:
            num, denom = function_q7(str(val), str(pln1.getCoeff(NaturalNumber(str(j))))).split('/')
            pln.add(NaturalNumber(str(int(j)+int(i))), RationalNumber(IntegerNumber(num), NaturalNumber(denom)))

    return str(pln)

def function_p9(input_str1, input_str2):
    pln1 = Polynomial()
    pln1.makePolynomial(input_str1)
    pln2 = Polynomial()
    pln2.makePolynomial(input_str2)
    pln = Polynomial()

    break_deg = pln2.getDegrees()[0]
    while(pln1.getDegrees()[0] >= break_deg):
        num, denom = function_q8(str(pln1.getCoeff(NaturalNumber(str(pln1.getDegrees()[0])))), str(pln2.getCoeff(NaturalNumber(str(pln2.getDegrees()[0]))))).split('/')
        val = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
        deg = int(pln1.getDegrees()[0]) - int(pln2.getDegrees()[0])

        temp = Polynomial()
        temp.makePolynomial(f"{val}x^{deg}")
        newpln = function_p8(str(pln2), str(temp))
        temp.clear()
        temp.makePolynomial(newpln)

        newpln = function_p2(str(pln1), str(temp))
        pln1.clear()
        pln1.makePolynomial(newpln)

        pln.add(deg, val)
    return str(pln)

def function_p10(input_str1, input_str2):
    pln1 = Polynomial()
    pln1.makePolynomial(input_str1)
    pln2 = Polynomial()
    pln2.makePolynomial(input_str2)
    pln = Polynomial()

    break_deg = pln2.getDegrees()[0]
    while(pln1.getDegrees()[0] >= break_deg):
        num, denom = function_q8(str(pln1.getCoeff(NaturalNumber(str(pln1.getDegrees()[0])))), str(pln2.getCoeff(NaturalNumber(str(pln2.getDegrees()[0]))))).split('/')
        val = RationalNumber(IntegerNumber(num), NaturalNumber(denom))
        deg = int(pln1.getDegrees()[0]) - int(pln2.getDegrees()[0])

        temp = Polynomial()
        temp.makePolynomial(f"{val}x^{deg}")
        newpln = function_p8(str(pln2), str(temp))
        temp.clear()
        temp.makePolynomial(newpln)

        newpln = function_p2(str(pln1), str(temp))
        pln1.clear()
        pln1.makePolynomial(newpln)

        pln.add(deg, val)
    return str(pln1)
    
def function_p13(input_str):
    pln = Polynomial()
    pln.makePolynomial(input_str)

    def check_root(pln, val):
        temp = Polynomial()
        temp.makePolynomial(f"x - {val}")
        if(function_p10(pln, temp) == 0):
            return True
        return False
    
    
    pass

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

# Словарь для маппинга номеров на функции
functions_dict = {
    str(i): globals()[f'function_{i}'] for i in range(1, 20)
}