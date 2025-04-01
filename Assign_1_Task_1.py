# Perform Basic Mathematical Operations
a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
print('Addition =', a+b)
print('Subtraction =', a-b)
print('Multiplication =', a*b)
try:
    print('Division =', a/b)
except:
    print('Division = Error: Division by zero is not allowed')
