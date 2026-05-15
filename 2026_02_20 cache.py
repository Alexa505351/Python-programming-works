def cache(func):
    storage = {}
    
    def wrapper(*args):
        key = args
        if key in storage:
            print(f"Возвращаем из кэша для аргументов {args}")
            return storage[key]
        print(f"Вычисляем для аргументов {args}")
        result = func(*args)
        storage[key] = result
        return result
    return wrapper

@cache
def add(a, b):
    return a + b
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("=== Пример с add ===")
print(add(2, 3))   
print(add(2, 3))   
print(add(5, 7))
print(add(2, 3))

print("\n=== Пример с fibonacci ===")
print(fibonacci(5))
print(fibonacci(5))
print(fibonacci(6))  
