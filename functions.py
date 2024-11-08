from classes import NaturalNumber, IntegerNumber, RationalNumber, Polynomial, makePolynomial
from technical_functions import euclidean_algorithm


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


def NZER_N_B(num):  # N-1  Проверка на ноль: если число не равно нулю, то «да» иначе «нет»
    if int(num) == 0:
        return "Число является 0"
    else:
        return "Число не является 0"


def ADD_1N_N():
    pass


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


def DIV_NN_Dk():
    pass


def DIV_NN_N():
    pass


def MOD_NN_N():
    pass


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


def POZ_Z_D():
    pass


def MUL_ZM_Z():
    pass


def TRANS_N_Z():
    pass


def TRANS_Z_N():
    pass


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


def DIV_ZZ_Z():
    pass


def MOD_ZZ_Z():
    pass


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


def MUL_PQ_P():
    pass


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
    "0": COM_NN_D,
    "1": NZER_N_B,
    "2": ADD_1N_N,
    "3": ADD_NN_N,
    "4": SUB_NN_N,
    "5": MUL_ND_N,
    "6": MUL_Nk_N,
    "7": MUL_NN_N,
    "8": SUB_NDN_N,
    "9": DIV_NN_Dk,
    "10": DIV_NN_N,
    "11": MOD_NN_N,
    "12": GCF_NN_N,
    "13": LCM_NN_N,
    "14": ABS_Z_N,
    "15": POZ_Z_D,
    "16": MUL_ZM_Z,
    "17": TRANS_N_Z,
    "18": TRANS_Z_N,
    "19": ADD_ZZ_Z,
    "20": SUB_ZZ_Z,
    "21": MUL_ZZ_Z,
    "22": DIV_ZZ_Z,
    "23": MOD_ZZ_Z,
    "24": RED_Q_Q,
    "25": INT_Q_B,
    "26": TRANS_Z_Q,
    "27": TRANS_Q_Z,
    "28": ADD_QQ_Q,
    "29": SUB_QQ_Q,
    "30": MUL_QQ_Q,
    "31": DIV_QQ_Q,
    "32": ADD_PP_P,
    "33": SUB_PP_P,
    "34": MUL_PQ_P,
    "35": MUL_Pxk_P,
    "36": LED_P_Q,
    "37": DEG_P_N,
    "38": FAC_P_Q,
    "39": MUL_PP_P,
    "40": DIV_PP_P,
    "41": MOD_PP_P,
    "42": GCF_PP_P,
    "43": DER_P_P,
    "44": NMR_P_P
}