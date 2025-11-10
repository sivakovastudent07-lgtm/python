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
def my_function(a, b, c):
    time.sleep(0.001)  
    return a + b + c

timed_my_function = timing(my_function)

print("введите три аргумента через пробел (например: 1 2 3): ")
user_input = input().strip()

if not user_input:
    print("ничего не введено")
else:
    parts = user_input.split()
    if len(parts) != 3:
        print("нужно ровно три аргумента")
    else:
        try:
            args = []
            for part in parts:
                try:
                    args.append(int(part))
                except ValueError:
                    args.append(float(part))
            
            a, b, c = args
            result = timed_my_function(a, b, c)
            print("результат:", result)
            
        except ValueError:
            print("ошибка: все аргументы должны быть числами")
        except Exception as error:
            print("ошибка:", error)