#Task 1: Check if a Number is Even or Odd

try:
    n = int(input('Enter the Test Number:'))
    if n%2 == 0:
         print(f'{n} is an Even number')
    else:
         print(f'{n} is an Odd number')
except:
    print('Error: Enter the valid input')