import numpy as np
import matplotlib.pyplot as plt

# конструкция with ... as ... помогает продолжить работать программе
# даже если не будет файл (или закрыт) или если будут прочие ошибки ...
with open("7-1-settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")] 
    '''
        в переменную tmp мы записываем список из чисел типа float:
        частоту дискретизации (период изм.) и шаг квантования АЦП (шаг U)
    '''
    
data_array = np.loadtxt("7-1-data.txt", dtype = float)
# получаем данные с АЦП - метод .loadtxt("filename", type_data)

print(data_array)

'''
    Figure - внешний контейнер для графиков (включает в себя 1 или более Axes)
    Axes - именно та диаграмма, которую мы ожидаем увидеть, настоящий график
    В свою очередь Axes имеет свои оси: y_Axix и x_Axis
'''

# Способ создание Figure с одним Axes это метод .subplots(nrows = кол-во графиков)

fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)

# Мы можем записать размер Figure в дюймах записав в кортеж (width, height) - (ширина, высота) в дюймах
# dpi - количество точек на дюйм
# figsize = (w, h)
# px, py = w * dpi, h * dpi

ax.plot(data_array) # подготовить график к запуску
fig.savefig("8-test_graph.png") # сохраняет график как картинку в директории
plt.show() # показать график