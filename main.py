# Запрашиваем у пользователя число
n = int(input("Введите число: "))

# Инициализируем переменные
factorial = 1  # Переменная для хранения результата факториала
i = 1  # Счетчик для цикла while

# Используем цикл while для вычисления факториала
while i <= n:
    factorial *= i  # Умножаем текущий факториал на значение счетчика
    i += 1  # Увеличиваем счетчик на 1

# Выводим результат
print(f"Факториал числа {n} равен {factorial}")
