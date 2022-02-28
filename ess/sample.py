
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

    
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 60:
    price = 10
else:
    price = 5

print("Your admission cost is $"+str(price)+".")


requested_toppings = ['mushrooms','onions','pineapple','scallion','ginger']
available_toppings = ['mushrooms','onions','scallion','garlic']

if available_toppings or requested_toppings:

    for requested_topping in requested_toppings:
        
        if requested_topping in available_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Don't have " + requested_topping+".")

else:
    print("\nToppings empty")
