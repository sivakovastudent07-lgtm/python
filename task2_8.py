import time

def timing(func):
    """
    декоратор для измерения времени выполнения функции с фиксированными аргументами a, b, c
    в миллисекундах
    """
    def timed_f(a=0, b=0, c=0):
        start_time = time.time()
        result = func(a, b, c)
        end_time = time.time()
        elapsed_ms = (end_time - start_time) * 10**3
        print(f"время выполнения функции '{func.__name__}': {elapsed_ms:.2f} мс")
        return result

    return timed_f
