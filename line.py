import sys

@profile
def to_be_profiled():
    
    my_list1 = [i**2 for i in range(50000)]

    my_list2 = (i**2 for i in range(100000, 150000))
    sum = 0
    print("my_list1 = {} bytes".format(sys.getsizeof(my_list1)))
    print("my_list2 = {} bytes".format(sys.getsizeof(my_list2)))

    for i in my_list2:
        sum += i
        my_list1.append(i)
    print(sum)


to_be_profiled()