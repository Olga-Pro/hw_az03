# 1. Создай гистограмму для случайных данных,
# сгенерированных с помощью функции `numpy.random.normal`.
#
# # Параметры нормального распределения
# mean = 0       # Среднее значение
# std_dev = 1    # Стандартное отклонение
# num_samples = 1000  # Количество образцов
#
# # Генерация случайных чисел,
# распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)


# Импорт библиотек
import numpy as np
import matplotlib.pyplot as plt

random_array = np.random.normal(0,1, 1000)
# print(random_array)

# Построение гистограммы
plt.hist(random_array, bins=50, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма для случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()