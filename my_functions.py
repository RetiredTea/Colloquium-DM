from classes import *
from depend import MUL_ZZ_Z, MUL_Nk_N, MUL_NN_N,  ADD_1N_N, SUB_NN_N, COM_NN_D

def TRANS_N_Z(natural_num):
    """Преобразование натурального числа в целое"""
    if type(natural_num) == NaturalNumber: # Проверка типа поданных данных
        int_num = IntegerNumber(natural_num.__str__())
        return int_num
    else:
        raise ValueError("На вход должно подаваться натуральное число.")

def TRANS_Z_N(integer_num):
    """Преобразование целого числа в натуральное"""
    if type(integer_num) == IntegerNumber: # Проверка типа поданных данных
        if integer_num.get_sign()==0: # Проверка знака числа
            natural_num = NaturalNumber(integer_num.__str__())
            return natural_num
        else:
            raise ValueError("Число должно быть неотрицательным")
    else:
        raise ValueError("На вход должно подаваться целое неотрицательное число.")

def MUL_QQ_Q(r_number_1, r_number_2):
    """Умножение рациональных чисел"""
    if type(r_number_1) == RationalNumber and type(r_number_2) == RationalNumber:
        numerator = MUL_ZZ_Z(r_number_1.numerator, r_number_2.numerator) # Нахождение числителя
        denominator = MUL_NN_N(r_number_1.denominator, r_number_2.denominator) # Нахождение знаменателя
        r_number = RationalNumber(IntegerNumber(str(numerator)), NaturalNumber(str(denominator)))
        return r_number
    else:
        raise ValueError("На вход должны подаваться рациональные числа")


def find_denominator(n_num_1, n_num_2, k=NaturalNumber("0")): # Имитируем поиск первого числа от деления при делении в столбик
    """Определение первой цифры от деления большего натурального числа на меньшее"""
    result = NaturalNumber("0")
    temp_num = NaturalNumber(MUL_Nk_N(n_num_2, NaturalNumber(str(k))).__str__())  # n_num_2 * 10^k

    while COM_NN_D(n_num_1, MUL_NN_N(temp_num, NaturalNumber(str(result)))) in [NaturalNumber("2"), NaturalNumber('0')]: # Перебирем числа от 0 до 10
        result = ADD_1N_N(result) # Добавляем единицу

    return SUB_NN_N(result, NaturalNumber("1"))  # Возвращаем результат минус 1


def DIV_NN_Dk(n_num_1, n_num_2):
    """Вычисление первой цифры от деления большего натурального на меньшее"""
    if isinstance(n_num_1, NaturalNumber) and isinstance(n_num_2, NaturalNumber):
        if n_num_1.__str__() == "0" or n_num_2.__str__() == "0": # Если среди чисел 0, то возвращаем 0
            return NaturalNumber("0")

        # Сравниваем числа
        comp_1 = COM_NN_D(n_num_1, n_num_2)
        # Если числа равны, возвращаем первую цифру как 1
        if comp_1 == NaturalNumber("0"):
            return NaturalNumber("1")

        # Если первое число меньше, меняем местами
        if comp_1 == NaturalNumber("1"):
            n_num_1, n_num_2 = n_num_2, n_num_1

        k = SUB_NN_N(NaturalNumber(str(n_num_1.__len__())), NaturalNumber(str(n_num_2.__len__()))) # Находим разницу в числе разрядов чисел
        comp_2 = COM_NN_D(n_num_1, MUL_Nk_N(n_num_2, k)) # Сравниваем числа после умножения на 10^k

        if comp_2 == NaturalNumber("1"): # Находим подходящее для метода подбора k
            while COM_NN_D(n_num_1, MUL_Nk_N(n_num_2, k)) != NaturalNumber("2"):
                k = SUB_NN_N(k, NaturalNumber("1"))
        comp_2 = COM_NN_D(n_num_1, MUL_Nk_N(n_num_2, k))

        # Если n_num_1 больше и comp_2 тоже показывает, что результат больше
        if comp_2 == NaturalNumber("2"):
            return find_denominator(n_num_1, n_num_2, k)
        # Если n_num_1 больше, но comp_2 показывает, что результат меньше
        elif comp_1 == NaturalNumber("2") and comp_2 == NaturalNumber("1"):
            return find_denominator(n_num_1, n_num_2)
    else:
        raise ValueError("На вход должны подаваться натуральные числа")

def MUL_PQ_P(polynomial, rational):
    """Умножение многочлена на рациональное число"""
    result = Polynomial() # Создаем многочлен
    temp = polynomial.head
    while temp is not None:
        # Умножаем коэффициент каждого члена многочлена на рациональное число
        numerator_multiplied = MUL_ZZ_Z(temp.val.numerator, rational.numerator)
        denominator_multiplied = MUL_NN_N(temp.val.denominator, rational.denominator)
        result.add(temp.deg, RationalNumber(numerator_multiplied, denominator_multiplied))
        temp = temp.next
    return result





