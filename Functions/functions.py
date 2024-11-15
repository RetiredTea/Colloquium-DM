from classes import *
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

#  Модуль выполнен: Мельник А., гр. 3382.
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

# Модуль выполнен: Самойлова Е.М., гр. 3382.
# Умножение натурального числа на цифру
def MUL_ND_N(num: NaturalNumber, digit: NaturalNumber) -> NaturalNumber:
    carry = 0  # Перенос для сложения
    result = []  # Список для хранения результата

    # Преобразуем строку в целые числа и выполняем умножение
    for i in reversed(num.get_value()):  # Проходим по цифрам в обратном порядке
        product = i * int(digit) + carry  # Умножаем и добавляем перенос
        result.append(product % 10)  # Сохраняем младшую цифру результата
        carry = product // 10  # Обновляем перенос

    # Если остался перенос, добавляем его в результат
    while carry > 0:
        result.append(carry % 10)  # Сохраняем оставшиеся цифры переноса
        carry //= 10

    result.reverse()  # Переворачиваем результат для правильного порядка цифр
    return NaturalNumber(''.join(map(str, result)))

# Модуль выполнен: Самойлова Е.М., гр. 3382.
# Умножение натурального числа на 10^k, k-натуральное
def MUL_Nk_N(num: NaturalNumber, degree: NaturalNumber) -> NaturalNumber:

    result = str(num) + '0' * int(degree)  # Добавляем k-нулей к числу
    return NaturalNumber(result)


# Модуль выполнен: Самойлова Е.М., гр. 3382.
#Умножение натуральных чисел
def MUL_NN_N(num1: NaturalNumber, num2: NaturalNumber) -> NaturalNumber:
    total_result = NaturalNumber('0')  # Начальное значение результата
    # Перебираем цифры первого числа num1 справа налево
    for i, digit in enumerate(reversed(num1.get_value())):
        # Умножаем num2 на текущую цифру num1
        partial_product = MUL_ND_N(num2, NaturalNumber(str(digit)))
        # Сдвигаем промежуточный результат partial_product на i позиций влево (добавляем нули)
        shifted_partial_product = MUL_Nk_N(partial_product, NaturalNumber(str(i)))
        # Добавляем сдвинутый частичный результат к общему результату
        total_result = ADD_NN_N(total_result, shifted_partial_product)

    return total_result

# Модуль выполнен: Самойлова Е.М., гр. 3382.
""""
Вычитание из натурального другого натурального, 
умноженного на цифру для случая с неотрицательным результатом
"""
def SUB_NDN_N(num1: NaturalNumber, multiplier: NaturalNumber, num2: NaturalNumber) -> NaturalNumber:
    # Обращаемся к функциям умножения натурального числа на цифру и разности двух натуральных чисел
    result = SUB_NN_N(num1, MUL_NN_N(num2, multiplier))
    return result

# Модуль выполнен: Андреев М.В., гр. 3382.
# Вычисление первой цифры частного при делении большего натурального числа на меньшее, домноженное на 10^k,
# где k - номер позиции этой цифры (номер считается с нуля)
def DIV_NN_Dk(num1: NaturalNumber, num2: NaturalNumber) -> ValueError | NaturalNumber:
    # Проверка, что делитель num2 не равен 0
    if num2.__str__() == "0":
        return ValueError("Нельзя делить на 0")  # Генерация ошибки, если деление на 0

    # Если числа равны (num1 == num2), результат деления — единица
    if COM_NN_D(num1, num2) == 0:
        return NaturalNumber("1")

    # Определяем большее и меньшее число
    big = num1 if COM_NN_D(num1, num2) == 2 else num2  # Присваиваем big значение большего из num1 и num2
    small = num2 if COM_NN_D(num1, num2) == 2 else num1  # Присваиваем small значение меньшего

    # Вычисляем начальное значение позиции k
    k = big.__len__() - small.__len__()
    digits_of_smaller = small.__len__()

    # Извлекаем старшие разряды числа big для сравнения с числом small
    necessary_big = NaturalNumber(big.__str__()[:digits_of_smaller])  # Извлекаем первые разряды, соответствующие длине small
    if COM_NN_D(necessary_big, small) == 1:  # Если выделенная часть necessary_big меньше small
        necessary_big = NaturalNumber(big.__str__()[:digits_of_smaller + 1])  # Увеличиваем длину на 1 разряд
        k -= 1  # Снижаем k, так как увеличили количество цифр в necessary_big

    # Ищем множитель для small, чтобы достичь максимального возможного значения, не превышающего necessary_big
    multiplier = 1
    small_multiplied = small
    while COM_NN_D(small_multiplied, necessary_big) != 2:  # Пока small_multiplied <= necessary_big
        multiplier += 1
        small_multiplied = ADD_NN_N(small_multiplied, small)  # Увеличиваем small_multiplied на small

    # Возвращаем результат, умноженный на 10^k (положение разряда)
    result = NaturalNumber(str(multiplier - 1))  # Находим окончательное значение, уменьшая multiplier на 1
    return MUL_Nk_N(result, k)  # Домножаем на 10^k для корректного расположения разряда


# Модуль выполнен: Андреев М.В., гр. 3382.
# Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
def DIV_NN_N(num1: NaturalNumber, num2: NaturalNumber) -> ValueError | NaturalNumber:
    "Неполное частное от деления натуральных чисел"
    # Проверка деления на ноль
    if num2.__str__() == "0":
        return ValueError("Нельзя делить на 0")  # Генерация ошибки, если делитель равен 0

    # Обработка случая, когда оба числа равны нулю
    if num1.__str__() == "0" and num2.__str__() == "0":
        return NaturalNumber("0")  # Результат 0, если оба числа нулевые

    # Если num1 меньше num2, результат частного будет 0
    if COM_NN_D(num1, num2) == 1:
        return NaturalNumber("0")

    # Инициализация результата
    result = NaturalNumber("0")

    # Цикл для нахождения частного
    while COM_NN_D(num1, num2) in [2, 0]:  # пока num1 >= num2
        quotient = DIV_NN_Dk(num1, num2)  # Вычисляем очередную цифру частного
        num1 = SUB_NN_N(num1, MUL_NN_N(num2, quotient))  # Вычитаем произведение частного на делитель из num1
        result = ADD_NN_N(result, quotient)  # Добавляем найденную цифру частного к результату

    return result

#  Модуль выполнен: Мельник А., гр. 3382.
def MOD_NN_N(num_1: NaturalNumber, num_2: NaturalNumber):  # N-12	Остаток от деления первого натурального числа на второе натуральное (делитель!=0)
    if int(num_2) == 0:
        raise ValueError("Делитель не может быть равен нулю.")

    # Получение неполного частного
    quotient = DIV_NN_N(num_1, num_2)

    # Вычисление остатка
    remainder = SUB_NDN_N(num_1, num_2, quotient)  # Остаток = a - b * (неполное частное)

    return remainder

# Модуль выполнен: Денис Ц., гр. 3382.
#===== НОД натуральных чисел ====
#===== принимает два числа возвращает одно - НОД (ввод/вывод объектами класса NaturalNumber) ====
def GCF_NN_N(num1: NaturalNumber, num2: NaturalNumber):
    def swap(a: NaturalNumber, b: NaturalNumber):
        if COM_NN_D(a,b) == 2:
            return a, b
        c = a
        a = b
        b = c
        return a, b
    while NZER_N_B(num1) == False and NZER_N_B(num2) == False:
        num1, num2 = swap(num1,num2)
        num1 = MOD_NN_N(num1,num2)
    if(int(num2) == 0 and int(num1) != 0):
        return num1
    elif(int(num2) == 0 and int(num1) == 0):
        return NaturalNumber("1")
    return num2

# Модуль выполнен: Царегородцев Д., гр. 3382.
#===== НОК натуральных чисел ====
#===== принимает два числа возвращает одно - НОК (ввод/вывод объектами класса NaturalNumber) ====
def LCM_NN_N(num1: NaturalNumber, num2: NaturalNumber):
    return DIV_NN_N(MUL_NN_N(num1,num2), GCF_NN_N(num1, num2))


# Модуль выполнен: Борисов Е.А., гр. 3382.
# Модуль целого числа
def ABS_Z_N(num: IntegerNumber) -> NaturalNumber:
    result = IntegerNumber(str(num))
    # Меняем знак на плюс.
    result.sign = 0

    # Возвращаем результат как объект NaturalNumber.
    return NaturalNumber(str(result))

#  Модуль выполнен: Мельник А., гр. 3382.
def POZ_Z_D(num: IntegerNumber):  # Z-2	Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    if int(num) > 0:
        return 2
    elif int(num) < 0:
        return 1
    elif int(num) == 0:
        return 0

#  Модуль выполнен: Мельник А., гр. 3382.
def MUL_ZM_Z(num: IntegerNumber):  # Z-3	Умножение целого на (-1)
    if(int(num) == 0):
        return num
    else:
        if num.sign == 1:
            num.sign = 0
        else:
            num.sign = 1
        return num

# Модуль выполнен: Андреев М.В., гр. 3382.
# Преобразование натурального в целое
def TRANS_N_Z(natural_num: NaturalNumber):
    """Преобразование натурального числа в целое"""
    if type(natural_num) == NaturalNumber: # Проверка типа поданных данных
        int_num = IntegerNumber(natural_num.__str__())
        return int_num
    else:
        raise ValueError("На вход должно подаваться натуральное число.")

# Модуль выполнен: Андреев М.В., гр. 3382.
# Преобразование целого неотрицательного в натуральное
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
    if (num1_poz == 2 or num1_poz == 0) and (num2_poz == 2 or num2_poz == 0):
        result = IntegerNumber(str(ADD_NN_N(abs1, abs2)))
        return result

    # Если подаваемые числа отрицательные или 0.
    elif (num1_poz == 1 or num1_poz == 0) and (num2_poz == 1 or num2_poz == 0):
        add_result_as_integer = IntegerNumber(str(ADD_NN_N(abs1, abs2)))
        result = MUL_ZM_Z(add_result_as_integer)
        return result

    # Если первое отрицательное и второе положительное.
    elif (num1_poz == 1 and num2_poz == 2):

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
    elif (num1_poz == 2 and num2_poz == 1):

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
    if (num1_poz == 2) and (num2_poz == 0 or num2_poz == 1):
        result = IntegerNumber(str(ADD_NN_N(abs1, abs2)))
        return result

    # Если первое отрицательное и второе положительное или 0.
    elif (num1_poz == 1) and (num2_poz == 0 or num2_poz == 2):
        add_result_as_integer = IntegerNumber(str(ADD_NN_N(abs1, abs2)))
        result = MUL_ZM_Z(add_result_as_integer)
        return result

    # Если первое 0.
    elif num1_poz == 0:
        result = MUL_ZM_Z(num2)
        return result

    # Если оба положительные.
    elif (num1_poz == 2 and num2_poz == 2):

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
    elif (num1_poz == 1 and num2_poz == 1):

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
    if (num1_poz == 2 and num2_poz == 1) or (num1_poz == 1 and num2_poz == 2):
        mul_result_as_integer = IntegerNumber(str(MUL_NN_N(abs1, abs2)))
        result = MUL_ZM_Z(mul_result_as_integer)
        return result

    # Иначе - положительнный
    else:
        return IntegerNumber(str(MUL_NN_N(abs1, abs2)))

#  Модуль выполнен: Мельник А., гр. 3382.
def DIV_ZZ_Z(num1: IntegerNumber, num2: IntegerNumber):  # Z-9	Частное от деления целого на целое (делитель отличен от нуля)
    if int(num2) == 0:
        raise ValueError("Делитель не может быть равен нулю.")
    if int(num1) == 0:  # если делимое = 0 вернуть 0
        return num1

    # знаки a и b
    sign_a = POZ_Z_D(num1)
    sign_b = POZ_Z_D(num2)

    # абсолютные значения
    abs_a = ABS_Z_N(num1)
    abs_b = ABS_Z_N(num2)

    # неполное частное от абсолютных значений
    quotient = DIV_NN_N(abs_a, abs_b)

    if sign_a == 2 and sign_b == 2:  # случай, когда оба числа положительны
        return IntegerNumber(str(quotient))
    if sign_a == 1 and sign_b == 1:  # случай, когда оба числа отрицательны
        quotient = IntegerNumber(str(ADD_1N_N(quotient)))
        return quotient
    else:
        if int(SUB_ZZ_Z(abs_a, MUL_ZZ_Z(abs_b, IntegerNumber(str(quotient))))) == 0:  # случай, когда остатка нет
            quotient = MUL_ZM_Z(IntegerNumber(str(quotient)))
            return quotient
        else:
            if sign_a == 1:  # случай, когда делимое отрицательно
                quotient = IntegerNumber(str(ADD_1N_N(quotient)))
                quotient = MUL_ZM_Z(IntegerNumber(str(quotient)))
                return quotient  # Отрицательное частное
            elif sign_b == 1:  # случай, когда делитель отрицателен
                quotient = MUL_ZM_Z(IntegerNumber(str(quotient)))
                return quotient  # Отрицательное частное


def MOD_ZZ_Z(num1: IntegerNumber, num2: IntegerNumber):  # Z-10	Остаток от деления целого на целое(делитель отличен от нуля)
    if int(num2) == 0:
        raise ValueError("Делитель не может быть равен нулю.")

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


#  Модуль выполнен: Самойлова Е.М., гр. 3382.
"""
 Проверка сокращенного дробного на целое, 
 если рациональное число является целым, то «да», иначе «нет»
"""
def INT_Q_B(r_number: RationalNumber) -> bool:

    # Преобразуем числитель в строку и проверяем делимость на знаменатель
    num_value = int(r_number.numerator)
    denom_value = int(r_number.denominator)

    if num_value % denom_value == 0:
        return True
    else:
        return False


def TRANS_Z_Q(integer_number: IntegerNumber) -> RationalNumber:
    return RationalNumber(str(integer_number))


# Преобразование сокращенного дробного в целое (если знаменатель равен 1)
def TRANS_Q_Z(r_number: RationalNumber) -> IntegerNumber:
    # Проверяем, равен ли знаменатель 1, если не равен возвращаем ошибку
    if r_number.denominator.__str__() != "1":
        raise ValueError ("Дробь не может быть преобразована в целое число, знаменатель не равен 1")
    # Преобразуем числитель в целое число
    result = IntegerNumber(str(r_number.numerator))
    return result  # Возвращаем целое число


# Модуль выполнен: Царегородцев Д., гр. 3382.
#===== Сложение дробей ====
#===== принимает две дроби возвращает их сумму(ввод/вывод рациональое число) ====
# Нужны функции сложения целых чисел, умножения целового на целое, преобразования натурального в целое
def ADD_QQ_Q (frac1: RationalNumber, frac2: RationalNumber):
    denominator = (LCM_NN_N(frac1.denominator,frac2.denominator))
    numerator = ADD_ZZ_Z(MUL_ZZ_Z(frac1.numerator, TRANS_N_Z((DIV_NN_N(denominator, frac1.denominator)))),\
                        MUL_ZZ_Z(frac2.numerator, TRANS_N_Z(DIV_NN_N(denominator, frac2.denominator))))
    frac_sum = RationalNumber(numerator, denominator)
    return(frac_sum)


# Модуль выполнен: Царегородцев Д., гр. 3382.
#===== Вычитание дробей ====
#===== принимает две дроби возвращает их разность(ввод/вывод строкой) ====
# нужны функции умножения целых чисел, вычетания целых чисел, преобразования натурального в целое
def SUB_QQ_Q(frac1: RationalNumber, frac2: RationalNumber):
    denominator = (LCM_NN_N(frac1.denominator, frac2.denominator))
    numerator = SUB_ZZ_Z(MUL_ZZ_Z(frac1.numerator, TRANS_N_Z((DIV_NN_N(denominator, frac1.denominator)))),\
                        MUL_ZZ_Z(frac2.numerator, TRANS_N_Z(DIV_NN_N(denominator, frac2.denominator))))
    frac_sum = RationalNumber(numerator, denominator)
    return(frac_sum)

# Модуль выполнен: Андреев М.В., гр. 3382.
# Умножение рациональных чисел
def MUL_QQ_Q(r_number_1: RationalNumber, r_number_2: RationalNumber):
    # Проверка типов аргументов
    if isinstance(r_number_1, RationalNumber) and isinstance(r_number_2, RationalNumber):
        # Умножаем числители и знаменатели рациональных чисел по отдельности
        numerator = MUL_ZZ_Z(r_number_1.numerator, r_number_2.numerator)
        denominator = MUL_NN_N(r_number_1.denominator, r_number_2.denominator)

        # Создаем новый рациональный результат
        r_number = RationalNumber(IntegerNumber(str(numerator)), NaturalNumber(str(denominator)))

        return r_number
    else:
        # Генерация ошибки, если типы аргументов не являются RationalNumber
        raise ValueError("На вход должны подаваться рациональные числа")

def DIV_QQ_Q(rational_number1: RationalNumber, rational_number2: RationalNumber) -> RationalNumber | ValueError:

    if rational_number2.numerator.value == [0]:
        return ValueError("Второй операнд не может быть 0.")

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

# Модуль выполнен: Царегородцев Д., гр. 3382.
#===== Сложение многочленов ====
def ADD_PP_P(polyn1: Polynomial, polyn2: Polynomial):
    result = Polynomial()  # Создаем новый многочлен для результата
    # Сначала добавляем все члены из первого многочлена
    temp = polyn1.head
    while temp is not None:
        result.add(temp.deg, temp.val)
        temp = temp.next
    # Затем добавляем все члены из второго многочлена
    temp = polyn2.head
    while temp is not None:
        result.add(temp.deg, temp.val)
        temp = temp.next
    return result

# Модуль выполнен: Царегородцев Д., гр. 3382.
#===== Вычитание многочленов ====
def SUB_PP_P(polyn1: Polynomial, polyn2: Polynomial):
    result = Polynomial()  # Создаем новый многочлен для результата
    # Сначала добавляем все члены из первого многочлена
    temp = polyn1.head
    while temp is not None:
        result.add(temp.deg, temp.val)
        temp = temp.next
    # Затем вычитаем все члены из второго многочлена
    temp = polyn2.head
    while temp is not None:
        temp.val.numerator = MUL_ZM_Z(temp.val.numerator)
        result.add(temp.deg, temp.val)
        temp = temp.next
    return result

# Модуль выполнен: Андреев М.В., гр. 3382.
# Умножение многочлена на рациональное число
def MUL_PQ_P(polynomial: Polynomial, rational: RationalNumber):
    """Умножение многочлена на рациональное число"""

    # Проверка, что переданы правильные типы: Polynomial и RationalNumber
    if not (isinstance(polynomial, Polynomial) and isinstance(rational, RationalNumber)):
        return ValueError("Должны подаваться многочлен и рациональное число")

    # Создаем пустой результат многочлена
    result = Polynomial()

    # Начинаем с первого члена многочлена
    temp = polynomial.head

    # Перебираем каждый элемент в списке членов многочлена
    while temp is not None:
        # Умножаем числитель коэффициента на числитель рационального числа
        numerator_multiplied = MUL_ZZ_Z(temp.val.numerator, rational.numerator)

        # Умножаем знаменатель коэффициента на знаменатель рационального числа
        denominator_multiplied = MUL_NN_N(temp.val.denominator, rational.denominator)

        # Добавляем новый член в многочлен результата с полученным коэффициентом
        result.add(temp.deg, RationalNumber(numerator_multiplied, denominator_multiplied))

        # Переходим к следующему члену многочлена
        temp = temp.next

    return result


# Модуль выполнен: Яковлев Д.С., гр. 3382.
# Умножение многочлена на x^k, k-натуральное или 0.
def MUL_Pxk_P(pln: Polynomial, k: NaturalNumber) -> Polynomial:
    temp = Polynomial() # Создаём результирующий многочлен
    for i in pln.getDegrees(): # Для каждой степени с коэффициентом отличным от нуля
        temp.add(NaturalNumber(str(i+int(k))), pln.getCoeff(NaturalNumber(str(i)))) # Добавляем к степени k (меняем на i+k) (добавляя к результирующему)
    return temp # Возвращаем копию переданного многочлена умноженную на x^k


# Модуль выполнен: Самойлова Е.М., гр. 3382.
# Старший коэффициент многочлена
def LED_P_Q(polynom: Polynomial) -> RationalNumber:
    # Вызываем метод, возвращающий массив степеней, и выводим максимальную степень.
    deg = polynom.getDegrees()[0]
    # Получаем коэффициент, соответствующий старшей степени.
    result = polynom.getCoeff(NaturalNumber(str(deg)))
    return result

# Модуль выполнен: Борисов Е.А., гр. 3382.
# Степень многочлена.
def DEG_P_N(polynom: Polynomial) -> NaturalNumber:
    # Вызываем метод, возвращающий массив степеней, и выводим максимальную степень.
    deg = NaturalNumber(str(polynom.getDegrees()[0]))
    return deg

def FAC_P_Q(polynomial: Polynomial) -> tuple[NaturalNumber, NaturalNumber]:
    """
    Функция находит НОД числителей и НОК знаменателей коэффициентов многочлена.
    Возвращает кортеж: (НОД числителей, НОК знаменателей).
    Аргументы:
    polynomial (Polynomial): Объект многочлена с коэффициентами, содержащими числители и знаменатели.
    Возвращает:
    tuple[NaturalNumber, NaturalNumber]: НОД числителей и НОК знаменателей.
    """
    # Списки для хранения числителей (для НОД) и знаменателей (для НОК) коэффициентов
    gcd_list = []
    lcm_list = []

    # Получаем степени многочлена и соответствующие коэффициенты
    pol_degs = polynomial.getDegrees()
    pol_coefs = [polynomial.getCoeff(NaturalNumber(str(deg))) for deg in pol_degs]
    if int(DEG_P_N(polynomial)) == 0 and int(pol_coefs[0].numerator) == 0:
        return 1 , 1

    # Извлекаем числители ненулевых коэффициентов для вычисления НОД
    for coeff in pol_coefs:
        numerator = coeff.numerator

        # Проверяем, что числитель не равен нулю
        if not NZER_N_B(numerator):

            # Проверяем, что числитель имеет тип NaturalNumber, иначе преобразуем
            if not isinstance(numerator, NaturalNumber):
                numerator = ABS_Z_N(numerator)  # Преобразование в натуральное число

            # Добавляем числитель в список для вычисления НОД
            gcd_list.append(numerator)

    # Извлекаем знаменатели всех коэффициентов для вычисления НОК
    for coeff in pol_coefs:
        denominator = coeff.denominator

        # Проверяем, что знаменатель имеет тип NaturalNumber, иначе преобразуем
        if not isinstance(denominator, NaturalNumber):
            denominator = TRANS_Z_N(denominator)  # Преобразование в натуральное число

        # Добавляем знаменатель в список для вычисления НОК
        lcm_list.append(denominator)

    # Инициализация НОД как первого числителя и поочередное нахождение НОД для всех остальных числителей
    gcd_result = gcd_list[0]
    for num in gcd_list[1:]:
        gcd_result = GCF_NN_N(gcd_result, num)  # Вычисляем НОД текущего результата с числителем num

    # Инициализация НОК как первого знаменателя и поочередное нахождение НОК для всех остальных знаменателей
    lcm_result = lcm_list[0]
    for den in lcm_list[1:]:
        lcm_result = LCM_NN_N(lcm_result, den)  # Вычисляем НОК текущего результата со знаменателем den

    # Возвращаем НОД числителей и НОК знаменателей в виде кортежа
    return int(gcd_result), int(lcm_result)


def MUL_PP_P(pln1: Polynomial, pln2: Polynomial) -> Polynomial:
    arr1 = pln1.getDegrees()
    arr2 = pln2.getDegrees()
    pln = Polynomial()

    for i in arr2:
        for j in arr1:
            val = MUL_QQ_Q(pln2.getCoeff(NaturalNumber(str(i))), pln1.getCoeff(NaturalNumber(str(j))))
            pln.add(NaturalNumber(str(int(j) + int(i))), val)

    return pln


# Модуль выполнен: Яковлев Д.С., гр. 3382.
# Частное от деления многочлена на многочлен при делении с остатком.
def DIV_PP_P(input_pln1: Polynomial, input_pln2: Polynomial) -> Polynomial:
    pln1 = makePolynomial(str(input_pln1))  # Создадим копию первого многочлена
    pln2 = makePolynomial(str(input_pln2))  # Создадим копию второго многочлена
    pln = Polynomial()  # Создадим многочлен частного
    break_deg = DEG_P_N(pln2)  # Запомним степень делителя
    if(str(pln2) == "0"): # Проверяем на нулевой многочлен
        raise ValueError("Делитель не может быть нулём.")
    while (COM_NN_D(DEG_P_N(pln1), break_deg) != 1):  # Пока степень первого многочлен не меньше степени второго
        if (int(DEG_P_N(pln1)) == 0 and int(pln1.getCoeff(DEG_P_N(pln1)).numerator) == 0 and int(break_deg) == 0):
            break
        temp = Polynomial()  # Одночлен, на который мы домножем второй многочлен для последующего деления в столбик

        val = DIV_QQ_Q(pln1.getCoeff(DEG_P_N(pln1)), pln2.getCoeff(DEG_P_N(pln2)))  # Коэффициент одночлена
        deg = SUB_NN_N(DEG_P_N(pln1), DEG_P_N(pln2))  # Степень одночлена
        temp.add(deg, val)  # Запишем одночлен

        temp = MUL_PP_P(pln2, temp)  # Домножем второй многочлен на одночлен
        pln1 = SUB_PP_P(pln1, temp)  # Вычтем из первого многочлена второй, домноженный на одночлен

        pln.add(deg, val)  # Добавляем одночлен на который было разделен первый многочлен к частному
    return pln  # Возвращаем частное


# Модуль выполнен: Яковлев Д.С., гр. 3382.
# Остаток от деления многочлена на многочлен при делении с остатком.
def MOD_PP_P(input_pln1: Polynomial, input_pln2: Polynomial) -> Polynomial:
    pln1 = makePolynomial(str(input_pln1))  # Создадим копию первого многочлена
    pln2 = makePolynomial(str(input_pln2))  # Создадим копию второго многочлена
    pln = Polynomial()  # Создадим многочлен частного
    break_deg = DEG_P_N(pln2)  # Запомним степень делителя
    if(str(pln2) == "0"): # Проверяем на нулевой многочлен
        raise ValueError("Делитель не может быть нулём.")
    while (COM_NN_D(DEG_P_N(pln1), break_deg) != 1):  # Пока степень первого многочлен не меньше степени второго
        if (int(DEG_P_N(pln1)) == 0 and int(pln1.getCoeff(DEG_P_N(pln1)).numerator) == 0 and int(break_deg) == 0):
            break
        temp = Polynomial()  # Одночлен, на который мы домножем второй многочлен для последующего деления в столбик
        val = DIV_QQ_Q(pln1.getCoeff(DEG_P_N(pln1)), pln2.getCoeff(DEG_P_N(pln2)))  # Коэффициент одночлена
        deg = SUB_NN_N(DEG_P_N(pln1), DEG_P_N(pln2))  # Степень одночлена
        temp.add(deg, val)  # Запишем одночлен

        temp = MUL_PP_P(pln2, temp)  # Домножем второй многочлен на одночлен
        pln1 = SUB_PP_P(pln1, temp)  # Вычтем из первого многочлена второй, домноженный на одночлен

        pln.add(deg, val)  # Добавляем одночлен на который было разделен первый многочлен к частному
    return pln1  # Возвращаем частное

# Модуль выполнен: Царегородцев Д., гр. 3382.
#===== НОД многочленов ====
#=====  ====
def GCF_PP_P(input_pln1: Polynomial, input_pln2: Polynomial):
    def swap(pln1, pln2):
        return pln2, pln1
    pln1 = makePolynomial(str(input_pln1))
    pln2 = makePolynomial(str(input_pln2))
    while(str(pln2) != "0"):
        pln1 = MOD_PP_P(pln1, pln2)
        pln1, pln2 = swap(pln1, pln2)
    if(int(pln1.getCoeff(DEG_P_N(pln1)).numerator) < 0):
        pln1 = MUL_PQ_P(pln1, RationalNumber("-1"))
    # Опционально: следующая строка приводит полином к красивым коэффициентам
    #pln1.setNiceCoeffs()
    return pln1

# Модуль выполнен: Царегородцев Д., гр. 3382.
#===== Производная многочлена ====
def DER_P_P(pln: Polynomial):
    polyn = makePolynomial(str(pln))
    temp = polyn.head
    while temp is not None:
        if str(temp.deg) != '1' and str(temp.deg) != '0':
            temp.val = MUL_QQ_Q(temp.val, TRANS_Z_Q(TRANS_N_Z(temp.deg)))
            temp.deg = SUB_NN_N(temp.deg, NaturalNumber('1'))
        elif str(temp.deg) == '1':
            temp.deg = '0'

        elif str(temp.deg) == '0':
            if (temp.prev != None):
                temp = temp.prev
                temp.next = None
            else:
                temp.val = RationalNumber("0")
            break
        temp = temp.next
    if(str(polyn) == "0"):
        polyn = makePolynomial("1")
    return polyn


# Модуль выполнен: Яковлев Д.С., гр. 3382.
# Преобразование многочлена — кратные корни в простые.
def NMR_P_P(pln: Polynomial) -> Polynomial:
    res = Polynomial() # Создадим результирующий многочлен
    der = DER_P_P(pln) # Запомним производную
    # Опционально можно добавить следующую строку если нам не важен общий коэффициент произвоной многочлена, который больше 1
    der.setNiceCoeffs() # Сократим производную на НОД всех коэффициентов (например 2x+2 ---> x+1)
    gcf = GCF_PP_P(pln, der) # Запомним НОД исходного многочлена и его производной
    res = DIV_PP_P(pln, gcf) # Запишем в результирующий многочлен частное от исходного на сохранённый НОД
    res.setNiceCoeffs() # Сокращаем получившийся многочлен на общую константу
    return res # Возвращаем исходный многочлен без кратных корней






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
