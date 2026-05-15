# Декораторы для добавления ингредиентов
def bread(func):
    def wrapper():
        result = func()
        return "Bread\n" + result + "Bread"
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

# Исходная функция, которая возвращает пустую строку
@bread
@meat
@tomato
@salat
def make_sandwich():
    return ""

# Вывод результата
print(make_sandwich())
