def cache(func):
    results = {} 
    def cached_f(a=0, b=0, c=0): 
        key = (a, b, c)

        if key in results:
            print(f"Результат для аргументов {key} найден в кэше.")
            return results[key]
        else:
            print(f"Вычисляем результат для аргументов {key}...")
            result = func(a, b, c)
            results[key] = result
            return result

    return cached_f
