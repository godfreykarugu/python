'''
1. print out the total items in the list
2. print out the third and fourth last values in the same list
3. Replace the 3rd item in the list with "MIT"
4. Remove the first item from list
'''


students= ['Mike', 'John', 'Erick', 'David', 'Jane','Sharon','Misheck']
print(len(students))   # 1
print(students [4:6])   # 2

students[2]= 'MIT'      # 3
print(students[-4:-2])   # print the fourth and the third last items in the list
students.pop(0)          # 4

print(students)

#................. list operations ..................................

'''fruits= ['mangoes', 'apples', 'bananas', 'pasion','melon']
print(fruits)
print(fruits[0])
print(len(fruits))

fruits[0] = 'bananas'
print(fruits)

fruits.append('kiwi')
print(fruits)
fruits.insert(2, 'pineaple')
print(fruits)
fruits.remove('bananas')  # remove the first occurence of the item
print(fruits)
fruits.pop()             # removes the last item in the list
print(fruits)
fruits.pop(3)             # remove the item in the specified index
print(fruits)
fruits.clear()            # removes all the items in the list
print(fruits)
fruits = ['mangoes', 'apples', 'pinapples', 'melon']
#print(fruits) '''


#............This has a logical error, it's not executing the else part

'''fruits = ['mangoes', 'apples', 'pinapples', 'melon']
if 'apples' in fruits:
    fruits.remove('apples')
    print(fruits)
else:
    print('there were no apples in the list') '''

#............................ testing the same concept

num = 2

if num >= 18:
    num = num + 1
    print('Have added 1 to the old value')
    print('New value is', num)
else:
    print('No divide given')


