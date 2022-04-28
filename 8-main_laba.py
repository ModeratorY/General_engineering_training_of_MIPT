import numpy as np
import matplotlib.pyplot as plt

with open("7-1-settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")] 

data_array = np.loadtxt("7-1-data.txt", dtype = int)

x = np.linspace(0, 36.36, num = len(data_array)) 
y = data_array * 3.3 / 256

fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)

ax.plot(x, y, '-g', label = 'line 1') # добавление легенды
ax.legend()

ax.set_xlim(0, 40) # установка макс и мин значения на графике
ax.set_ylim(0, 3.5)

plt.minorticks_on()

plt.grid(color = 'm', which = 'major')
plt.title("Зависимость зарядки C от времени t")

plt.ylabel("Напряжение, В")
plt.xlabel("Время, с")
plt.text(6, 0.8, "Общая продолжительность эксперимента: 36.36 c") # название графика

plt.savefig("8-main_graph.png")