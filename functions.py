def hello_function():
    '''This is where the function documentation goes'''
    print('Hello from function')

def function_with_return():
    '''This function returns a number'''
    return 42

def function_args(arg1):
    '''Prints the argument it recieves'''
    print(arg1)

def function_default_args(arg1=42):
    '''A function with a default argument'''
    print(arg1)

def function_kwargs(name='no name', age=42):
    '''Keyword arguments demo'''
    print(name, ' ', age)

def function_positional_and_kwarg(day, month, year):
    '''Function with postional and keyword argument'''
    print(day, ' ', month, ' ', year)

def function_variable_args(*args):
    '''This function prints a variable number of arguments'''
    print(' '.join(*args))

hello_function()
print(hello_function)

return_value = function_with_return()
print(return_value)

function_args('My argument')

function_default_args(34)
function_default_args()

function_kwargs(age=34,name='my name')
function_kwargs(name='my name',age=34)

function_positional_and_kwarg(13,'November',year=2016)

variable_args1 = 'python', 'ruby', 'php'
function_variable_args(variable_args1)
variable_args2 = 'python', 'ruby', 'php', 'java'
function_variable_args(variable_args2)