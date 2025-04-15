import random
import statistics
import math

# Генерация списка из 100 случайных чисел
random_numbers = [random.randint(1, 100) for _ in range(100)] # выполняет задачу 100 раз

# Среднее арифметическое
mean_value = statistics.mean(random_numbers)

# Медиана
median_value = statistics.median(random_numbers)

# Стандартное отклонение
std_deviation = statistics.stdev(random_numbers)

# Округлённое значение квадратного корня
sqrt_rounded = round(math.sqrt(sum(random_numbers)))

print("Среднее арифметическое:", mean_value)
print("Медиана:", median_value)
print("Стандартное отклонение:", std_deviation)
print("Округлённый корень:", sqrt_rounded)
