
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) +' '+ self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

new_car = Car('audi','a4','2016')
print(new_car.get_descriptive_name())
new_car.read_odometer()

#new_car.odometer_reading = 23
#new_car.read_odometer()

new_car.update_odometer(25)
new_car.read_odometer()
#new_car.update_odometer(21)

new_car.increment_odometer(100)
new_car.read_odometer()
