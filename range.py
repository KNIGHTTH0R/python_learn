#range(stop)
r1=range(10)
print(list(r1))

#range(start,stop)
r2=range(2,10)
print(list(r2))

#range(start,stop,step)
r3=range(10,20,2)
print(list(r3))

#negative step value
r4=range(30,10,-5)
print(list(r4)) 

r5=range(10,20)
print(15 in r5)
print(25 in r5)

print(range(0,4,2)==range(0,3,2))
print(range(10)!=range(20))
