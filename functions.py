from classes import NaturalNumber, IntegerNumber, RationalNumber, Polynomial

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

# Модуль выполнен: Самойлова Е.М., гр. 3382.
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

# Модуль выполнен: Самойлова Е.М., гр. 3382.
# Преобразование сокращенного дробного в целое (если знаменатель равен 1)
def TRANS_Q_Z(r_number: RationalNumber) -> IntegerNumber:

    # Проверяем, равен ли знаменатель 1, если не равен возвращаем ошибку
    if r_number.denominator.__str__() != "1":
        raise ValueError ("Дробь не может быть преобразована в целое число, знаменатель не равен 1")
    # Преобразуем числитель в целое число
    result = IntegerNumber(str(r_number.numerator))
    return result  # Возвращаем целое число

# Модуль выполнен: Самойлова Е.М., гр. 3382.
# Старший коэффициент многочлена
def LED_P_Q(polynom: Polynomial) -> RationalNumber:
    # Вызываем метод, возвращающий массив степеней, и выводим максимальную степень.
    deg = polynom.getDegrees()[0]
    # Получаем коэффициент, соответствующий старшей степени.
    result = polynom.getCoeff(NaturalNumber(str(deg)))
    return result

