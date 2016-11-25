def division(num1, num2):
    """Return num1/num2"""
    return num1/num2

try:
    print(division(10,0))
except ZeroDivisionError:
    print("You can't divide by zero")

class Base(Exception):
    """Base class"""
    pass

class Derived(Base):
    """Inherits from Base class"""
    pass

for to_raise in [Base,Derived]:
    try:
        raise to_raise()
    except Derived:
        print("Derived class")
    except Base:
        print("Base class")

for to_raise in [Base,Derived]:
    try:
        raise to_raise()
    except Base:
        print("Base class")
    except Derived:
        print("Derived class")

try:
    raise Exception("An exception occurred")
except:
    print("All exceptions are caught here")

try:
    raise Exception('arg1', 'arg2')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x,y = inst.args
    print("x = {} y = {}".format(x,y))

class Error(Exception):
    """Base class for all exceptions in the module"""
    name = "exceptions.py"

class FirstError(Error):
    """Specific exception class inherits from Error"""
    
    def __init__(self,message):
        self.message = message

try:
    raise FirstError("First custom exception")
except FirstError as custom_exception:
    print("FirstError has been raise with message: ",custom_exception.message, "\ncurrent module: ", custom_exception.name)

def proper_divide(x,y):
    """Returns x/y and handles exceptions"""
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division by zero handled")
    else:
        print("Result is ", result)
    finally:
        print("This is always executed")

proper_divide(10,5)
proper_divide(10,0)