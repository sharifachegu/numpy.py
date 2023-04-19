import numpy as np

distance = np.array([10, 20, 30])  # расстояние в метрах
time = np.array([2, 4, 6])  # время в секундах
velocity = distance / time
print("Скорость равна", velocity, "м/с")
