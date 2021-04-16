def factorial(n):
    if n == 0:
        return 0
    else:
        fact = 1
        for i in range(1,n +1):
            fact *= i
        return fact

# n = int(input())
print(factorial(3))