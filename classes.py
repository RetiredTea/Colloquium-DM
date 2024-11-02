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
    def __init__(self, deg=0, val=0, prev=None, next=None):
        self.val = val
        self.deg = deg
        self.prev = prev
        self.next = next


class Polynomial:
    def __init__(self, deg=0, val=0):
        self.head = PolynomialNode(deg, val, None)

    def add(self, deg, val):
        temp = self.head
        while (temp != None):
            if (deg < temp.deg and temp.next != None):
                temp = temp.next
            elif (deg == temp.deg):
                temp.val += val
                break
            else:
                elem = PolynomialNode(deg, val)
                if (deg > temp.deg):
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
        while (temp != None):
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
        while (temp != None):
            if (temp.deg == deg):
                return temp.val
        return 0


# Класс натурального числа
# Хранение натурального числа подразумевается в виде массива чисел ->
# Это поможет реализации посимвольных математических операций.
class NaturalNumber:

    def __init__(self, value: str):

        # Проверки на корректность ввода
        if not isinstance(value, str):
            raise ValueError('Число должно быть представлено строкой.')
        elif not value.isdigit() or int(value) < 0:
            raise ValueError('Значение должно быть натуральным числом или нулём.')

        # Инициализация массивом цифр
        self.value = list(map(int, list(str(int(value)))))

    # Вывод числа в виде строки
    def __str__(self):
        return ''.join(list(map(str, list(self.value))))

    # Возврат массива цифр
    def get_value(self):
        return self.value

    # Перегруженный len
    def __len__(self):
        return len(self.value)


# Класс целого числа
# Хранится в аналогично натуральному, но присутствует знак в виде int.
class IntegerNumber:

    def __init__(self, value: str):

        # Проверки на корректность ввода
        if not isinstance(value, str):
            raise ValueError("Число должно быть представлено строкой.")
        elif not (value.lstrip('-').isdigit()):
            raise ValueError("Значение должно быть целым числом.")

        # Знак числа хранится как int. (0 - "+", 1 - "-")
        self.sign = 0

        # Инициализация отрицательного и положительно числа соответственно
        if value[0] == '-':
            self.sign = 1
            self.value = list(map(int, list(value.lstrip('-'))))
        else:
            self.value = list(map(int, list(value)))

    # Вывод числа в виде строки
    def __str__(self):
        if self.sign == 1:
            return f"-{''.join(list(map(str, list(self.value))))}"
        else:
            return ''.join(list(map(str, list(self.value))))

    # Возврат массива цифр
    def get_value(self):
        return self.value

    # Возврат знака
    def get_sign(self):
        return self.sign

    # Перегруженный len
    def __len__(self):
        return len(self.value)


# Класс рационального числа
# Хранится как целое и натуральное число для числителя и знаменателя соответственно.
class RationalNumber:

    def __init__(self, numerator, denominator=NaturalNumber("1")):

        # Проверки на корректность ввода
        if (not isinstance(numerator, IntegerNumber)) and (not isinstance(denominator, NaturalNumber)):
            raise ValueError("Числитель и знаменатель должны быть классами IntegerNumber и NaturalNumber соответственно.")

        # Инициализация числителя и знаменателя
        self.numerator = numerator
        if denominator != ["0"]:
            self.denominator = denominator
        else:
            raise ValueError("Знаменатель не может быть нулём")

    # Вывод числа в виде строки
    def __str__(self):

        # Так как числитель и знаменатель - объекты предыдущих классов, вызываются методы __str__.
        return f"{str(self.numerator)}/{str(self.denominator)}"
