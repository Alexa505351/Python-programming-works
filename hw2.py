"""Task 1"""
'''def get_odd_numbers(n: int) -> list:
    return list(range(1, n + 1, 2))
if __name__ == "__main__":
    n = int(input("Введите число: "))
    
    result = get_odd_numbers(n)
    print(f"Список из нечётных чисел от одного до N: {result}")

"""Task 2"""
def get_even_index_elements(names: list) -> list:
    result = []
    for i in range(len(names)):
        if i % 2 == 0:
            result.append(names[i])
    
    return result
if __name__ == "__main__":
    participants = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    
    first_day = get_even_index_elements(participants)
    
    print(f"Первый день: {first_day}")


"""Task 3"""
def remove_largest_elements(cards: list) -> list:
    if not cards:
        return []
    max_value = max(cards)
    result = []
    for card in cards:
        if card != max_value:
            result.append(card)
    
    return result

if __name__ == "__main__":
    n = int(input("Количество видеокарт: "))
    
    video_cards = []
    for i in range(1, n + 1):
        card = int(input(f"{i} Видеокарта: "))
        video_cards.append(card)
    
    print(f"\nСтарый список видеокарт: {video_cards}")
    
    new_video_cards = remove_largest_elements(video_cards)


"""Task 4"""
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorites = []
count = int(input("Сколько фильмов хотите добавить? "))
added = 0

while added < count:
    film = input("Введите название фильма: ")
    
    if film in films:
        if film not in favorites:  
            favorites.append(film)
            added += 1
        else:
            print(f"Фильм {film} уже есть в вашем списке любимых")
            
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")

if favorites:
    print(f"Ваш список любимых фильмов: {', '.join(favorites)}")
else:
    print("Вы не добавили ни одного фильма в список любимых")


"""Task 5"""

def find_position(containers: list, new_weight: int) -> int:
    for i in range(len(containers)):
        if new_weight >= containers[i]:
            return i + 1
    return len(containers) + 1

if __name__ == "__main__":
    n = int(input("Количество контейнеров: "))
    containers = []
    for i in range(n):
        weight = int(input(f"Введите вес контейнера {i+1}: "))
        containers.append(weight)
    new_weight = int(input("\nВведите вес нового контейнера: "))
    position = find_position(containers, new_weight)
    print(f"\nНомер, который получит новый контейнер: {position}")
    
    print(f"Новый список видеокарт: {new_video_cards}")



"""Task 6"""

def rotate_right(lst: list, k: int) -> list:
    if not lst:
        return lst
    
    n = len(lst)
    k = k % n
    
    if k == 0:
        return lst.copy()

    lst = lst[::-1]
    
    lst = lst[:k][::-1] + lst[k:]
    
    lst = lst[:k] + lst[k:][::-1]
    
    return lst

if __name__ == "__main__":
    k = int(input("Сдвиг: "))
    input_str = input("Изначальный список: ")
    if input_str.startswith('[') and input_str.endswith(']'):
        input_str = input_str[1:-1]
    
    if input_str.strip():
        original = [int(x.strip()) for x in input_str.split(',')]
    else:
        original = []
    result = rotate_right(original, k)
    print(f"Сдвинутый список: {result}")'''

"""Task 7"""

def is_palindrome(word: str, case_sensitive: bool = False) -> dict:
    original = word
    
    if not case_sensitive:
        word = word.lower()
    
    is_pal = word == word[::-1]
    
    result = {
        "word": original,
        "is_palindrome": is_pal,
        "length": len(original),
        "reversed": original[::-1] if not case_sensitive else word[::-1]
    }
    return result

if __name__ == "__main__":
    while True:
        word = input("\nВведите слово (или 'выход' для завершения): ")
        
        if word.lower() == 'выход':
            print("Программа завершена")
            break
        
        if not word:
            print("Пожалуйста, введите слово")
            continue
        
        result = is_palindrome(word)
        
        if result["is_palindrome"]:
            print(f"Слово '{result['word']}' является палиндромом")
            print(f"Длина слова: {result['length']}")
        else:
            print(f"Слово '{result['word']}' не является палиндромом")
            print(f"Обратное слово: {result['reversed']}")


"""Task 8"""

def quick_sort(arr: list, left: int, right: int) -> None:
    if left >= right:
        return
    
    pivot = arr[(left + right) // 2]
    i, j = left, right
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    quick_sort(arr, left, j)
    quick_sort(arr, i, right)

if __name__ == "__main__":
    input_str = input("Изначальный список: ")
    if input_str.startswith('[') and input_str.endswith(']'):
        input_str = input_str[1:-1]
    
    if input_str.strip():
        arr = [int(x.strip()) for x in input_str.split(',')]
    else:
        arr = []
    quick_sort(arr, 0, len(arr) - 1)
    
    print(f"Отсортированный список: {arr}")


"""Task 9"""

results = [int(x) for x in input("Введите список чисел: ").split()]

print("Чётные числа в обратном порядке:", end=" ")

for i in range(len(results) - 1, -1, -1):
    if results[i] % 2 == 0:
        print(results[i], end=" ")

print() 

