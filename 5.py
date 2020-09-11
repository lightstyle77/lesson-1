# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('task5.txt', 'w+') as f:
    line = input('Введите цифры через пробел \n')
    f.writelines(line)
    result = 0
    f.close()
    f = open('task5.txt', 'r')
    numbers = f.read().split()
    for i in range(len(numbers)):
        result += int(numbers[i])
    print(result)
