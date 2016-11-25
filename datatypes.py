import sys

print('Initialize var=10')
var=10
print(var)
print('Assigning var=\'string\'')
var='string'
print(var)

if not bool(()):
	print('() is falsey')
if not bool([]):
	print('[] is falsey')
if not bool({}):
	print('{} is falsey')
if not bool(''):
	print('\'\' is falsey')
if not bool(None):
	print('None is falsey')

print('Check type of variable with type(\'value\') Eg-type(\'0\')')
print(type(0))

print('Max value of float: sys.float_info.max')
print(sys.float_info.max)

#single line comment
