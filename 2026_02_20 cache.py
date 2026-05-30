def cache(func):
    cache_storage = {}
    
    def wrapper(*args):
        if args in cache_storage:
            return cache_storage[args]
        
        result = func(*args)
        cache_storage[args] = result
        return result
    
    return wrapper


@cache
def my_sum(a, b):
    return a + b


def main():
    print(my_sum(2, 3))  
    print(my_sum(2, 3))   
    print(my_sum(5, 7))   
    print(my_sum(2, 3))   


if __name__ == '__main__':
    main()
