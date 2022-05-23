
def make_pizza(size, *toppings):
    print("\nMaking a "+str(size)+"-inch pizza with following toppings: ")
    for topping in toppings:
        print('- ' + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom','green peppers','extra cheese')
