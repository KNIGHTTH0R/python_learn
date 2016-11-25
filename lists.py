mylist=[1,2,3]
print(mylist)

mylist[0]=99
print(mylist)

print(mylist[0])
print(mylist[1])
print(mylist[2])

print(99 in mylist)

list1=[1,2]
list2=[3,4]
print(list1+list2)

print(list1*3)

list3=[1,2,3,4,5]
print(list3[2:5]) #inclusive of start and excludes end

list4=[8,9,10]
for num in list4:
    print(num)

for i in range(len(list4)):
    print('Index : ',i,' ,value : ',list4[i])

