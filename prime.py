number = int(input("Enter a number: "))
if number <= 1:
    print(f"{number} is not a prime number.")
elif number <= 3:
    print(f"{number} is a prime number.")
elif number % 2 == 0 or number % 3 == 0:
    print(f"{number} is not a prime number.")
else:
    is_prime = all(number % i != 0 for i in range(5, int(number**0.5) + 1, 6))
    print(f"{number} is a prime number." if is_prime else f"{number} is not a prime number.")

