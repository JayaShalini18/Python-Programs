def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

number = int(input("Enter an integer: "))

if number % 2 == 1:  
    fact = factorial(number)
    fact_digits = len(str(fact))
    is_palindrome=is_palindrome(number)
    print("Factorial:", fact)
    print("Number of digits in factorial:", fact_digits)
    print("Is the number palindrome?",is_palindrome)
else:
        print("The number is not odd")

