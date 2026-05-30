def bread(func):
    def wrapper():
        result = func()
        return "Bread\n" + result + "\nBread"
    return wrapper

def salat(func):
    def wrapper():
        result = func()
        return "Salat\n" + result
    return wrapper

def tomato(func):
    def wrapper():
        result = func()
        return "Tomato\n" + result
    return wrapper

def meat(func):
    def wrapper():
        result = func()
        return "Meat\n" + result
    return wrapper

@bread
@meat
@tomato
@salat
def make_sandwich():
    return ''

def main():
    print(make_sandwich())

if __name__ == '__main__':
    main()
