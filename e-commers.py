# Пример функции трансформации
def T(n: int) -> int:
    # Имитация долгой операции
    import time
    time.sleep(1)
    return n - 5  # Пример трансформации

# Список значений
N = [10, 3, 15, 0, -2, 20]

result = [T(n) for n in N if T(n) > 0]

print(result)