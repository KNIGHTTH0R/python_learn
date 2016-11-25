num=42
if num>0:
    print('postive number')
elif num==0:
    print('Zero')
else:
    print('negative number')

print('while example')
counter=10
while counter>0:
    print(counter)
    counter-=1
print('Blast off')

print('for example 1')
values=[11,12,34,46]
for i in values:
    print(i)

print('for example 2')
for i in range(6):
    print(i)

print('continue example')
for i in range(10):
    if(i%2==0):
        continue
    print(i)

print('break example')
for i in range(10):
    if(i==6):
        break
    print(i)

print('pass example')
for i in range(10):
    pass
    print(i)
    pass