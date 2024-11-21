from classes import NaturalNumber, RationalNumber, IntegerNumber, Polynomial

# Функция для умножения натурального числа на одну цифру (от 0 до 9).
def MUL_ND_N(num: NaturalNumber, digit: NaturalNumber) -> NaturalNumber:
    if not (0 <= int(digit) <= 9):  # Проверяем, что digit является цифрой
        raise ValueError('The number must be from 0 to 9') 
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
 
# Умножение натурального числа на 10^k, k-натуральное
def MUL_Nk_N(num: NaturalNumber, degree: NaturalNumber) -> NaturalNumber:

    result = str(num) + '0' * int(degree)  # Добавляем k-нулей к числу
    return NaturalNumber(result)  
        
# Умножение натуральных чисел
def MUL_NN_N(num1: NaturalNumber, num2: NaturalNumber) -> NaturalNumber:
    total_result = NaturalNumber('0')  # Начальное значение результата

    for i, digit in enumerate(reversed(num1.get_value())):
        # Умножаем num2 на текущую цифру num1
        partial_product = MUL_ND_N(num2, NaturalNumber(str(digit)))
        # Сдвигаем частичный результат на i позиций влево (добавляем нули)
        shifted_partial_product = MUL_Nk_N(partial_product, NaturalNumber(str(i)))
        # Добавляем сдвинутый частичный результат к общему результату
        total_result = ADD_NN_N(total_result, shifted_partial_product)

    return total_result

""""
Вычитание из натурального другого натурального, 
умноженного на цифру для случая с неотрицательным результатом

"""
def SUB_NDN_N(num1: NaturalNumber, multiplier: NaturalNumber, num2: NaturalNumber) -> NaturalNumber:
    # Обращаемся к функциям умножения натурального числа на цифру и разности двух натуральных чисел
    result = SUB_NN_N(num1, MUL_ND_N(num2, multiplier))
    return result

# Метод для проверки, является ли рациональное число целым
def INT_Q_B(r_number: RationalNumber) -> bool:
    
    # Преобразуем числитель в строку и проверяем делимость на знаменатель
    num_value = int(r_number.numerator)
    denom_value = int(r_number.denominator)
        
    if num_value % denom_value == 0:
        return True  
    else:
        return False 
    
# Преобразование сокращенного дробного в целое (если знаменатель равен 1)
def TRANS_Q_Z(r_number: RationalNumber) -> IntegerNumber:
    
    # Проверяем, равен ли знаменатель 1
    if r_number.denominator.__str__() != "1":
        raise ValueError ("The fraction cannot be converted to an integer because the denominator is not equal to 1.")
    # Преобразуем числитель в целое число
    result = IntegerNumber(str(r_number.numerator))
    return result  # Возвращаем целое число
        

# Функция для получения старшего коэффициента
def LED_P_Q(polynom: Polynomial) -> RationalNumber:

    deg = polynom.getDegrees()[0]
    result = polynom.getCoeff(NaturalNumber(str(deg)))
    return result





