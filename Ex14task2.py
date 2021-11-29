from math import *

ALLOWED_SYMBOLS = ["+", "-", "*", "/", "^", "="]


class UserInputError(Exception):
    pass


def has_string_symbols(string, symbols):
    for symbol in symbols:
        if symbol in string:
            return True
    return False


def menu():
    print("Действия досупные с числами ( +, -, *, /, ^, = )")


def sum(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def st(num1, num2):
    try:
        return pow(num1, num2)
    except ValueError:
        print("You can't raise 0 to a negative power.\nRewrite second number 2.")
        return num1


def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("You can't divide by zero.\nRewrite second number 2.")
        return num1
    except TypeError:
        print("Some value was incorrect!\nRewrite second number 2.")
        return num1


def clc():
    menu()
    cha = input("Выберите действие из пункта меню (= - завершит подсчёт): ").strip()

    def user_input_check_loop():
        while True:
            if has_string_symbols(cha, ALLOWED_SYMBOLS):
                return cha
            else:
                raise UserInputError('You used not allowed symbols!')

    num1 = float(input("Введите первое число: "))
    while cha != "=":
        num2 = float(input("Введите второе число: "))
        if cha == "+":
            num1 = sum(num1, num2)
        elif cha == "-":
            num1 = sub(num1, num2)
        elif cha == "*":
            num1 = mul(num1, num2)
        elif cha == "/":
            num1 = div(num1, num2)
        elif cha == "^":
            num1 = st(num1, num2)
        else:
            user_input_check_loop()
        print("Результат", num1)
        menu()
        cha = input("Выберите действие из пункта меню (= - завершит подсчёт): ").strip()
    print("Окончательный результат", num1)


clc()