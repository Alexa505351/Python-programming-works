"""Task 1"""

a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
count_5 = 0
for item in a:
    if item == 5:
        count_5 += 1
print(f"Кол-во цифр 5 при первом объединении: {count_5}")
i = 0
while i < len(a):
    if a[i] == 5:
        a.pop(i)
    else:
        i += 1

a.extend(c)
count_3 = 0
for item in a:
    if item == 3:
        count_3 += 1
print(f"Кол-во цифр 3 при втором объединении: {count_3}")

print(f"Итоговый список: {a}")


"""TAsk 2"""

def merge_sorted_lists(list1: list, list2: list) -> list:
    merged_set = set(list1) | set(list2)
    return sorted(merged_set)

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

"""Task 3"""

def process_parts(shop: list, part_name: str) -> tuple:
    filtered = [price for name, price in shop if name == part_name]
    
    return len(filtered), sum(filtered)
shop = [
    ['каретка', 1200],
    ['шатун', 1000],
    ['седло', 300],
    ['педаль', 100],
    ['седло', 1500],
    ['рама', 12000],
    ['обод', 2000],
    ['шатун', 200],
    ['седло', 2700]
]

part_name = input("Название детали: ")
count, total_cost = process_parts(shop, part_name)

print(f"Кол-во деталей — {count}")
print(f"Общая стоимость — {total_cost}")


"""Task 4"""

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
MAX_GUESTS = 6

while True:
    print(f"\nСейчас на вечеринке {len(guests)} человек:")
    for i, guest in enumerate(guests, 1):
        print(f"  {i}. {guest}")
    
    action = input("\nГость пришёл или ушёл? ")
    
    if action == "Пора спать":
        print("\nВечеринка закончилась, все легли спать.")
        break
    
    name = input("Имя гостя: ")
    
    if action == "пришёл":
        if len(guests) < MAX_GUESTS:
            if name not in guests:
                guests.append(name)
                print(f"Привет, {name}!")
            else:
                print(f"{name} уже здесь!")
        else:
            print(f"Прости, {name}, но мест нет.")
    
    elif action == "ушёл":
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"{name} не найден(а) в списке гостей.")


"""Task 5"""

songs = [
    ["Мир в моих глазах", 4.86],
    ["Сладчайшее совершенство", 4.43],
    ["Личный Иисус", 4.56],
    ["Ореол", 4.9],
    ["В ожидании ночи", 6.07],
    ["Наслаждайся тишиной", 4.20],
    ["Политика истины", 4.76],
    ["Синее платье", 4.29],
    ["Чистый", 5.83]
]

n = int(input("Сколько песен выбрать? "))

total_time = 0
for i in range(1, n + 1):
    song_name = input(f"Название {i}-й песни: ")
    found = False
    for song in songs:
        if song[0].lower() == song_name.lower():
            total_time += song[1]
            found = True
            break
    if not found:
        print(f"Ошибка: песня '{song_name}' не найдена в списке")
        total_time = None
        break
if total_time is not None:
    print(f"Общее время звучания песен: {total_time} минуты")



"""Task 6"""

n = int(input("Кол-во коньков: "))
skates = [int(input(f"Размер {i+1}-й пары: ")) for i in range(n)]
k = int(input("\nКол-во людей: "))
feet = [int(input(f"Размер ноги {i+1}-го человека: ")) for i in range(k)]
skates.sort()
feet.sort()

count = 0
i = j = 0

while i < len(skates) and j < len(feet):
    if skates[i] >= feet[j]:
        count += 1
        i += 1
        j += 1
    else:
        i += 1

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {count}")



"""Task 7"""

def josephus_simulation(n: int, k: int) -> int:
    people = list(range(1, n + 1))
    current_index = 0
    
    print(f"Текущий круг людей: {people}")
    print(f"Начало счёта с номера {people[current_index]}")
    while len(people) > 1:
        remove_index = (current_index + k - 1) % len(people)
        print(f"Выбывает человек под номером {people[remove_index]}")
        people.pop(remove_index)
        current_index = remove_index % len(people) if people else 0
        if len(people) > 1:
            print(f"\nТекущий круг людей: {people}")
            print(f"Начало счёта с номера {people[current_index]}")
    
    print(f"\nОстался человек под номером {people[0]}")
    return people[0]

if __name__ == "__main__":
    n = int(input("Кол-во человек: "))
    k = int(input("Какое число в считалке? "))
    
    print(f"\nЗначит, выбывает каждый {k}-й человек\n")
    
    result = josephus_simulation(n, k)


"""Task 8"""

def find_symmetric_extension(sequence: list) -> tuple:
    n = len(sequence)
    for i in range(n):
        is_palindrome = True
        left = i
        right = n - 1
        
        while left < right:
            if sequence[left] != sequence[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1
        
        if is_palindrome:
            numbers_to_add = sequence[:i][::-1]
            return len(numbers_to_add), numbers_to_add
    return 0, []

if __name__ == "__main__":
    n = int(input("Кол-во чисел: "))
    
    sequence = []
    for i in range(n):
        num = int(input(f"Число: "))
        sequence.append(num)
        
    
    print(f"\nПоследовательность: {sequence}")
    count, numbers = find_symmetric_extension(sequence)
    
    print(f"Нужно приписать чисел: {count}")
    print(f"Сами числа: {numbers}")
print(merge_sorted_lists(list1, list2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
