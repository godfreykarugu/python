'''

car ={
    "brand": input("The  is your brand? "),
    "model": input("Enter the model name "),
    "year": int(input("Enter the year of manufacture ")),
    "color": input("Enter the color "),
    "cost": float(input("Enter the cost "))
}
print('-------------------------------------------')
print("The car brand is: ",car['brand'])
print("The car model is: ",car['model'])
print("The car year of manufacture is: ",car['year'])
print("The Cost of the car",car['cost'])

print('-------------------------------------------')
print(car.keys())

'''

vehicle = {
    "brand": "Ford",
    "model": "Mustang",
    "color": "Red"
}
#print(vehicle)
# print(vehicle.keys())
# print(vehicle.items())
# print(vehicle.values())

vehicle['year']= '2016'

print(vehicle)