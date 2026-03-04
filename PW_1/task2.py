# варіант 3
import math


def is_prime (n):
    if n < 2:
        return False
    counter = 0
    max_d = int(math.sqrt(n))
    i = 2
    while i <= max_d:
        if n % i == 0:
            counter += 1
            break
        i+=1
    if counter > 0:
        return False
    else:
        return True

print(is_prime(10))
print(is_prime(11))
print(is_prime(100))
print(is_prime(17))
print(is_prime(13))
print(is_prime(256))
print(is_prime(257))
print(is_prime(49))

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"The number {num} is prime")
else:
    print(f"The number {num} is not prime")