def NZER_N_B(num):  # N-1  Проверка на ноль: если число не равно нулю, то «да» иначе «нет»
    if int(num) == 0:
        return True
    else:
        return False


def ADD_1N_N(num):  # N-3	Добавление 1 к натуральному числу
    num = str(int(num) + 1)
    return num


def MOD_NN_N(num_1, num_2):  # N-12	Остаток от деления первого натурального числа на второе натуральное (делитель!=0)
    if int(num_2) == 0:
        raise ValueError("Делитель не может быть равен нулю.")  # хз, надо или не надо?

    # Получение неполного частного
    quotient = DIV_NN_N(num_1, num_2)

    # Вычисление остатка
    remainder = SUB_NDN_N(num_1, num_2, quotient)  # Остаток = a - b * (неполное частное)

    return remainder


def POZ_Z_D(num):  # Z-2	Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    if int(num) > 0:
        return str(2)
    elif int(num) < 0:
        return str(1)
    elif int(num) == 0:
        return str(0)


def MUL_ZM_Z(num):  # Z-3	Умножение целого на (-1)
    if num[0] == '-':
        num = num[1:]
        return num
    else:
        num = '-' + num
        return num


def DIV_ZZ_Z(num1, num2):  # Z-9	Частное от деления целого на целое (делитель отличен от нуля)
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
    if (sign_a == '2' and sign_b == '2') or (sign_a == '1' and sign_b == '1'):
        return quotient  # Положительное частное
    else:
        quotient = '-' + quotient
        return quotient  # Отрицательное частное


def MOD_ZZ_Z(num1, num2):  # Z-10	Остаток от деления целого на целое(делитель отличен от нуля)
    if int(num2) == 0:
        raise ValueError("Делитель не может быть равен нулю.")  # хз, надо или не надо?

    # частное от деления
    quotient = DIV_ZZ_Z(num1, num2)

    # остаток
    remainder = SUB_ZZ_Z(num1, MUL_ZZ_Z(num2, quotient))  # Остаток = a - b * (частное)

    return remainder
