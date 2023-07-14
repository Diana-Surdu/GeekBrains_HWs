# Создайте функцию генератор чисел Фибоначчи


def fibonacci(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))