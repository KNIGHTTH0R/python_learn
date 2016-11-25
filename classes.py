import copy

class Point:
    """A class to represent a point"""

    details = "Represent points"

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def __str__(self):
        return "x={} y={}".format(self.x,self.y)

    def get_sum(self):
        """Return sum of x and y components"""
        return self.x + self.y
    
    def add_point(self,to_add):
        """Update self by add x and y component of new_point"""
        self.x += to_add.x
        self.y += to_add.y

    def __add__(self,new_point):
        self.x += new_point.x
        self.y += new_point.y
        return self

def print_point(point):
    """print contents of given point"""
    print("x={} y={}".format(point.x,point.y))

point = Point(10,20)
print(point)

print(point.details)
print(point.get_sum())

new_point = Point(2,4)
print(new_point)

point.add_point(new_point)
print(point)

print_point(new_point)

copied_point = copy.copy(point)
copied_point.x = 5
copied_point.y = 5
print(point)
print(copied_point)

print(copied_point + new_point)

class Vehicle(object):
    """Represents a vehicle"""

    def __init__(self,engine_power=100):
        self.engine_power = engine_power
    
    def __str__(self):
        return "Engine power : {}HP".format(self.engine_power)
    
    def print_name(self):
        print("From vehicle")
    
class Car(Vehicle):
    """Represents a car"""

    def __init__(self,wheels=4):
        super().__init__()
        self.wheels = wheels
    
    def __str__(self):
        return "Engine power : {}HP , Wheels = {}".format(self.engine_power,self.wheels)
    
    def print_name(self):
        print("From vehicle")

car = Car()
print(car)
car.print_name()