'''
def say_hello(name):
    print("Hello " + name + "!")

say_hello("John")
say_hello("Smith")
'''

'''
def cube(num):
    return num * num * num

print(cube(4))
'''

# logical or operator

'''
is_male =False
is_Tall = False

if is_male or is_Tall:
    print("Male or Tall")
else:
    print("Neither Male nor Tall")
'''
# logical and operator

''' 
is_male =True
is_Tall = True

if is_male and is_Tall:
    print("Male and Tall")
else:
    print("Either Not Male or Not Tall or Neither Male nor Tall")
'''

# if--elif

is_male =True
is_Tall = False

if is_male and is_Tall:
    print("Male and Tall")
elif is_male and not(is_Tall):
    print("Male but not Tall")
elif not(is_male) and is_Tall:
    print("Not Male but Tall")
else:
    print("Either Not Male or Not Tall or Neither Male nor Tall")
