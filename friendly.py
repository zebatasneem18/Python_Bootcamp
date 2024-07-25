def is_friendly_number(n):
    if n <= 0:
        return False 

    # Calculate sum of proper divisors of n
    sum_divisors_n = sum(i for i in range(1, n) if n % i == 0)

    # Calculate sum of proper divisors of the sum_divisors_n
    sum_divisors_sum_n = sum(i for i in range(1, sum_divisors_n) if sum_divisors_n % i == 0)

    return sum_divisors_sum_n == n and n != sum_divisors_n
num = 120
if is_friendly_number(num):
    print(f"{num} is a friendly number.")
else:
    print(f"{num} is not a friendly number.")
