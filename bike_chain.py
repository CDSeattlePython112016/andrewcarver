class Bike(object):
    """docstring for Bike"""
    def __init__(self, price, speed=20):
        print ('New bike, boi!')
        self.price = price
        self.max_speed = speed
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print 'We ridin'
        self.miles += 10
        return self
    def reverse(self):
        if self.miles > 5:
            print 'Back it up'
            self.miles -= 5
        return self

bike1 = Bike(5000, 50)
bike2 = Bike(5000, 50)
bike3 = Bike(5000, 50)

# Bike 1
bike1.ride().ride().reverse().displayInfo()

# Bike 2
bike2.ride().ride().reverse().reverse().displayInfo()

# Bike 3
bike3.reverse().reverse().reverse().displayInfo()
