n = float(input('Enter the number: '))

if n>0:
    import math
    print(f'Square root of {n} =',math.sqrt(n))
    print(f'Natural log of {n} =',math.log(n,math.e))
    print(f'Sine of {n} =',math.sin(n))
else:
    print('Enter the positive value')
