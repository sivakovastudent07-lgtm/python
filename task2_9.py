def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(f"функция '{func.__name__}' ожидает {len(expected_types)} аргументов, получено {len(args)}")
            
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"аргумент {i+1} функции '{func.__name__}' должен быть типа {expected_type.__name__}, "
                        f"получен {type(arg).__name__}"
                    )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))        
    print(add(5, -1))       
    
