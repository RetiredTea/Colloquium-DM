from classes import *
from YoptaCode import * # код Артема

#===== НОД натуральных чисел ====
#===== принимает два числа возвращает одно - НОД (ввод/вывод объектами класса NaturalNumber) ====
def GCF_NN_N(num1: NaturalNumber, num2: NaturalNumber):
    def swap(a: NaturalNumber, b: NaturalNumber): 
        if a > b:
            return a, b # нужна функция сравнения пока что простая затычка
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
    return MOD_NN_N(num1 * num2, GCF_NN_N(num1, num2)) # нужна функция умножения чисел

#===== Сложение дробей ====
#===== принимает две дроби возвращает их сумму(ввод/вывод рациональое число) ====
# Нужны функции сложения целых чисел, умножения целового на целое, преобразования натурального в целое
def ADD_QQ_Q (frac1: RationalNumber, frac2: RationalNumber):
    denominator = (LCM_NN_N(frac1.denominator,frac2.denominator))
    numerator = frac1.numerator * (MOD_NN_N(denominator, frac1.denominator)) + frac2.numerator * (MOD_NN_N(denominator, frac2.denominator))
    frac_sum = RationalNumber(numerator, denominator)
    return(frac_sum) 

#===== Вычитание дробей ====
#===== принимает две дроби возвращает их разность(ввод/вывод строкой) ====
# нужны функции умножения целых чисел, вычетания целых чисел, преобразования натурального в целое
def SUB_QQ_Q(frac1: RationalNumber, frac2: RationalNumber):
    denominator = (LCM_NN_N(frac1.denominator, frac2.denominator))
    numerator = frac1.numerator * (MOD_NN_N(denominator, frac1.denominator)) - frac2.numerator * (MOD_NN_N(denominator, frac2.denominator))
    frac_sum = RationalNumber(numerator, denominator)
    return(frac_sum)

#===== Сложение многочленов ====
#=====  ====
def P1(polyn1:str, polyn2:str):
    pass

#===== Вычитание многочленов ====
#=====  ====
def P2():
    pass

#===== НОД многочленов ====
#=====  ====
def P11():
    pass

#===== Производная многочлена ====
#=====  ====
def P12():
    pass
