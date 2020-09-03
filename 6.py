# Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func()

def int_func(text):
    result_text = ''
    text_list = text.split(' ')
    for temp in range(len(text_list)):
        temp = text_list.pop(0)
        result_text = f'{result_text}{temp.capitalize()} '
    return result_text


print(int_func('Bob dog cat rabbit'))
