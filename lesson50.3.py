import matplotlib.pyplot as plt

# Пример данных:
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Столбчатая диаграмма:
plt.bar(categories, values)
plt.title('Пример столбчатой диаграммы')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()