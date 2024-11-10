from classes import *
from depend import MUL_ZZ_Z, MUL_Nk_N, MUL_NN_N , ADD_1N_N, SUB_NN_N, COM_NN_D

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

def MUL_QQ_Q(r_number_1: RationalNumber, r_number_2: RationalNumber):
    """Умножение рациональных чисел"""
    if type(r_number_1) == RationalNumber and type(r_number_2) == RationalNumber:
        numerator = MUL_ZZ_Z(r_number_1.numerator, r_number_2.numerator)
        denominator = MUL_NN_N(r_number_1.denominator, r_number_2.denominator)
        r_number = RationalNumber(IntegerNumber(str(numerator)), NaturalNumber(str(denominator)))
        return r_number
    else:
        raise ValueError("На вход должны подаваться рациональные числа")


def find_denominator(n_num_1: NaturalNumber, n_num_2: NaturalNumber, k=NaturalNumber("0")):
    """Определение первой цифры от деления большего натурального числа на меньшее"""
    result = NaturalNumber("0")
    temp_num = NaturalNumber(MUL_Nk_N(n_num_2, NaturalNumber(str(k))).__str__())  # n_num_2 * 10^k

    while COM_NN_D(n_num_1, MUL_NN_N(temp_num, NaturalNumber(str(result)))) in [2,0]:
        result = ADD_1N_N(result)

    return SUB_NN_N(result, NaturalNumber("1"))  # Возвращаем результат минус 1


def DIV_NN_Dk(num1: NaturalNumber, num2: NaturalNumber) -> NaturalNumber:
    if not (isinstance(num1, NaturalNumber) and isinstance(num2, NaturalNumber)):
        return ValueError("На вход должны подаваться натуральные числа")
    # Если num1 == num2, то результат 1
    if COM_NN_D(num1, num2) == 0:
        return NaturalNumber("1")

    # Убедимся, что num1 больше num2
    big = num1 if COM_NN_D(num1, num2) == 2 else num2
    small = num2 if COM_NN_D(num1, num2) == 2 else num1

    k = big.__len__() - small.__len__()
    digits_of_smaller = small.__len__()

    # Выделяем старшие разряды big, чтобы сравнивать с small
    necessary_big = NaturalNumber(big.__str__()[:digits_of_smaller])
    if COM_NN_D(necessary_big, small) == 1:
        necessary_big = NaturalNumber(big.__str__()[:digits_of_smaller + 1])
        k -= 1

    # Умножаем small на множитель, пока он не превысит necessary_big
    multiplier = 1
    small_multiplied = small
    while COM_NN_D(small_multiplied, necessary_big) != 2:
        multiplier += 1
        small_multiplied = ADD_NN_N(small_multiplied, small)

    result = NaturalNumber(str(multiplier - 1))
    return MUL_Nk_N(result, k)

def DIV_NN_N(num1: NaturalNumber, num2: NaturalNumber) -> NaturalNumber:
    "Неполное частное от деления натуральных чисел"
    if not (isinstance(num1, NaturalNumber) and isinstance(num2, NaturalNumber)):
        return ValueError("Числа должны быть натуральными")
    if num1.__str__() == "0" and num2.__str__() == "0":
        return  ValueError("деления на 0 запрещено")
    if num1.__str__() == "0" or num2.__str__() == "0":
        return NaturalNumber("0")
    # Проверка, что num1 >= num2
    if COM_NN_D(num1, num2) == 1:
        num1, num2 = num2, num1

    result = NaturalNumber("0")

    while COM_NN_D(num1, num2) in [2, 0]:  # пока num1 >= num2
        quotient = DIV_NN_Dk(num1, num2)
        num1 = SUB_NN_N(num1, MUL_NN_N(num2, quotient))
        result = ADD_NN_N(result, quotient)

    return result

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


# r1=RationalNumber(IntegerNumber("1"), NaturalNumber("2"))
# r2=RationalNumber(IntegerNumber("3"), NaturalNumber("9"))
# print(MUL_QQ_Q(r1,r2))

#n1 = NaturalNumber("0")
#n2 = NaturalNumber("0")
#print(DIV_NN_Dk(n1,n2))

#r=RationalNumber(IntegerNumber("2"), NaturalNumber("3"))
#p=Polynomial()
#p.makePolynomial("10*x^1+1")
#print(MUL_PQ_P(p,r).__str__())
