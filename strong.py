def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

num = 145
sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))

print(f"{num} is a strong number." if sum_of_factorials == num else f"{num} is not a strong number.")
