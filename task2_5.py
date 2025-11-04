def cache(func):
    results = {}
    def cached_f(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in results:
            print(f"результат для вызова функции с аргументами args={args}, kwargs={dict(kwargs)} найден в кэше")
            return results[key]
        else:
            print(f"результат для вызова функции с аргументами args={args}, kwargs={dict(kwargs)} вычисляется...")
            result = func(*args, **kwargs)
            results[key] = result
            return result
    return cached_f

@cache
def square(x):
    return int(x) * int(x)

@cache
def add(x, y):
    return int(x) + int(y)

@cache
def greet(name):
    return f"Привет, {name}!"

FUNCTIONS = {
    'square': square,
    'add': add,
    'greet': greet,
}

print("доступные функции:")
for name in FUNCTIONS:
    print(f"  - {name}")

func_name = input("выберите функцию: ").strip()

if func_name not in FUNCTIONS:
    print("ошибка: такой функции нет")
else:
    func = FUNCTIONS[func_name]
    args_input = input("введите аргументы через запятую (например: 5 или 'Алиса', 10): ").strip()
    
    if args_input:
        args_list = [part.strip() for part in args_input.split(',')]
        args = []
        for a in args_list:
            if a.startswith("'") and a.endswith("'"):
                args.append(a[1:-1])
            elif a.startswith('"') and a.endswith('"'):
                args.append(a[1:-1])
            else:
                args.append(a)
    else:
        args = []

    try:
        result = func(*args)
        print("результат:", result)
    except Exception as e:
        print("ошибка при выполнении:", e)