def sum1():
    print(num1 + num2)


def subtraction():
    print(num1 - num2)


def multiplication():
    print(num1 * num2)


def division():
    print(num1 / num2)


try:
    while True:
        num1 = float(input("Введите первое число либо 0, если хотите завершить программу: "))
        if num1 == 0:
            break
        num2 = float(input("Введите второе число: "))
        sign = input("Введите +, -, *, /: ")
        if sign == '+':
            sum1()
        elif sign == '-':
            subtraction()
        elif sign == '*':
            multiplication()
        elif sign == '/':
            division()
        else:
            print("Введите +, -, *, /: ")
except ZeroDivisionError:
    print("Деление на 0")
