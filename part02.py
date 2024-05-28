# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.

# Импорт библиотек
import numpy as np
import matplotlib.pyplot as plt


random_x = np.random.rand(100)  # массив из 100 случайных чисел
random_y = np.random.rand(100)  # массив из 100 случайных чисел
#print(random_array1)

# Создаем диаграмму рассеяния
plt.scatter(random_x, random_y)

# Добавление заголовка и меток осей
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния для случайных данных")

# Показать график
plt.show()