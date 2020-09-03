# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов


def my_func(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    max_arg = max(arg_list)
    arg_list.remove(max_arg)
    max2_arg = max(arg_list)
    return max_arg + max2_arg


print(my_func(60, 10, 11))
