"""lambda functions"""

"""Example 1: Lambda Function with List Comprehension"""
# function takes 0 argument
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# for item in is_even_list:
#     print(item())

test_list = [lambda arg=1: arg * 10, lambda arg=2: arg * 10, lambda arg=3: arg * 10]

# for x in test_list:
#     print(x())

test_item = lambda arg=1: arg * 10
# print(test_item())

"""Example 2: Lambda Function with if-else"""
max_value = lambda a, b: a if (a > b) else b

# print(max_value(1, 2))

"""Example 3: Lambda with Multiple statements"""
num_list = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# test = [1, 2, 3]
# print(sorted(test, reverse=True))

# Sort each sublist
sort_list = lambda x: (sorted(i) for i in x)
# print(sort_list(num_list))

second_largest = lambda y, z: [x[len(x)-2] for x in y(z)]
result = second_largest(sort_list, num_list)
# print(result)

"""Example 4: Lambda with with filter()"""
# The filter() function returns an iterator were the items are filtered through
# a function to test if the item is accepted or not.
list1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list1 = list(filter(lambda x: (x % 2 != 0), list1))
# print(final_list1)

ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age > 18, ages))
# print(adults)

"""Example 5: Lambda with with map()"""
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
list2 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list2 = list(map(lambda x: x * 2, list2))
# print(final_list2)

animals = ["dog", "cat", "parrot", "rabbit"]

uppered_animals = list(map(lambda animal: animal.upper(), animals))
# print(uppered_animals)

"""Example 5: Lambda with with reduce()"""
# The reduce() function is used to apply a particular function passed in its argument
# to all of the list elements mentioned in the sequence passed along.
# 1. first two elements of sequence are picked and the result is obtained.
# 2. apply the same function to the previously attained result and the number
# just succeeding the second element and the result is again stored.
# 3. This process continues till no more elements are left in the container.
from functools import reduce

list3 = [5, 8, 10, 20, 50, 100]
sum_list = reduce((lambda x, y: x + y), list3)
# print(sum_list)

lis = [1, 3, 5, 6, 2]


max_num = reduce(lambda a, b: a if a > b else b, lis)
# print(max_num)

