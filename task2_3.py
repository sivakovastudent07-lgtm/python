import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args):
            current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            line = f"{current_time} | {func.__name__} | {args}\n"
            with open(filename, "a", encoding="utf-8") as f:
                f.write(line)
            return func(*args)
        return wrapper
    return decorator

@log_calls("log_calls.log")
def square(number):
    return float(number) * float(number)

@log_calls("log_calls.log")
def text_lower(text):
    return str(text).lower()

@log_calls("log_calls.log")
def show_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

@log_calls("log_calls.log")
def multiply(number1, number2):
    return float(number1) * float(number2)

FUNCTIONS = {
    'square': square,
    'text_lower': text_lower,
    'show_time': show_time,
    'multiply': multiply,
}

print("Доступные функции:")
for name in FUNCTIONS:
    print(f"  - {name}")

func_name = input("Введите имя функции: ").strip()

if func_name not in FUNCTIONS:
    print("Ошибка: такой функции нет")
else:
    func = FUNCTIONS[func_name]
    filename = "log_calls.log" 
    if func_name == 'show_time':
        args = []
    elif func_name in ('square', 'text_lower'):
        arg = input("Введите аргумент: ").strip()
        args = [arg]
    elif func_name == 'multiply':
        a = input("Введите первый аргумент: ").strip()
        b = input("Введите второй аргумент: ").strip()
        args = [a, b]
    else:
        args = []

    try:
        result = func(*args)
        print("Результат:", result)
    except Exception as error:
        print("Ошибка при выполнении функции:", error)