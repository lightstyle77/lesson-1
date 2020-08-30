# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict

seasons_list = ['winter', 'spring', 'summer', 'autumn']
month = int(input('Введите номер месяца от 1 до 12: '))
if month == 1 or month == 12 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])

seasons_dict = {'winter': (1, 2, 12), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'autumn': (9, 10, 11)}
month = int(input('Введите номер месяца от 1 до 12: '))
for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print(key)
