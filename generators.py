#list comprehensions

list1 = [x**2 for x in range(10)]

print(list1)
print()

list2 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(list2)
print()

list3 = [x for x in range(10) if x%2 != 0]

print(list3)
print()

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

transposed = [[row[i] for row in matrix] for i in range(3)]

print(transposed)

print()
#iterators

class Squared:
    """Square all the numbers"""

    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        val = self.data[self.index] **2
        self.index += 1

        return val

values = Squared([1,2,3,10])

for i in values:
    print(i)

print()
#generators

def double_values(data):
    """Doubles all the values"""
    for val in data:
        yield val*2

for i in double_values([4,5,3]):
    print(i)

print()
#generator expressions

exp = sum(i for i in range(5))

print(exp)