a=dict(one=1,two=2)
b={'one':1,'two':2}
c=dict(zip(['one','two'],[1,2]))
d=dict([('one',1),('two',2)])
e=dict({'one':1,'two':2})
print(a==b==c==d==e)

print('Dictionary contents ',a)

print('len(a) ',len(a))
print('a[\'one\'] ',a['one'])
a['one']=11
print('Dictionary contents after a[\'one\']=11 ',a)
a['one']=1
print('a[\'one\']=1 ','one' in a)
print('1 in a ',1 in a)
print('a.get(\'three\',3) ',a.get('three',3))
print('a.keys() ',a.keys())
print('a.values() ',a.values())
print('a.pop(\'one\') ',a.pop('one'))
print('Dictionary contents ',a)

vals=a.values()
print(vals)
a['two']=22
print(vals)