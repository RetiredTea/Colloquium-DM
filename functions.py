from classes import NaturalNumber, IntegerNumber, RationalNumber, Polynomial, makePolynomial
from technical_functions import *


#-------------------------------------------------------------------------------------------------|
# МОДУЛИ ИЗ ТАБЛИЦЫ                                                                               |
# Ниже необходимо добавить свои модули из таблицы с указанием имени, фамилии и номера группы.     |
# Порядок функций менять нельзя.                                                                  |
#-------------------------------------------------------------------------------------------------|

# Модуль выполнен: Борисов Е.А., гр. 3382.
# Сравнение целых чисел. Результат: 2 - если num1 > num2, 0 - если num1 == num2, иначе 1.
def COM_NN_D(num1: NaturalNumber, num2: NaturalNumber) -> int:
    # Рассматриваем очевидные варианты. Если длина одного из чисел больше, выводится соответствующий результат.
    if len(num1) > len(num2):
        return 2

    elif len(num1) < len(num2):
        return 1

    # Если длины равны, запускается поразрядное сравнение.
    else:
        # Если один из разрядов числа больше разряда другого, выводится соответствующий результат.
        for i in range(len(num1.value)):

            if num1.value[i] > num2.value[i]:
                return 2

            elif num1.value[i] < num2.value[i]:
                return 1

        # Иначе числа равны.
        return 0


def NZER_N_B(num: NaturalNumber):  # N-1  Проверка на ноль: если число не равно нулю, то «да» иначе «нет»
    if int(num) == 0:
        return True
    else:
        return False


def ADD_1N_N(num: NaturalNumber):  # N-3	Добавление 1 к натуральному числу
    num = int(num) + 1
    return NaturalNumber(str(num))


# Модуль выполнен: Борисов Е.А., гр. 3382.
# Сложение натуральных чисел в столбик.
def ADD_NN_N(num1: NaturalNumber, num2: NaturalNumber) -> NaturalNumber:
    # Проверка какое из введённых чисел больше. (Прим. Ссылка на модуль function_n1)
    # Если первое число больше, оно становится первым слагаемым.
    # Разворачиваем массивы value, к первому слагаемому добавляем 0 для случая, если появится лишний разряд.
    # difference_index - индекс, на котором заканчивается второе слагаемое, если оно меньше первого.
    # Если слагаемые равны, то difference_index будет равен len(summand1) - 2.
    if COM_NN_D(num1, num2) == 2:
        summand1 = list(reversed(num1.value)) + [0]
        summand2 = list(reversed(num2.value))
        difference_index = (len(num1) - (len(num1) - len(num2))) - 1

    # Иначе второе становится первым слагаемым.
    # В случае с равными числами перестановка ни на что не влияет.
    # Далее аналогично предыдущему условию.
    else:
        summand1 = list(reversed(num2.value)) + [0]
        summand2 = list(reversed(num1.value))
        difference_index = (len(num2) - (len(num2) - len(num1))) - 1

    # Далее производится поразрядное сложение в пределах длины меньшего (или равного) слагаемого.
    # Текущий разряд становится равен остатку от деления на 10.
    # К следующему разряду прибавляется целая часть от деления на 10.
    for i in range(len(summand2)):
        remainder = (summand1[i] + summand2[i]) % 10
        integer = (summand1[i] + summand2[i]) // 10
        summand1[i] = remainder
        summand1[i + 1] += integer

    # Следующее условие срабатывает, если слагаемые не равны по длине.
    # Поразрядное сложение производится в пределах от difference_index до конца первого слагаемого.
    if difference_index != (len(summand1) - 2):
        for i in range(difference_index, len(summand1) - 1):
            remainder = summand1[i] % 10
            integer = summand1[i] // 10
            summand1[i] = remainder
            summand1[i + 1] += integer

    # Если первый ноль остаётся незначащим, он удаляется.
    if summand1[-1] == 0:
        summand1.pop()

    # Возвращаем результат как объект NaturalNumber.
    result = ''.join(list(map(str, list(reversed(summand1)))))
    return NaturalNumber(result)


# Модуль выполнен: Борисов Е.А., гр. 3382.
# Вычитание из большего натурального числа меньшего.
def SUB_NN_N(num1: NaturalNumber, num2: NaturalNumber) -> NaturalNumber:
    # Проверка какое из введённых чисел больше. (Прим. Ссылка на модуль function_n1)
    # Если первое число больше, оно становится уменьшаемым.
    # Разворачиваем массивы value.
    # difference_index - индекс, на котором заканчивается вычитаемое.
    if COM_NN_D(num1, num2) == 2:
        decrement = list(reversed(num1.value))
        subtraction = list(reversed(num2.value))
        difference_index = (len(num1) - (len(num1) - len(num2))) - 1

    # Иначе второе число становится вычитаемым.
    elif COM_NN_D(num1, num2) == 1:
        decrement = list(reversed(num2.value))
        subtraction = list(reversed(num1.value))
        difference_index = (len(num2) - (len(num2) - len(num1))) - 1

    # Если числа равны, возвращаем 0 как объект класса.
    else:
        return NaturalNumber("0")

    # Далее запускается поразрядное вычитание
    for i in range(len(subtraction)):
        decrement[i] = decrement[i] - subtraction[i]

        # Если значение разряда меньше нуля, то к разряду прибавляется 10, а из следующего разряда вычитается 1.
        if decrement[i] < 0:
            decrement[i] += 10
            decrement[i + 1] -= 1

    # С позиции differene_index запускается проверка остальных разрядов.
    if difference_index != (len(subtraction)):
        for i in range(difference_index, len(decrement) - 1):
            if decrement[i] < 0:
                decrement[i] += 10
                decrement[i + 1] -= 1

    # Если после выполнения поразрядного вычитания первый разряд становится незначащим - он удаляется.
    if decrement[-1] == 0:
        decrement.pop()

    # Возвращаем результат как объект NaturalNumber.
    result = ''.join(list(map(str, list(reversed(decrement)))))
    return NaturalNumber(result)


def MUL_ND_N():
    pass


def MUL_Nk_N():
    pass


def MUL_NN_N():
    pass


def SUB_NDN_N():
    pass


def DIV_NN_Dk(n_num_1: NaturalNumber, n_num_2: NaturalNumber):
    """Вычисление первой цифры от деления большего натурального на меньшее"""
    if isinstance(n_num_1, NaturalNumber) and isinstance(n_num_2, NaturalNumber):
        if n_num_1.__str__() == "0" and n_num_2.__str__() == "0":
            return ValueError("Деление на 0 недопустимо")
        if n_num_1.__str__() == "0" or n_num_2.__str__() == "0":
            return NaturalNumber("0")

        # Сравниваем числа
        comp_1 = COM_NN_D(n_num_1, n_num_2)
        # Если числа равны, возвращаем первую цифру как 1
        if comp_1 == 0:
            return NaturalNumber("1")

        # Если первое число меньше, меняем местами
        if comp_1 == 1:
            n_num_1, n_num_2 = n_num_2, n_num_1

        k = SUB_NN_N(NaturalNumber(str(n_num_1.__len__())), NaturalNumber(str(n_num_2.__len__())))
        comp_2 = COM_NN_D(n_num_1, MUL_Nk_N(n_num_2, k))

        if COM_NN_D(comp_2, NaturalNumber("1")) == 0:
            while COM_NN_D(n_num_1, MUL_Nk_N(n_num_2, k)) != 2:
                k = SUB_NN_N(k, NaturalNumber("1"))
        comp_2 = COM_NN_D(n_num_1, MUL_Nk_N(n_num_2, k))

        return find_denominator(n_num_1, n_num_2, k)

    else:
        raise ValueError("На вход должны подаваться натуральные числа")



def DIV_NN_N():
    pass


def MOD_NN_N(num_1: NaturalNumber, num_2: NaturalNumber):  # N-12	Остаток от деления первого натурального числа на второе натуральное (делитель!=0)
    if int(num_2) == 0:
        raise ValueError("Делитель не может быть равен нулю.")  # хз, надо или не надо?

    # Получение неполного частного
    quotient = DIV_NN_N(num_1, num_2)

    # Вычисление остатка
    remainder = SUB_NDN_N(num_1, num_2, quotient)  # Остаток = a - b * (неполное частное)

    return remainder

def GCF_NN_N():
    pass

def LCM_NN_N():
    pass


# Модуль выполнен: Борисов Е.А., гр. 3382.
# Модуль целого числа
def ABS_Z_N(num: IntegerNumber) -> NaturalNumber:
    result = IntegerNumber(str(num))
    # Меняем знак на плюс.
    result.sign = 0

    # Возвращаем результат как объект NaturalNumber.
    return NaturalNumber(str(result))


def POZ_Z_D(num: IntegerNumber):  # Z-2	Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    if int(num) > 0:
        return 2
    elif int(num) < 0:
        return 1
    elif int(num) == 0:
        return 0


def MUL_ZM_Z(num: IntegerNumber):  # Z-3	Умножение целого на (-1)
    if(int(num) == 0):
        return num
    else:
        if num.sign == 1:
            num.sign = 0
        else:
            num.sign = 1
        return num

def TRANS_N_Z(natural_num: NaturalNumber):
    """Преобразование натурального числа в целое"""
    if type(natural_num) == NaturalNumber: # Проверка типа поданных данных
        int_num = IntegerNumber(natural_num.__str__())
        return int_num
    else:
        raise ValueError("На вход должно подаваться натуральное число.")


def TRANS_Z_N(integer_num: IntegerNumber):
    """Преобразование целого числа в натуральное"""
    if type(integer_num) == IntegerNumber: # Проверка типа поданных данных
        if integer_num.get_sign()==0: # Проверка знака числа
            natural_num = NaturalNumber(integer_num.__str__())
            return natural_num
        else:
            raise ValueError("Число должно быть неотрицательным")
    else:
        raise ValueError("На вход должно подаваться целое неотрицательное число.")


# Модуль выполнен: Борисов Е.А., гр. 3382.
# Сложение целых чисел.
def ADD_ZZ_Z(num1: IntegerNumber, num2: IntegerNumber) -> IntegerNumber:
    # Определение знаков подаваемых чисел.
    num1_poz = POZ_Z_D(num1)
    num2_poz = POZ_Z_D(num2)

    # Вычисление модулей подаваемых чисел.
    abs1 = ABS_Z_N(num1)
    abs2 = ABS_Z_N(num2)

    # Если подаваемые числа положительные или 0.
    if (num1_poz == "2" or num1_poz == "0") and (num2_poz == "2" or num2_poz == "0"):
        result = IntegerNumber(str(ADD_NN_N(abs1, abs2)))
        return result

    # Если подаваемые числа отрицательные или 0.
    elif (num1_poz == "1" or num1_poz == "0") and (num2_poz == "1" or num2_poz == "0"):
        add_result_as_integer = IntegerNumber(str(ADD_NN_N(abs1, abs2)))
        result = MUL_ZM_Z(add_result_as_integer)
        return result

    # Если первое отрицательное и второе положительное.
    elif (num1_poz == "1" and num2_poz == "2"):

        # Если модуль первого больше второго.
        if COM_NN_D(abs1, abs2) == 2:
            sub_result_as_integer = IntegerNumber(str(SUB_NN_N(abs1, abs2)))
            result = MUL_ZM_Z(sub_result_as_integer)
            return result

        # Если модуль второго больше первого.
        elif COM_NN_D(abs1, abs2) == 1:
            result = IntegerNumber(str(SUB_NN_N(abs1, abs2)))
            return result

        # Если равны.
        else:
            return IntegerNumber("0")

    # Если первое положительное и второе отрицательное
    elif (num1_poz == "2" and num2_poz == "1"):

        # Если модуль второго больше первого.
        if COM_NN_D(abs1, abs2) == 1:
            sub_result_as_integer = IntegerNumber(str(SUB_NN_N(abs1, abs2)))
            result = MUL_ZM_Z(sub_result_as_integer)
            return result

        # Если модуль первого больше второго.
        elif COM_NN_D(abs1, abs2) == 2:
            result = IntegerNumber(str(SUB_NN_N(abs1, abs2)))
            return result

        # Если равны.
        else:
            return IntegerNumber("0")

# Модуль выполнен: Борисов Е.А., гр. 3382.
# Вычитание целых чисел
def SUB_ZZ_Z(num1: IntegerNumber, num2: IntegerNumber) -> IntegerNumber:
    # Определение знаков подаваемых чисел.
    num1_poz = POZ_Z_D(num1)
    num2_poz = POZ_Z_D(num2)

    # Вычисление модулей подаваемых чисел.
    abs1 = ABS_Z_N(num1)
    abs2 = ABS_Z_N(num2)

    # Если первое положительное и второе отрицательное или 0.
    if (num1_poz == "2") and (num2_poz == "0" or num2_poz == "1"):
        result = IntegerNumber(str(ADD_NN_N(abs1, abs2)))
        return result

    # Если первое отрицательное и второе положительное или 0.
    elif (num1_poz == "1") and (num2_poz == "0" or num2_poz == "2"):
        add_result_as_integer = IntegerNumber(str(ADD_NN_N(abs1, abs2)))
        result = MUL_ZM_Z(add_result_as_integer)
        return result

    # Если первое 0.
    elif num1_poz == "0":
        result = MUL_ZM_Z(num2)
        return result

    # Если оба положительные.
    elif (num1_poz == "2" and num2_poz == "2"):

        # Если модуль первого меньше второго.
        if COM_NN_D(abs1, abs2) == 1:
            sub_result_as_integer = IntegerNumber(str(SUB_NN_N(abs1, abs2)))
            result = MUL_ZM_Z(sub_result_as_integer)
            return result

        # Иначе.
        else:
            result = IntegerNumber(str(SUB_NN_N(abs1, abs2)))
            return result

    # Если оба отрицательные.
    elif (num1_poz == "1" and num2_poz == "1"):

        # Если модуль первого больше второго.
        if COM_NN_D(abs1, abs2) == 2:
            sub_result_as_integer = IntegerNumber(str(SUB_NN_N(abs1, abs2)))
            result = MUL_ZM_Z(sub_result_as_integer)
            return result

        # Иначе.
        else:
            result = IntegerNumber(str(SUB_NN_N(abs1, abs2)))
            return result


# Модуль выполнен: Борисов Е.А., гр. 3382.
# Умножение целых чисел.
def MUL_ZZ_Z(num1: IntegerNumber, num2: IntegerNumber) -> IntegerNumber:
    # Определение знаков подаваемых чисел.
    num1_poz = POZ_Z_D(num1)
    num2_poz = POZ_Z_D(num2)

    # Вычисление модулей подаваемых чисел.
    abs1 = ABS_Z_N(num1)
    abs2 = ABS_Z_N(num2)

    # Если введённые числа различны по знаку - результат отрицательный.
    if (num1_poz == "2" and num2_poz == "1") or (num1_poz == "1" and num2_poz == "2"):
        mul_result_as_integer = IntegerNumber(str(MUL_NN_N(abs1, abs2)))
        result = MUL_ZM_Z(mul_result_as_integer)
        return result

    # Иначе - положительнный
    else:
        return IntegerNumber(str(MUL_NN_N(abs1, abs2)))


def DIV_ZZ_Z(num1: IntegerNumber, num2: IntegerNumber):  # Z-9	Частное от деления целого на целое (делитель отличен от нуля)
    if int(num2) == 0:
        raise ValueError("Делитель не может быть равен нулю.")

    # знаки a и b
    sign_a = POZ_Z_D(num1)
    sign_b = POZ_Z_D(num2)

    # абсолютные значения
    abs_a = ABS_Z_N(num1)
    abs_b = ABS_Z_N(num2)

    # неполное частное от абсолютных значений
    quotient = DIV_NN_N(abs_a, abs_b)

    # знак результата
    if (sign_a == 2 and sign_b == 2) or (sign_a == 1 and sign_b == 1):
        return IntegerNumber(str(quotient))  # Положительное частное
    else:
        quotient = IntegerNumber(str(quotient))
        quotient = MUL_ZM_Z(quotient)
        return quotient  # Отрицательное частное


def MOD_ZZ_Z(num1: IntegerNumber, num2: IntegerNumber):  # Z-10	Остаток от деления целого на целое(делитель отличен от нуля)
    if int(num2) == 0:
        raise ValueError("Делитель не может быть равен нулю.")  # хз, надо или не надо?

    # частное от деления
    quotient = DIV_ZZ_Z(num1, num2)

    # остаток
    remainder = SUB_ZZ_Z(num1, MUL_ZZ_Z(num2, quotient))  # Остаток = a - b * (частное)

    return remainder


def RED_Q_Q(rational_number: RationalNumber) -> RationalNumber:
    if (rational_number.denominator == 1):
        return rational_number

    temp = RationalNumber(rational_number.numerator, rational_number.denominator)
    nod = euclidean_algorithm(int(rational_number.numerator), int(rational_number.denominator))[3]
    temp.numerator = IntegerNumber(str(int(rational_number.numerator) // nod))
    temp.denominator = NaturalNumber(str(int(rational_number.denominator) // nod))

    return temp


def INT_Q_B():
    pass


def TRANS_Z_Q(integer_number: IntegerNumber) -> RationalNumber:
    return RationalNumber(str(integer_number))


def TRANS_Q_Z():
    pass


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


def SUB_QQ_Q():
    pass


def MUL_QQ_Q(r_number_1: RationalNumber, r_number_2: RationalNumber):
    """Умножение рациональных чисел"""
    if type(r_number_1) == RationalNumber and type(r_number_2) == RationalNumber:
        numerator = MUL_ZZ_Z(r_number_1.numerator, r_number_2.numerator)
        denominator = MUL_NN_N(r_number_1.denominator, r_number_2.denominator)
        r_number = RationalNumber(IntegerNumber(str(numerator)), NaturalNumber(str(denominator)))
        return r_number
    else:
        raise ValueError("На вход должны подаваться рациональные числа")


def DIV_QQ_Q(rational_number1: RationalNumber, rational_number2: RationalNumber) -> RationalNumber:
    temp1 = RationalNumber(rational_number1.numerator, rational_number1.denominator)
    temp2 = RationalNumber(rational_number2.numerator, rational_number2.denominator)
    if (temp2.numerator.get_sign() == 1):
        temp2.numerator = IntegerNumber(str(int(temp2.numerator) * (-1)))
        temp1.numerator = IntegerNumber(str(int(temp1.numerator) * (-1)))

    if temp2.numerator != '0':
        temp1.numerator = IntegerNumber(str(int(temp1.numerator) * int(temp2.denominator)))
        temp1.denominator = NaturalNumber(str(int(temp1.denominator) * int(temp2.numerator)))
    else:
        raise ValueError("Знаменатель не может быть нулём")

    return temp1


def ADD_PP_P():
    pass


def SUB_PP_P(pln1: Polynomial, pln2: Polynomial) -> Polynomial:
    arr2 = pln2.getDegrees()
    temp = makePolynomial(str(pln1))

    for i in arr2:
        val = DIV_QQ_Q(pln2.getCoeff(NaturalNumber(str(i))), RationalNumber(IntegerNumber("-1")))
        temp.add(i, val)

    return temp


def MUL_PQ_P(polynomial: Polynomial, rational: RationalNumber):
    """Умножение многочлена на рациональное число"""
    if not (isinstance(polynomial, Polynomial) and isinstance(rational, RationalNumber)):
        return ValueError("Должны подаваться многочлен и рациональное число")

    result = Polynomial()
    temp = polynomial.head
    while temp is not None:
        # Умножаем коэффициент каждого члена многочлена на рациональное число
        numerator_multiplied = MUL_ZZ_Z(temp.val.numerator, rational.numerator)
        denominator_multiplied = MUL_NN_N(temp.val.denominator, rational.denominator)
        result.add(temp.deg, RationalNumber(numerator_multiplied, denominator_multiplied))
        temp = temp.next
    return result


def MUL_Pxk_P(pln: Polynomial, k: NaturalNumber) -> Polynomial:
    temp = makePolynomial(str(pln))
    for i in temp.getDegrees():
        temp.changeDegree(i, NaturalNumber(str(int(i) + int(k))))

    return temp


def LED_P_Q():
    pass

# Модуль выполнен: Борисов Е.А., гр. 3382.
# Степень многочлена.
def DEG_P_N(polynom: Polynomial) -> int:
    # Вызываем метод, возвращающий массив степеней, и выводим максимальную степень.
    deg = polynom.getDegrees()[0]
    return deg

def FAC_P_Q():
    pass


def MUL_PP_P(pln1: Polynomial, pln2: Polynomial) -> Polynomial:
    arr1 = pln1.getDegrees()
    arr2 = pln2.getDegrees()
    pln = Polynomial()

    for i in arr2:
        for j in arr1:
            val = MUL_QQ_Q(pln2.getCoeff(NaturalNumber(str(i))), pln1.getCoeff(NaturalNumber(str(j))))
            pln.add(NaturalNumber(str(int(j) + int(i))), val)

    return pln


def DIV_PP_P(input_pln1: Polynomial, input_pln2: Polynomial) -> Polynomial:
    pln1 = makePolynomial(str(input_pln1))
    pln2 = makePolynomial(str(input_pln2))
    break_deg = pln2.getDegrees()[0]
    pln = Polynomial()
    while (pln1.getDegrees()[0] >= break_deg):
        val = DIV_QQ_Q(pln1.getCoeff(NaturalNumber(str(pln1.getDegrees()[0]))),
                       pln2.getCoeff(NaturalNumber(str(pln2.getDegrees()[0]))))
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
    while (pln1.getDegrees()[0] >= break_deg):
        val = DIV_QQ_Q(pln1.getCoeff(NaturalNumber(str(pln1.getDegrees()[0]))),
                       pln2.getCoeff(NaturalNumber(str(pln2.getDegrees()[0]))))
        deg = int(pln1.getDegrees()[0]) - int(pln2.getDegrees()[0])

        temp = Polynomial()
        temp.makePolynomial(f"{val}x^{deg}")
        temp = MUL_PP_P(pln2, temp)

        pln1 = SUB_PP_P(pln1, temp)

        pln.add(deg, val)
    return pln1


def GCF_PP_P():
    pass


def DER_P_P():
    pass


def NMR_P_P(pln: Polynomial) -> str:
    def check_root(pln, val):
        temp = Polynomial()
        temp.makePolynomial(f"x - {val}")
        if (MOD_PP_P(pln, temp) == 0):
            return True
        return False

    pass


# Словарь для маппинга номеров на функции
functions_dict = {
    "1": COM_NN_D,
    "2": NZER_N_B,
    "3": ADD_1N_N,
    "4": ADD_NN_N,
    "5": SUB_NN_N,
    "6": MUL_ND_N,
    "7": MUL_Nk_N,
    "8": MUL_NN_N,
    "9": SUB_NDN_N,
    "10": DIV_NN_Dk,
    "11": DIV_NN_N,
    "12": MOD_NN_N,
    "13": GCF_NN_N,
    "14": LCM_NN_N,
    "15": ABS_Z_N,
    "16": POZ_Z_D,
    "17": MUL_ZM_Z,
    "18": TRANS_N_Z,
    "19": TRANS_Z_N,
    "20": ADD_ZZ_Z,
    "21": SUB_ZZ_Z,
    "22": MUL_ZZ_Z,
    "23": DIV_ZZ_Z,
    "24": MOD_ZZ_Z,
    "25": RED_Q_Q,
    "26": INT_Q_B,
    "27": TRANS_Z_Q,
    "28": TRANS_Q_Z,
    "29": ADD_QQ_Q,
    "30": SUB_QQ_Q,
    "31": MUL_QQ_Q,
    "32": DIV_QQ_Q,
    "33": ADD_PP_P,
    "34": SUB_PP_P,
    "35": MUL_PQ_P,
    "36": MUL_Pxk_P,
    "37": LED_P_Q,
    "38": DEG_P_N,
    "39": FAC_P_Q,
    "40": MUL_PP_P,
    "41": DIV_PP_P,
    "42": MOD_PP_P,
    "43": GCF_PP_P,
    "44": DER_P_P,
    "45": NMR_P_P
}