''' simple try-except block'''

try:
    num = int(input('Enter a number: '))
    print(num)
except:
    print('Invalid input')

''' multiple errors same except block-----'''

try:
    num = int(input('Enter a number: '))
    num2 = num / 0
except ZeroDivisionError as err:
    print(err)
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)