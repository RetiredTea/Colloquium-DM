from classes import NaturalNumber, IntegerNumber, Polynomial
from dependence import POZ_Z_D, MUL_ZM_Z, MUL_NN_N


# ЗАВИСИМОСТЬ ОТ МОДУЛЕЙ: POZ_Z_D, MUL_ZM_Z, MUL_NN_N!
# НЕ МЕРЖИТЬ!


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


# Модуль выполнен: Борисов Е.А., гр. 3382.
# Модуль целого числа
def ABS_Z_N(num: IntegerNumber) -> NaturalNumber:
    result = IntegerNumber(str(num))
    # Меняем знак на плюс.
    result.sign = 0

    # Возвращаем результат как объект NaturalNumber.
    return NaturalNumber(str(result))


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

    if (num1_poz == "2" and num2_poz == "2") or (num1_poz == "1" and num2_poz == "1"):
        result = IntegerNumber(str(MUL_NN_N(abs1, abs2)))
        return result

    elif (num1_poz == "2" and num2_poz == "1") or (num1_poz == "1" and num2_poz == "2"):
        mul_result_as_integer = IntegerNumber(str(MUL_NN_N(abs1, abs2)))
        result = MUL_ZM_Z(mul_result_as_integer)
        return result

    else:
        return IntegerNumber(str(MUL_NN_N(abs1, abs2)))


# Модуль выполнен: Борисов Е.А., гр. 3382.
# Степень многочлена.
def DEG_P_N(polynom: Polynomial) -> int:
    # Вызываем метод, возвращающий массив степеней, и выводим максимальную степень.
    deg = polynom.getDegrees()[0]
    return deg


'''
poly = Polynomial()
poly.makePolynomial("x^10000 + 1")
print(poly)'''
