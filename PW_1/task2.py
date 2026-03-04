# варіант 3
import math

# Функція перевірки числа на простоту
def is_prime (n):
    # Числа <2 не є простими
    if n < 2:
        return False
    counter = 0 # Лічильник
    max_d = int(math.sqrt(n)) # Максимальний дільник
    i = 2 # Початковий дільник
    while i <= max_d: # Цикл перевірки
        if n % i == 0: # Якщо число ділиться, перериваємо цикл
            counter += 1
            break
        i+=1
    if counter > 0: # Якщо лічильник більше 0 число не є простим
        return False
    else: # Число просте
        return True

# print(is_prime(10))
# print(is_prime(11))
# print(is_prime(100))
# print(is_prime(17))
# print(is_prime(13))
# print(is_prime(256))
# print(is_prime(257))
# print(is_prime(49))

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"The number {num} is prime")
else:
    print(f"The number {num} is not prime")