import timeit
import cProfile
import pstats
import time
import sys

res1 = timeit.timeit('''
a = [i for i in range(50000)]
for i in a:
    pass
''', number = 100)

res2 = timeit.timeit('''
a = (i for i in range(50000))
for i in a:
    pass
''', number = 100)

print(res1)

print(res2)

def to_be_profiled():
    my_list1 = [i**2 for i in range(50000)]

    my_list2 = (i**2 for i in range(100000, 150000))

    sum = 0

    print("my_list1 = {} bytes".format(sys.getsizeof(my_list1)))
    print("my_list2 = {} bytes".format(sys.getsizeof(my_list2)))

    for i in my_list2:
        sum += i
        time.sleep(0.00001)
        my_list1.append(i)
    print(sum)

cProfile.run('to_be_profiled()', 'cprofile_results')

p = pstats.Stats('cprofile_results')
#sort by standard name
p.strip_dirs().sort_stats(-1).print_stats(10)
#sort by function name
p.sort_stats('name').print_stats(10)
#sort by cumulative time in a function
p.sort_stats('cumulative').print_stats(10)
#sort by time spent in a function
p.sort_stats('time').print_stats(10)