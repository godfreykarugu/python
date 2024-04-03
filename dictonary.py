person={
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "city": input("Enter your city: ")
    }
print("Hello ",person["name"])
print("Confirm that you are",person["age"]," years old")
print("and a resident of ",person["city"])

print('--------------------------------------------------')

monthConversion = {
    'January': 31,
    'February': 28,
    'March':    31,
    'April':    30,
    'May': 31,
    'June': 30,
    'July':    31,
    'August':    31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
 }

print(monthConversion.get('January'))