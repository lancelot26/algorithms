# Рекурсия: Факториал

def factorial(x):
    if x == 1:  # базовый случай
        return 1
    else:
        return x * factorial(x - 1)