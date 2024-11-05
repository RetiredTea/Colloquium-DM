from classes import Polynomial
from classes import IntegerNumber
from classes import NaturalNumber
from classes import RationalNumber
from classes import makePolynomial
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

def RED_Q_Q(rational_number: RationalNumber) -> RationalNumber:
    if(rational_number.denominator == 1):
        return rational_number
    
    temp = RationalNumber(rational_number.numerator, rational_number.denominator)
    nod = euclidean_algorithm(int(rational_number.numerator), int(rational_number.denominator))[3]
    temp.numerator = IntegerNumber(str(int(rational_number.numerator)//nod))
    temp.denominator = NaturalNumber(str(int(rational_number.denominator)//nod))

    return temp

def TRANS_Z_Q(integer_number: IntegerNumber) -> RationalNumber:
    return RationalNumber(str(integer_number))

def ADD_QQ_Q(rational_number1: RationalNumber, rational_number2: RationalNumber) -> RationalNumber:
    # Сложение рациональных чисел:
    # (a/b) + (c/d) = (a*d + b*c) / (b*d)
    # Получаем числители и знаменатели
    a = int(rational_number1.numerator)
    b = int(rational_number1.denominator)
    c = int(rational_number2.numerator)
    d = int(rational_number2.denominator)

    # Вычисляем новый числитель и знаменатель
    new_numerator_value = IntegerNumber(str(a * d + b * c))
    new_denominator_value = NaturalNumber(str(b * d))

    # Возвращаем новый объект RationalNumber
    return RationalNumber(new_numerator_value, new_denominator_value)

def MUL_QQ_Q(rational_number1: RationalNumber, rational_number2: RationalNumber) -> RationalNumber:
    temp = RationalNumber(rational_number1.numerator, rational_number1.denominator)
    if rational_number2.numerator != '0':
        temp.numerator = IntegerNumber(str(int(rational_number1.numerator) * int(rational_number2.numerator)))
        temp.denominator = NaturalNumber(str(int(rational_number1.denominator) * int(rational_number2.denominator)))
    else:
        raise ValueError("Знаменатель не может быть нулём")
    
    return temp

def DIV_QQ_Q(rational_number1: RationalNumber, rational_number2: RationalNumber) -> RationalNumber:
    temp1 = RationalNumber(rational_number1.numerator, rational_number1.denominator)
    temp2 = RationalNumber(rational_number2.numerator, rational_number2.denominator)
    if(temp2.numerator.get_sign() == 1):
        temp2.numerator = IntegerNumber(str(int(temp2.numerator) * (-1)))
        temp1.numerator = IntegerNumber(str(int(temp1.numerator) * (-1)))

    if temp2.numerator != '0':
        temp1.numerator = IntegerNumber(str(int(temp1.numerator) * int(temp2.denominator)))
        temp1.denominator = NaturalNumber(str(int(temp1.denominator) * int(temp2.numerator)))
    else:
        raise ValueError("Знаменатель не может быть нулём")
    
    return temp1

def SUB_PP_P(pln1: Polynomial, pln2: Polynomial) -> Polynomial:
    arr2 = pln2.getDegrees()
    temp = makePolynomial(str(pln1))

    for i in arr2:
        val = DIV_QQ_Q(pln2.getCoeff(NaturalNumber(str(i))), RationalNumber(IntegerNumber("-1")))
        temp.add(i, val)

    return temp

def MUL_Pxk_P(pln: Polynomial, k: NaturalNumber) -> Polynomial:
    temp = makePolynomial(str(pln))
    for i in temp.getDegrees():
        temp.changeDegree(i, NaturalNumber(str(int(i)+int(k))))

    return temp

def MUL_PP_P(pln1: Polynomial, pln2: Polynomial) -> Polynomial:
    arr1 = pln1.getDegrees()
    arr2 = pln2.getDegrees()
    pln = Polynomial()

    for i in arr2:
        for j in arr1:
            val = MUL_QQ_Q(pln2.getCoeff(NaturalNumber(str(i))), pln1.getCoeff(NaturalNumber(str(j))))
            pln.add(NaturalNumber(str(int(j)+int(i))), val)

    return pln

def DIV_PP_P(input_pln1: Polynomial, input_pln2: Polynomial) -> Polynomial:
    pln1 = makePolynomial(str(input_pln1))
    pln2 = makePolynomial(str(input_pln2))
    break_deg = pln2.getDegrees()[0]
    pln = Polynomial()
    while(pln1.getDegrees()[0] >= break_deg):
        val = DIV_QQ_Q(pln1.getCoeff(NaturalNumber(str(pln1.getDegrees()[0]))), pln2.getCoeff(NaturalNumber(str(pln2.getDegrees()[0]))))
        deg = int(pln1.getDegrees()[0]) - int(pln2.getDegrees()[0])

        temp = Polynomial()
        temp.makePolynomial(f"{val}x^{deg}")
        temp = MUL_PP_P(pln2, temp)

        pln1 = SUB_PP_P(pln1, temp)

        pln.add(deg, val)
    return pln

def MOD_PP_P(input_pln1: Polynomial, input_pln2: Polynomial) -> Polynomial:
    pln1 = makePolynomial(str(input_pln1))
    pln2 = makePolynomial(str(input_pln2))
    break_deg = pln2.getDegrees()[0]
    pln = Polynomial()
    while(pln1.getDegrees()[0] >= break_deg):
        val = DIV_QQ_Q(pln1.getCoeff(NaturalNumber(str(pln1.getDegrees()[0]))), pln2.getCoeff(NaturalNumber(str(pln2.getDegrees()[0]))))
        deg = int(pln1.getDegrees()[0]) - int(pln2.getDegrees()[0])

        temp = Polynomial()
        temp.makePolynomial(f"{val}x^{deg}")
        temp = MUL_PP_P(pln2, temp)

        pln1 = SUB_PP_P(pln1, temp)

        pln.add(deg, val)
    return pln1
    
def NMR_P_P(pln: Polynomial) -> str:
    def check_root(pln, val):
        temp = Polynomial()
        temp.makePolynomial(f"x - {val}")
        if(MOD_PP_P(pln, temp) == 0):
            return True
        return False
    
    
    pass

def function_2(input_str1, input_str2):
    try:
        number1 = float(input_str1)
        number2 = float(input_str2)
        result = number1 + number2
        return f"Результат сложения: {result}"
    except ValueError:
        return "Ошибка: оба поля должны содержать корректные числа."
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


#----------------------------------------------------------------------------------------------------------------------------------


'''     Tests
print(RED_Q_Q(RationalNumber(IntegerNumber("1"), NaturalNumber("2"))), RED_Q_Q(RationalNumber(IntegerNumber("2"), NaturalNumber("4"))), RED_Q_Q(RationalNumber(IntegerNumber("10"), NaturalNumber("5"))))
print(TRANS_Z_Q(IntegerNumber("1")), TRANS_Z_Q(IntegerNumber("2")), TRANS_Z_Q(IntegerNumber("10")))
print(DIV_QQ_Q(RationalNumber(IntegerNumber("1"), NaturalNumber("2")), RationalNumber(IntegerNumber("-2"), NaturalNumber("5"))), DIV_QQ_Q(RationalNumber(IntegerNumber("-2"), NaturalNumber("4")), RationalNumber(IntegerNumber("1"))))
pln = Polynomial()
pln1 = Polynomial()
pln.makePolynomial("10x^10 - 1 + 5x^5")
pln1.makePolynomial("9x^10 - x^7 - 2 + 5x^5")
print(SUB_PP_P(pln, pln1).getNiceStr())
print(MUL_Pxk_P(pln, NaturalNumber("100")).getNiceStr())
print(MUL_QQ_Q(RationalNumber(IntegerNumber("1"), NaturalNumber("2")), RationalNumber(IntegerNumber("-5"), NaturalNumber("2"))))
print(MUL_PP_P(pln, pln1).getNiceStr())
poly = Polynomial()
poly = makePolynomial("2x^3-6x^2-26x+30")
poly1 = makePolynomial("x-1")
print(DIV_PP_P(poly, poly1).getNiceStr())
poly.clear()
poly1 = Polynomial()
poly = makePolynomial("4x^5 - 3x^3 + x - 1")
poly1 = makePolynomial("2x^2 - 3")
print(MOD_PP_P(poly, poly1).getNiceStr())
'''