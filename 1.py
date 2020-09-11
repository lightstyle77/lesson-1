# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open('task1.txt', 'w')
line = input('Введите текст (для завершения введите пустую строку) \n')
while line:
    f.writelines(line)
    line = input('Введите текст (для завершения введите пустую строку) \n')
    if not line:
        break

f.close()
f = open('task1.txt', 'r')
content = f.readlines()
print(content)
f.close()
