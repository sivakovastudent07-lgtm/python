import time

def log_calls(filename):
    def decorator(func):
        def wrapper(a, b):  # фиксированные аргументы
            current_time = time.ctime()
            func_name = func.__name__

            args_text = f"{a}, {b}"
            result = func(a, b)

            log_line = f"[{current_time}] Функция '{func_name}' вызвана с аргументами: ({args_text}), результат: {result}\n"

            with open(filename, "a", encoding="utf-8") as f:
                f.write(log_line)

            return result
        return wrapper  
    return decorator