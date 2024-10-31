import re
from fractions import Fraction
import math

# Используйте метод makePolynomial для создания нового многочлена, передавайте туда строку вида (+-n)x(^m) - то что в скобка опциональноэ
# Используйте метод getStringPolynomial для получения многочлена: строки вида (+-n)x(^m)
# Используйте метод add для добавления нового члена, либо изменения коэффициента у старого (складывает старое значение с переданным)
# Используйте метод getCoeff чтобы узнать коэффициент по степени члена

# Примеры исполбзования:

# poly = Polynomial()
# poly.makePolynomial("+50x^5 - 4x^3 - 9 + x - 10x^10")
# print(poly.getStringPolynomial())
        
# a = Polynomial(1, 10)
# a.add(3, 3)
# a.add(3, 2)
# a.add(1, 4)
# a.add(5, 6)
# a.add(10, -1)
# print(a.getStringPolynomial())

class PolynomialNode:
    def __init__(self, deg = 0, val = 0, prev = None, next = None):
        self.val = val
        self.deg = deg
        self.prev = prev
        self.next = next

class Polynomial:
    def __init__(self, deg = 0, val = 0):
        self.head = PolynomialNode(deg, val, None)
        
    def add(self, deg, val):
        temp = self.head
        while(temp != None):
            if(deg < temp.deg and temp.next != None):
                temp = temp.next
            elif(deg == temp.deg):
                temp.val += val
                break
            else:
                elem = PolynomialNode(deg, val)
                if(deg > temp.deg):
                    elem.next = temp
                    elem.prev = temp.prev
                    if temp.prev != None:
                        temp.prev.next = elem
                    temp.prev = elem
                else:
                    elem.prev = temp
                    elem.next = temp.next
                    if temp.next != None:
                        temp.next.prev = elem
                    temp.next = elem
                break
        temp = self.head.prev
        while(temp != None):
            self.head = temp
            temp = temp.prev
    
    def getStringPolynomial(self):
        indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }

        def degree(deg):
            degree = ""
            temp = str(deg)
            for char in temp:
                degree += indexes[char] or ""
            return degree
        
        if not self.head:
            return "0"
        
        res = ""
        temp = self.head
        while temp is not None:
            if temp.val != 0:
                if res:  # Если это не первый элемент
                    if temp.val > 0:
                        res += " + "
                    else:
                        res += " - "
                else:
                    if temp.val < 0:
                        res += "-"
                coeff_str = str(abs(temp.val))
                if temp.deg == 0:
                    res += coeff_str
                else:
                    if (abs(temp.val) == 1):
                        if temp.deg == 1:
                            res += f"x"
                        else:
                            res += f"x{degree(temp.deg)}"
                    else:
                        if temp.deg == 1:
                            res += f"{coeff_str}x"
                        else:
                            res += f"{coeff_str}x{degree(temp.deg)}"
            temp = temp.next
        
        return res or "0"

    def makePolynomial(self, polynomial_str):
        # Удаляем пробелы и разбиваем строку на термины
        polynomial_str = polynomial_str.replace(" ", "")
        terms = re.split(r'(?=[+-])', polynomial_str)  # Разделяем по знакам

        for term in terms:
            if term:  # Проверяем, что строка не пустая
                if 'x' in term:
                    # Обрабатываем термины с x
                    if '^' in term:
                        coeff_str, deg_str = term.split('x^')
                        deg = int(deg_str)
                    else:
                        coeff_str = term[:-1]  # Убираем 'x'
                        deg = 1

                    # Определяем коэффициент
                    if coeff_str == '' or coeff_str == '+':
                        coeff = 1
                    elif coeff_str == '-':
                        coeff = -1
                    else:
                        coeff = int(coeff_str)

                else:
                    # Обрабатываем константы (термины без x)
                    coeff = int(term)
                    deg = 0

                # Добавляем в многочлен
                self.add(deg, coeff)
                
    def getCoeff(self, deg):
        temp = self.head
        while(temp != None):
            if(temp.deg == deg):
                return temp.val
        return 0


class NaturalNumber:
    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or int(value) <= 0:
            raise ValueError("Значение должно быть натуральным числом.")
        self.value = int(value)  # Преобразуем строку в натуральное число

    def __str__(self):
        return str(self.value)

    def is_natural(self):
        return True

    def sum(self, other):  # Заглушка для сложения столбиком
        return NaturalNumber(str(self.value + other.value))

    def multiply(self, other):  # Заглушка для умножения столбиком
        return NaturalNumber(str(self.value * other.value))


class IntegerNumber(NaturalNumber):
    def __init__(self, value):
        if not isinstance(value, str) or not (value.lstrip('-').isdigit()):
            raise ValueError("Значение должно быть целым числом.")

        self.value = int(value)  # Преобразуем строку в целое число
        super().__init__(str(abs(self.value)) if self.value != 0 else "0")

    def __str__(self):
        return str(self.value)

    def is_integer(self):
        return True

    def subtract(self, other):  # Заглушка для вычитания столбиком
        return IntegerNumber(str(self.value - other.value))

    def negate(self):
        return IntegerNumber(str(-self.value))


class RationalNumber(IntegerNumber):
    def __init__(self, numerator, denominator="1"):
        if not (isinstance(numerator, str) and isinstance(denominator, str)):
            raise ValueError("Числитель и знаменатель должны быть строками.")

        num = int(numerator)
        denom = int(denominator)
        if denom == 0:
            raise ValueError("Знаменатель не может быть нулем.")

        self.value = Fraction(num, denom)  # Сохраняем как дробь
        super().__init__(str(self.value.numerator))  # Для корректного наследования проверок

    def __str__(self):
        if self.value.denominator != 1:
            return f"{self.value.numerator}/{self.value.denominator}"
        else:
            return str(self.value.numerator)

    def is_rational(self):
        return True

    def sum(self, other):  # Заглушка для сложения дробей
        result = self.value + other.value
        return RationalNumber(str(result.numerator), str(result.denominator))

    def multiply(self, other):  # Заглушка для умножения дробей
        result = self.value * other.value
        return RationalNumber(str(result.numerator), str(result.denominator))

    def divide(self, other): #Заглушка для деления
        if other.value == 0:
            raise ZeroDivisionError("Деление на ноль.")
        result = self.value / other.value
        return RationalNumber(str(result.numerator), str(result.denominator))


class RealNumber(RationalNumber):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Значение должно быть строкой.")

        try:
            self.value = float(value)
        except ValueError:
            raise ValueError("Значение должно быть вещественным числом.")

    def __str__(self):
        return str(self.value)

    def is_real(self):
        return True

    def power(self, exponent):  # Заглушка для возведения в степень
        return RealNumber(str(self.value ** exponent))