from classes import *
from YoptaCode import * # код Артема
'''
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
    return num2


#===== НОК натуральных чисел ====
#===== принимает два числа возвращает одно - НОК (ввод/вывод объектами класса NaturalNumber) ====
def LCM_NN_N(num1: NaturalNumber, num2: NaturalNumber):
    return MOD_NN_N(MULL_NN_N(num1,num2), GCF_NN_N(num1, num2)) # нужна функция умножения чисел

#===== Сложение дробей ====
#===== принимает две дроби возвращает их сумму(ввод/вывод рациональое число) ====
# Нужны функции сложения целых чисел, умножения целового на целое, преобразования натурального в целое
def ADD_QQ_Q (frac1: RationalNumber, frac2: RationalNumber):
    denominator = (LCM_NN_N(frac1.denominator,frac2.denominator))
    numerator = ADD_ZZ_Z(MUL_ZZ_Z(frac1.numerator, TRANS_N_Z((MOD_NN_N(denominator, frac1.denominator)))),\
                        MUL_ZZ_Z(frac2.numerator, TRANS_N_Z(MOD_NN_N(denominator, frac2.denominator))))
    frac_sum = RationalNumber(numerator, denominator)
    return(frac_sum) 

#===== Вычитание дробей ====
#===== принимает две дроби возвращает их разность(ввод/вывод строкой) ====
# нужны функции умножения целых чисел, вычетания целых чисел, преобразования натурального в целое
def SUB_QQ_Q(frac1: RationalNumber, frac2: RationalNumber):
    denominator = (LCM_NN_N(frac1.denominator, frac2.denominator))
    numerator = SUB_ZZ_Z(MUL_ZZ_Z(frac1.numerator, TRANS_N_Z((MOD_NN_N(denominator, frac1.denominator)))),\
                        MUL_ZZ_Z(frac2.numerator, TRANS_N_Z(MOD_NN_N(denominator, frac2.denominator))))
    frac_sum = RationalNumber(numerator, denominator)
    return(frac_sum)
'''
#===== Сложение многочленов ====
#=====  ====
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

#===== Вычитание многочленов ====
#=====  ====
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

#===== НОД многочленов ====
#===== Пока не робит ====
def GCF_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
    # Начинаем с двух многочленов
    a = poly1
    b = poly2
    while True:
        remainder = MOD_PP_P(a, b)
        # Обновляем a и b
        a = b
        b = remainder
        

#===== Производная многочлена ====
#=====  ====
def DER_P_P(polyn: Polynomial):
    temp = polyn.head
    while temp is not None:
        if str(temp.deg) != '1' and str(temp.deg) != '0':
            temp.val = MUL_QQ_Q(temp.val, TRANS_Z_Q(TRANS_N_Z(temp.deg)))
            temp.deg = SUB_NN_N(temp.deg, NaturalNumber('1'))
        elif str(temp.deg) == '1':
            temp.deg = '0'

        elif str(temp.deg) == '0':
            temp = temp.prev
            temp.next = None
            break
        temp = temp.next
    return polyn