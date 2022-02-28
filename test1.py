def sum1():
    print(num1 + num2)


def subtraction():
    print(num1 - num2)


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
    else:
        print("Введите +, -, *, /: ")
