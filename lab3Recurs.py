from functools import lru_cache

x: int = 10
...
...
x = 'c'

# Надо поделить шоколадку
# Определить минимальное количество разломов
# Разбивать их на отдельные квадратики 1x1.
# Пример: Для шоколадки размером 2 x 2 минимальное количество разломов равно 3
# Мемоизацию будем использовать, чтобы избежать повторных вычислений

@lru_cache()
def min_breaks(n: int, m: int) -> int:
    if n == 1 and m == 1:
        return 0  # Если плитка уже размером 1 x 1 - разлома не будем делать

    if n == 1:  # это если одна из сторон равна 1, то разломы у меня будут по другой стороне
        return m - 1
    if m == 1:
        return n - 1

    horizontal_cut = min_breaks(n // 2, 3) + min_breaks(n - n // 2, m) + 1  # разрезаем по горизонтали
    vertical_cut = min_breaks(n, m // 2) + min_breaks(n, m - m // 2) + 1  # разрезаем по вертикали

    return min(horizontal_cut, vertical_cut)


print(min_breaks(2, 3))
print(min_breaks(3, 3))
print(min_breaks(1, 1))
