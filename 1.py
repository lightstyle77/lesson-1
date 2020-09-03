# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def division(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


print(division(0, 5))
