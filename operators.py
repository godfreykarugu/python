#
# maths = 70
# english = 60
# phy = 75
#
#
# av = (maths+english+phy)/3
#
# print(av)

# --------------------nested if statement----------------------------------------------------
# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         if int(age) >= 18:
#             print("You are eligible to vote")
#             break
#         else:
#             print("You are not eligible to vote")
#             break
#     else:
#         print("Enter a valid digit")

#----------------------------------------------------------------------------

# -------------- if--elif --------------------------------------------------
# num = -67
#
# if num > 0:
#     print(num,"is positive")
# elif num < 0:
#     print(num,"is negative")
# else:
#     print(num,"is Zero")

# ------------------- odd or even number ------------------------------------

# num = int(input('Enter a number: '))
# if num % 2 ==1:
#     print(num,'is an ODD number')
# else:
#     print(num,'is an EVEN number')


# math=60
# english=28
# kisw=4
# geo=76
# hist=55
#
# sum=math+english+kisw+geo+hist
# average=sum/5
# if average>=70 & average<=100:
#     print("Grade:A ")
# elif average>=60 & average<=69:
#     print("Grade: B")
# elif average>=50 & average<=59:
#     print("Grade:C")
# elif average>=40 & average<=49:
#     print("Grade:D")
# elif average>=0 & average<=39:
#     print("Grade:F")
# else:
#     print("Ivalid Marks")


# ---------------- capturing marks from the user ..........................
sum=0                                                  # initialize sum to 0

subjects = int(input("Enter the number of subjects: ")) # ask user for the number of subjects
for i in range(0,subjects):                              # repeat capturing marks and add to sum till all subjects captured
    marks=float(input("Enter the Marks for subject: "))
    sum= sum + marks
average= sum/subjects                                       # determine average
print("The Total is: ",sum)                                 # print the sum
print("The average is: ",average)                           # print the average
if average>=70 & average<=100:                              # use if statement to determine the grade
    print("Grade:A ")
elif average>=60 & average<=69:
    print("Grade: B")
elif average>=50 & average<=59:
    print("Grade:C")
elif average>=40 & average<=49:
    print("Grade:D")
elif average>=0 & average<=39:
    print("Grade:F")
else:
    print("Ivalid Marks")