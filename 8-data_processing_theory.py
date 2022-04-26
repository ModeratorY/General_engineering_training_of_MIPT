import numpy as np 

'''
    NumPy - это библиотека языка Python, 
    добавляющая поддержку больших многомерных 
    массивов и матриц, вместе с большой библиотекой высокоуровневых
    математических функций для операции с этими массивами
'''

m = np.array([1, 2, 3]) # массив 
print("\nВыведет массив, который мы создали:", m, end = '\n\n')


# чтобы обратиться к элементу массива:
print("0 элемент массива:", m[0])
print("1 элемент массива:", m[1])
print("2 элемент массива:", m[2])

print("\nТакже можем использовать срезы:")
print("m[0:2] =", m[0:2])
print("m[1:] =", m[1:], end = '\n\n')


# Существуют разные методы, которые позволяют нам:

print("Метод ones():", np.ones(5))  # заполнить 5 элементов единиицами
print("Метод zeros():", np.zeros(5)) # заполнить 5 элементов нулями
print("Метод random.random():", np.random.random(5)) # заполнить 5 элементов рандомом
print("Метод empty():", np.empty(5), end = '\n\n') # если не хотим заполнять массив значениями (они будут при выводе)
# но в отличии от random(), значения empty() зависят от состояния памяти компьютера и ещё empty() самый быстрый метод)


# По умолчания тип данных NumPy float64 - число с плавающей точкой
# Но мы можем указать другой тип

m = np.zeros(1)
print("тип float64", type(m[0]))
m = np.zeros(1, dtype = np.int64)
print("тип int64", type(m[0]), end = '\n\n')


# Операции с массивами

first = np.array([1, 2, 3])
second = np.array([4, 5, 6])

print("first =", first)
print("second =", second)
print("first + second =", first + second)
print("first - second =", first - second)
print("first * second =", first * second)
print("first / second =", first / second)
print("first * 1.6 =", first * 1.6)
print("max in first:", first.max())
print("min in first:", first.min())
print("sum in first:", first.sum(), end = '\n\n')



# Матрицы (двумерные массивы)

data = np.array([[1, 2], [3, 4], [5, 6]]) # матрица 3x2
print("data:\n", data, end = '\n\n')
print("np.zeros((3, 2)):\n", np.zeros((3, 2)), end = '\n\n')


# Операции с матрицами 

data = np.array([[1, 2], [3, 4], [5, 6]]) # матрица 3x2
ones = np.ones((3, 2)) # в скобках пишется сначала количество строк, потому количество столбцов

print("data + ones: \n", data + ones, end = '\n\n')
print("data - ones: \n", data - ones, end = '\n\n')
# ... и так далее. Главное! Чтобы размер матриц был одинаков!


ones_row = np.ones((1, 2))
# можно складывать матрицы несоразмерные, только если во второй матрице
# будут совпадать либо строки, либо столбцы с первой матрицей, а второй параметр будет = 1

print("data + ones_row:\n", data + ones_row, end = '\n\n')

data = np.array([1, 2, 3])
powers_of_ten = np.array([[1, 10], [100, 1000], [10000, 100000]]) 
'''
    метод dot()
                 1     10
    (1 2 3).dot( 100   1000  ) = (30201 302010)
                 10000 100000
''' 

print("Перемножение data и powers_of_ten:\n", data.dot(powers_of_ten), end = '\n\n')


# Пример создания трёхмерного массива

example = np.array([ [[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]] ])

print("Количество измерений у массива:", example.ndim)
print("Количество элементов в массиве:", example.size)
print("Возвращает кортеж целых чисел:", example.shape, end = '\n\n')


# Удобное создание массива для дальнейшей обработки данных

''' Полная аналогия с range(начальный элемент, конечный элемент(не включая), шаг) '''
example_1 = np.arange(10) 
example_2 = np.arange(2, 10)
example_3 = np.arange(1, 9, 2)

print("example_1:", example_1)
print("example_2:", example_2)
print("example_3:", example_3, end = '\n\n')


# linspace(начальный, конечный, число чисел на которые мы хотим разбить массив)
example_4 = np.linspace(0, 20, num = 5) 
example_5 = np.linspace(0, 30, num = 6) 
print("example_4:", example_4)
print("example_5:", example_5, end = '\n\n')


# Сохраняем значения массива в файл и выгружаем их из файла

np.save('example_data', example) # чтобы сохранить в файл с разрешением .npy
data_file = np.load('example_data.npy') # чтобы выгрузить данные из файла

print("Данные из файла 'example_data':\n", data_file)
