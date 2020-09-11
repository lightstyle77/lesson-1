# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f = open('task2.txt', 'r')
content = f.read()
print(f'Содержимое файла: \n{content}')
f = open('task2.txt', 'r')
content = f.readlines()
print(f'Количество строк в файле - {len(content)}')
f = open('task2.txt', 'r')
content = f.readlines()
for i in range(len(content)):
    print(f'Количество слов {i + 1} - ой строки {len(content[i].split(" "))}')
