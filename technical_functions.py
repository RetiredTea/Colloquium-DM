from classes import NaturalNumber, IntegerNumber, RationalNumber, Polynomial
from functions import *

#----------------------------------------------------------------------------------------------------------|
# ТЕХНИЧЕСКИЕ ФУНКЦИИ                                                                                      |
# В этот файл добавляются технические функции, которых нет в таблице, но они необходимы для работы модулей.|
#----------------------------------------------------------------------------------------------------------|

# Алгоритм Евклида
def euclidean_algorithm(a, b):
    # Функция меняющая между собой значения 2 переданных переменных
    def swap(a, b):
        return b, a

    # Коэффициенты алгоритма Евклида
    coeffs = []

    # Применяем алгоритм Евклида
    while (b != 0):
        coeffs.append(a // b)
        a = a % b
        a, b = swap(a, b)

    # Записываем результаты алгоритма Евклида
    NOD = a
    a1 = 1
    a2 = 0
    b1 = 0
    b2 = 1
    for i in coeffs:
        a1 -= i * b1
        a2 -= i * b2
        a1, b1 = swap(a1, b1)
        a2, b2 = swap(a2, b2)

    # Возвращаем результаты
    return coeffs, (a1, a2), (b1, b2), NOD

def find_denominator(n_num_1: NaturalNumber, n_num_2: NaturalNumber, k=NaturalNumber("0")):
    """Определение первой цифры от деления большего натурального числа на меньшее"""
    result = NaturalNumber("0")
    temp_num = NaturalNumber(MUL_Nk_N(n_num_2, NaturalNumber(str(k))).__str__())  # n_num_2 * 10^k

    while COM_NN_D(n_num_1, MUL_NN_N(temp_num, NaturalNumber(str(result)))) in [2,0]:
        result = ADD_1N_N(result)

    return SUB_NN_N(result, NaturalNumber("1"))  # Возвращаем результат минус 1