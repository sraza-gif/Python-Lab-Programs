# Program to calculate factorial and check prime number

n = int(input("Enter a number: "))

# Factorial
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    print("Factorial of", n, "is", factorial)


# Prime number checking
if n <= 1:
    print(n, "is not a prime number.")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")