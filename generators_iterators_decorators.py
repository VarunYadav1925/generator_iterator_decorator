# Generator

def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

# my_nums = (x*x for x in [1,2,3,4,5])

# print(list(my_nums)) 

for num in my_nums:
    print(num)

#Generators 2
def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

for item in my_gen():
    print(item)

#generator 3
def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'
my_generator()


#Iterators
nums = [7,8,9,5]


# for i in nums:
#
#     print(i)


it = iter(nums)

print(it.__next__())

print(next(it))

for i in nums:
    print(i)

#Create an iterator
# class TopTen:

#     def __init__(self):
#         self.num = 1

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.num <= 10:
#             val = self.num
#             self.num += 1

#             return val
#         else:
#             raise StopIteration


# values = TopTen()

# print(next(values))

# # print(values.__next__())
# # print(values.__next__())

# for i in values:
#     print(i)




#Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@my_decorator
def add(a, b):
    "Our add function"
    return a + b

add(1, 3)