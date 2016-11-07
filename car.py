class Car(object):
    """docstring for Car"""
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 15
        else:
            self.tax = 12
        self.displayAll()
    def displayAll(self):
        print "The price is " + str(self.price) + "."
        print "It goes " + str(self.speed) + "mph."
        print "The fuel tank is " + str(self.fuel) + "."
        print "It's mileage is " + str(self.mileage) + "mpg."
        print "The tax is " + str(self.tax) + "%.\n"

car1 = Car(2000, 35, "full", 15)
car2 = Car(2000, 5, "not full", 105)
car3 = Car(2000, 15, "kinda full", 95)
car4 = Car(2000, 25, "full", 25)
car5 = Car(2000, 45, "empty", 25)
car6 = Car(20000000, 35, "empty", 15)

