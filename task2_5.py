def cache(func):
    results = {}  
    def cached_f(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
       
        if key in results:
            print(f"результат для вызова функции с аргументами args={args}, kwargs={dict(kwargs)} найден в кэше")
            return results[key]
        else:
            print(f"результат для вызова функции с аргументами args={args}, kwargs={dict(kwargs)}...")
            result = func(*args, **kwargs)
            results[key] = result
            return result
            
    return cached_f