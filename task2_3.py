import time

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs): 
            current_time = time.ctime()
            func_name = func.__name__
            args_text = ", ".join(
                [repr(arg) for arg in args] + 
                [f"{k}={repr(v)}" for k, v in kwargs.items()]
            )
            result = func(*args, **kwargs)
     
            log_line = f"[{current_time}] Функция '{func_name}' вызвана с аргументами: ({args_text}), результат: {result}\n"
            with open(filename, "a", encoding="utf-8") as f:
                f.write(log_line)

            return result
        return wrapper  
    return decorator