myset1=set()
print(myset1)

myset2=set('aaabbcc')
print(myset2)

myset3={'python','java','c#','php'}
print(myset3)

print('python' in myset3)

print(len(myset3))

myset4={'python','c++'}

print(myset3.intersection(myset4))

print(myset3.difference(myset4))

print(myset3.union(myset4))

myset4.add('lisp')
print(myset4)
myset4.remove('c++')
print(myset4)

print(myset3==myset4)