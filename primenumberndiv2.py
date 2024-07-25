def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, n // 2 + 1))
num = int(input( ))
print(f"{num} is {'prime' if is_prime(num) else 'not prime'}.")
