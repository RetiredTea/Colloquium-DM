import re
from functions import function_q5

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
    
    # Вывод числа в виде цечисленного значения   
    def __int__(self):
        return int(str(self))

    # Возврат массива цифр
    def get_value(self):
        return self.value

    # Возврат знака
    def get_sign(self):
        return self.sign

    # Перегруженный len
    def __len__(self):
        return len(self.value)

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
    
    # Вывод числа в виде цечисленного значения
    def __int__(self):
        return int(str(self))

    # Возврат массива цифр
    def get_value(self):
        return self.value

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
        if denominator.__str__() != "0":
            self.denominator = denominator
        else:
            raise ValueError("Знаменатель не может быть нулём")

    # Вывод числа в виде строки
    def __str__(self):

        # Так как числитель и знаменатель - объекты предыдущих классов, вызываются методы __str__.
        return f"{str(self.numerator)}/{str(self.denominator)}"

#Вспомогательный класс узла многочлена
#Поле val - коэффициент
#Поле deg - степень
class PolynomialNode:
    def __init__(self, deg = NaturalNumber("0"), val = RationalNumber("0"), prev = None, next = None):
        if (not isinstance(deg, NaturalNumber)) and (not isinstance(val, RationalNumber)):
            raise ValueError("Степень и коэффициент должны быть классами NaturalNumber и RationalNumber соответственно.")
        self.val = val
        self.deg = deg
        self.prev = prev
        self.next = next

#Класс многочлена
#Реализован на базе двусвязного списка
class Polynomial:
    # Инициализация многочлена
    def __init__(self):
        self.head = PolynomialNode()

    # Возвращает многлчен в виде строки  
    def __str__(self):
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
            if int(temp.val.numerator) != 0:
                if res:  # Если это не первый элемент
                    if (temp.val.numerator.get_sign() == 0):
                        res += " + "
                    else:
                        res += " - "
                else:
                    if (temp.val.numerator.get_sign() == 1):
                        res += "-"
                
                coeff_str = ""
                if (int(temp.val.denominator) == 1 and abs(int(temp.val.numerator)) != 1):
                    coeff_str = str(temp.val.numerator)
                elif (int(temp.val.denominator) != 1):
                    coeff_str = str(temp.val)
                if (temp.val.numerator.get_sign() == 1):
                    coeff_str = coeff_str[1:]
                if int(temp.deg) == 0:
                    if coeff_str == "":
                        coeff_str = "1"
                    res += coeff_str
                else:
                    if int(temp.deg) == 1:
                        res += f"{coeff_str}x"
                    else:
                        res += f"{coeff_str}x{degree(temp.deg)}"
            temp = temp.next
        
        return res or "0"
    
    # Добавление/изменение (сумма старого и нового коэффициентов) одночлена
    def add(self, deg: NaturalNumber, val: RationalNumber):
        if (not isinstance(deg, NaturalNumber)) and (not isinstance(val, RationalNumber)):
            raise ValueError("Степень и коэффициент должны быть классами NaturalNumber и RationalNumber соответственно.")
        
        temp = self.head
        while(temp != None):
            # Ищем для вставки место в списке
            if(int(deg) < int(temp.deg) and temp.next != None):
                temp = temp.next
            
            # Если у степени уже есть коэффициент
            elif(str(deg) == str(temp.deg)):
                temp.val = function_q5(temp.val, val)
                break

            # Если нашли место для вставки, то вставляем
            else:
                elem = PolynomialNode(deg, val)
                if(int(deg) > int(temp.deg)):
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

        # Если после вставки элемента мы не в начале то переходим в начало
        while(temp != None):
            self.head = temp
            temp = temp.prev

    # Создание многочлена при помощи входной строки
    def makePolynomial(self, input_str: str):
        # Удаляем пробелы и разбиваем строку на термины
        input_str = input_str.replace(" ", "")
        input_str = input_str.replace("*", "")
        terms = re.split(r'(?=[+-])', input_str)  # Разделяем по знакам

        for term in terms:
            if term:  # Проверяем, что строка не пустая
                term = term.replace("+", "")
                if 'x' in term:
                    # Обрабатываем термины с x
                    if '^' in term:
                        coeff_str, deg = term.split('x^')
                    else:
                        coeff_str = term[:-1]  # Убираем 'x'
                        deg = "1"

                    if coeff_str == "-" or coeff_str == "":
                        coeff_str += "1"
                    if '/' in coeff_str:
                        num_str, denom_str = coeff_str.split('/')
                        coeff = RationalNumber(IntegerNumber(num_str), NaturalNumber(denom_str))
                    else:
                        coeff = RationalNumber(IntegerNumber(coeff_str))


                else:
                    # Обрабатываем константы (термины без x)
                    if '/' in term:
                        num_str, denom_str = term.split('/')
                        coeff = RationalNumber(IntegerNumber(num_str), NaturalNumber(denom_str))
                    else:
                        coeff = RationalNumber(IntegerNumber(term))
                    deg = "0"
                # Добавляем в многочлен
                self.add(NaturalNumber(deg), coeff)

    # Возвращает коэффициент при степени
    def getCoeff(self, deg: NaturalNumber):
        if not isinstance(deg, NaturalNumber):
            raise ValueError("Степень должна быть классом NaturalNumber.")
        
        # Проходимся по списку и возвращаем значение
        temp = self.head
        while(temp != None):
            if(int(temp.deg) == int(deg)):
                return temp.val
            temp = temp.next
        return RationalNumber("0")
    
    # Возвращает массив степеней, у которых коэффициенты отличны от нуля
    def getDegrees(self):
        arr = []
        # Проходимся по списку и добавляем в массив степень, если коэффициент не ноль
        temp = self.head
        while(temp != None):
            if int(temp.val.numerator) != 0:
                arr.append(int(temp.deg))
            temp = temp.next
        return arr or [0]
    
    # Изменяет степень на новую
    def changeDegree(self, deg: NaturalNumber, newdeg: NaturalNumber):
        if (not isinstance(deg, NaturalNumber)) and (not isinstance(newdeg, NaturalNumber)):
            raise ValueError("Степени должны быть классом NaturalNumber.")
        
        # Проходимся по списку
        temp = self.head
        while(temp != None):
            # Если нашли значение, то добавляем новый элемент с новой степенью и старым коэффициентом, а коэффициент у старой степени зануляем
            if int(temp.deg) == int(deg):
                self.add(newdeg, temp.val)
                temp.val = 0
            temp = temp.next
        return
   

'''
Пример использования класса многочлена

x = RationalNumber(IntegerNumber("28"),NaturalNumber("11"))
poly = Polynomial()

print(str(poly))

poly.add(NaturalNumber("1"), x)

print(str(poly))

poly.add(NaturalNumber("10"), RationalNumber(IntegerNumber("-10"),NaturalNumber("1")))

print(str(poly))

poly.add(NaturalNumber("5"), RationalNumber(IntegerNumber("-1"),NaturalNumber("1")))

print(str(poly))

poly.add(NaturalNumber("5"), RationalNumber(IntegerNumber("1"),NaturalNumber("1")))

print(str(poly))

print(poly.getDegrees())

poly.changeDegree(NaturalNumber("1"), NaturalNumber("2"))

print(str(poly))

print(poly.getDegrees())

poly = Polynomial()
poly.makePolynomial("10*x^10 - 1x^5 - 103/28*x^3 + 1/2x - 10/2")
print(poly)
print(poly.getDegrees())
print(poly.getCoeff(NaturalNumber("0")))


output:
0
28/11x
-10x¹⁰ + 28/11x
-10x¹⁰ - x⁵ + 28/11x
-10x¹⁰ + 28/11x
[10, 1]
-10x¹⁰ + 28/11x²
[10, 2]
10x¹⁰ - x⁵ - 103/28x³ + 1/2x - 10
[10, 5, 3, 1, 0]
-10/1
'''