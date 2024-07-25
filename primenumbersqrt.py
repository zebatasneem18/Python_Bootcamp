import math
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


num = int(input())
print(f"{num} is {'a prime number.' if is_prime(num) else 'not a prime number.'}")