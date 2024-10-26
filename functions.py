def function_1():
    print("Функция 1 была вызвана")

def function_2():
    print("Функция 2 была вызвана")

def function_3():
    print("Функция 3 была вызвана")
def function_4():
    print("Функция 4 была вызвана")
def function_5():
    print("Функция 5 была вызвана")
def function_6():
    print("Функция 6 была вызвана")
def function_7():
    print("Функция 7 была вызвана")
def function_8():
    print("Функция 8 была вызвана")
def function_9():
    print("Функция 9 была вызвана")
def function_10():
    print("Функция 10 была вызвана")
def function_11():
    print("Функция 11 была вызвана")
def function_12():
    print("Функция 12 была вызвана")
def function_13():
    print("Функция 13 была вызвана")
def function_14():
    print("Функция 14 была вызвана")
def function_15():
    print("Функция 15 была вызвана")
def function_15():
    print("Функция 15 была вызвана")
def function_16():
    print("Функция 16 была вызвана")
def function_17():
    print("Функция 17 была вызвана")
def function_18():
    print("Функция 18 была вызвана")
def function_19():
    print("Функция 19 была вызвана")
def function_20():
    print("Функция 20 была вызвана")

    #Впишите свое
def function_40():
    print("Функция 45 была вызвана")

# Словарь для маппинга номеров на функции
functions_dict = {
    str(i): globals()[f'function_{i}'] for i in range(1, 20)
}