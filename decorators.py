def my_decorator(func):
    def inner():
        print("Decoration before function call")
        func()
        print("Decoration after function call")

    return inner

@my_decorator
def simple_print():
    print("Hello from simple_print")

simple_print()
print()

def check_valid_division(func):
    def inner(a,b):
        if b == 0:
            print("Division by zero is not allowed")
        else:
            func(a,b)
    
    return inner

@check_valid_division
def divide(a, b):
    print(a/b)

divide(10,5)
print()
divide(10,0)
print()

def print_star(func):
    def inner(val):
        print("*" * 20)
        func(val)
        print("*" * 20)
    
    return inner

def print_percent(func):
    def inner(val):
        print("%" * 20)
        func(val)
        print("%" * 20)
    
    return inner

@print_star
@print_percent
def fancy_print(val):
    print(val)

fancy_print("Hello World")
print()

@print_percent
@print_star
def fancy_print_different(val):
    print(val)

fancy_print_different("Different decoration")