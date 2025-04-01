#Task 1: Calculate Factorial Using a Function
n = int(input('Enter a number:'))
def factorial(n):

    if n<2:
        return 1
    else:
        return n * (factorial(n-1))

ans = factorial(n)
print(f'Factorial of {n} = ',ans)
