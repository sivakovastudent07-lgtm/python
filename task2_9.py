def type_check(type_a, type_b):
    """
    декоратор для проверки типов двух аргументов функции
    """
    def decorator(func):
        def checked_function(a=0, b=0):
            if not isinstance(a, type_a):
                print(f"ошибка: аргумент 'a' должен быть типа {type_a.__name__}, а получен {type(a).__name__}")
                return None
            if not isinstance(b, type_b):
                print(f"ошибка: аргумент 'b' должен быть типа {type_b.__name__}, а получен {type(b).__name__}")
                return None

            return func(a, b)

        return checked_function
    return decorator