# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации
# операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым
# элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        result_str = ''
        for i in range(len(self.list_1)):
            result_str += f'{self.list_1[i]}\n'

        return result_str

    def __add__(self, other):
        result_list = []
        for i in range(len(self.list_1)):
            temp_list = []
            for j in range(len(self.list_1[i])):
                temp_list.append(self.list_1[i].__getitem__(j) + other[i].__getitem__(j))
            result_list.append(temp_list)

        return Matrix(result_list)

    def __getitem__(self, index):
        return self.list_1[index]


list = [[5, 5, 5, 7], [7, 7, 7, 9]]
list2 = [[8, 8, 8, 54], [12, 9, 9, 23]]
class_matrix = Matrix(list)
class_matrix2 = Matrix(list2)
print(class_matrix)
print(class_matrix2)
print(class_matrix + class_matrix2)
