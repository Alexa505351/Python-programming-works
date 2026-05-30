"""Task 1"""
import sys
import platform

os_name = platform.system()
python_version = sys.version

file = open("os_info.txt", "w")
file.write(f"OS info is {os_name} Python version is {python_version}")
file.close()

"""Task 2"""
def sum_of_digits(n: int) -> int:
    total = 0
    num = n
    
    while num > 0:
        total += num % 10  
        num //= 
    return total

def count_digits(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    num = n
    while num > 0:
        count += 1
        num //= 10
    return count

if __name__ == "__main__":
    n = int(input("Введите число: "))
    
    sum_digits = sum_of_digits(n)
    count_digits = count_digits(n)
    
    print(f"Сумма чисел: {sum_digits}")
    print(f"Количество цифр в числе: {count_digits}")
    
"""Task 3"""

def find_minimal_divisor(n: int) -> int:
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return divisor
    return n

if __name__ == "__main__":
    n = int(input("Введите число: "))
    
    if n <= 1:
        print("Число должно быть больше 1")
    else:
        minimal_divisor = find_minimal_divisor(n)
        print(f"Наименьший делитель, отличный от единицы: {minimal_divisor}")
    print(f"Разность суммы и количества цифр: {sum_digits - count_digits}")

