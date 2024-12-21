import numpy as np

# Создание массива из чисел
array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций
sum_result = np.sum(array)  # Сумма
mean_result = np.mean(array)  # Среднее
std_result = np.std(array)  # Стандартное отклонение

# Вывод результатов
print("Массив:", array)
print("Сумма:", sum_result)
print("Среднее:", mean_result)
print("Стандартное отклонение:", std_result)