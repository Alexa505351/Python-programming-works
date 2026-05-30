"""Task 1"""

def extract_vowels(text: str) -> list:
    vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
    vowels_list = [char for char in text if char in vowels]
    
    return vowels_list
if __name__ == "__main__":
    text = input("Введите текст: ")
    
    vowels = extract_vowels(text)
    
    print(f"\nСписок гласных букв: {vowels}")
    print(f"Длина списка: {len(vowels)}")


"""Task 2"""

def generate_list(n: int) -> list:
    result = []
    
    for i in range(n):
        if i % 2 == 0:
            result.append(1)
        else:       
            result.append((i + 1) % 5)
    
    return result

if __name__ == "__main__":
    n = int(input("Введите длину списка: "))
    
    result = generate_list(n)

"""Task 3"""

import random

def generate_team(size: int = 20, min_score: float = 5.0, max_score: float = 10.0) -> list:
    return [round(random.uniform(min_score, max_score), 2) for _ in range(size)]


def get_winners(team1: list, team2: list) -> list:
    winners = []
    
    for score1, score2 in zip(team1, team2):
        if score1 >= score2:
            winners.append(score1)
        else:
            winners.append(score2)
    
    return winners

if __name__ == "__main__":
    random.seed(42)     
    team1 = generate_team()
    team2 = generate_team()
    winners = get_winners(team1, team2)
    print(f"Первая команда: {team1}")
    print(f"Вторая команда: {team2}")
    print(f"Победители тура: {winners}")


"""Task 4 """

alphabet = 'abcdefg'

print("1:", alphabet[:])
print("2:", alphabet[::-1])
print("3:", alphabet[::2])
print("4:", alphabet[1::2])
print("5:", alphabet[:2])
print("6:", alphabet[:-2:-1])
print("7:", alphabet[3:4])
print("8:", alphabet[-3:])
print("9:", alphabet[3:5])
print("10:", alphabet[4:2:-1])

"""Task 5"""

def reverse_between_h(text: str) -> str:
    
    first_h = text.find('h')
    last_h = text.rfind('h')

    between = text[first_h + 1:last_h]

    reversed_between = between[::-1]
    
    return reversed_between

if __name__ == "__main__":
    text = input("Введите строку: ")
    
    result = reverse_between_h(text)
    
    print(f"Развёрнутая последовательность между первым и последним h: {result}")


"""Task 6"""

result = [[1 + i + 4 * j for j in range(3)] for i in range(4)]

print(result)

"""Task 7"""

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
result = [num for sublist1 in nice_list for sublist2 in sublist1 for num in sublist2]
print(result)

"""Task 8"""

def caesar_cipher(text: str, shift: int) -> str:
    lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    
    result = []
    
    for char in text:
        if char in lower_alphabet:
            new_index = (lower_alphabet.index(char) + shift) % len(lower_alphabet)
            result.append(lower_alphabet[new_index])
        elif char in upper_alphabet:
            new_index = (upper_alphabet.index(char) + shift) % len(upper_alphabet)
            result.append(upper_alphabet[new_index])
        else:
            result.append(char)
    
    return ''.join(result)

if __name__ == "__main__":
    message = input("Введите сообщение: ")
    shift = int(input("Введите сдвиг: "))
    
    encrypted = caesar_cipher(message, shift)
    
    print(f"Зашифрованное сообщение: {encrypted}")
