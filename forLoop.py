test_list = [10, 15, 20, 7, 46, 2808]
sum=0
for i in test_list:
    sum += i
print('The sum is ',sum)

print('------------Nested loop------------')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print('------------exponential function using for loop------------')

base_num=int(input('Enter the base number: '))
exp_num=int(input('Enter the exponent: '))

def exponential(base_num,exp_num):
    result=1
    for num in range(exp_num):
        result=result * base_num
    return result
print("The power is ", exponential(base_num,exp_num))
