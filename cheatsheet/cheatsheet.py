# Dynamic language
n = 0
print(n)

n = 10
print(n)

n = 'abc'
print(n)

# Multiple assignment
a, b, n = 10, 20, 5

# Increment
n = n + 1
n += 1

# Decrement
n = n - 1
n -= 1

# Null
n = 4
n = None
print(n)

# If statement
n = 20
if n > 5:
    print('n is greater than 5')

# If-else statement
if n > 5:
    print('n is greater than 5')
else:
    print('n is less than or equal to 5')

# If-elif-else statement
if n > 5:
    print('n is greater than 5')
elif n <= 2:
    print('n is less than or equal to 2')
else:
    print('n is between 2 and 5')

# Parenthesis for multiline conditional
if (n > 2 and n < 10 or n < 10 and n > 2):
    print('n is between 2 and 10')

# While loop
n = 0
while n < 5:
    print(n)
    n += 1

# For loop
for i in range(5):
    print(i)

for i in range(10, 15):
    print(i)

for i in range(10, 20, 2):
    print(i)

for i in range(20, 10, -1):
    print(i)

for i in range(20, 10, -2):
    print(i)

# Division
print(5 / 2)
print(4 // 2)

print(n // 2)
print(n / 2)
print(int(-3 / 2))
print(int(-10 / 3))

print(10 % 3)
print(-10 % 3)

import math
print(math.fmod(-10, 3))
print(math.fmod(-10, 3))

print(math.floor(10 / 3))
print(math.ceil(10 / 3))
print(math.sqrt(2))
print(math.pow(3, 4))

print(float("inf"))
print(float("-inf"))

print(math.pow(2, 200))
print(math.pow(2, 200) < float('inf'))

# Arrays (lists)
arr = [1, 2, 3]
print(arr)

arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

popped = arr.pop()
print(popped)

arr.insert(1, 6)
print(arr)

arr[0] = 0
print(arr)

n = 5
arr = [1] * 5
print(arr)

n = 10
arr2 = [2] * n
print(arr2)
print(len(arr2))

arr = [1, 2, 3]
print(arr[-1])
print(arr[-2])
print(arr[-3])

print(arr[1:2])
print(arr[2:4])
print(arr[1:3])

a, b, c = [1, 2, 3]
print(a, b, c)

nums = [1, 2, 3, 4]
for i in range(len(nums)):
    print(nums[i])

for i in nums:
    print(i)

for i, n in enumerate(nums):
    print(i, n)

# List operations: append, pop, insert, len, enumerate

nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)

arr = [3, 4, 2, 6, 5, 7]
arr.sort()
arr.sort(reverse=True)

arr = ["abc", "def", "ghi"]
arr.sort()

# Lambda function
arr.sort(key=lambda x: len(x))
arr.sort(key=lambda x: len(x), reverse=True)
arr.sort(key=lambda x: len(x))

arr = [i for i in range(5)]
print(arr)

arr2 = [i + i for i in range(5)]

arr = [[0] * 5 for i in range(5)]
arr = [[0] * 5 for i in range(6)]
print(arr)

# String operations
s = 'abderc'
print(s)
print(s[0:2])
print(s[1:2])

s += 'def'
print(s)

print(int("123") + int("345"))
print(str(123) + str(456))

print(ord('a'))
print(ord('b'))

str_list = ['ab', 'cd', 'ef']
print("".join(str_list))

str2 = ['ab', 'cd', 'ef']
print("-".join(str2))

# Queue in Python
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
queue.pop()
print(queue)

queue = deque()
queue.append(5)
queue.appendleft(6)
queue.pop()
queue.popleft()

# HashSet
s = set()
s.add(3)
s.add(1)
print(s)
print(len(s))

print(1 in s)
print(2 in s)

s.remove(1)
print(2 in s)

print(set([1, 2, 2, 1, 3, 4]))

myset = {i for i in range(5)}
print(myset)

# HashMap (dictionary)
map = {}
map['a'] = 1
map['b'] = 2
print(map)
print(len(map))

map['a'] = 5
print(map)

print('a' in map)
print('c' in map)
print(map)

print(map.pop('a'))
print('a' in map)

map = {
    'a': 1,
    'b': 2,
    'c': 3
}

map = {i: 2 * i for i in range(3)}
print(map)

map = {i: 2 * i for i in range(5)}
print(map)

for key in map:
    print(key, map[key])

for val in map.values():
    print(val)

for key, val in map.items():
    print(key, val)

# Tuples
tup = (1, 2, 3)
# tup[0]  # This will raise an error because tuples are immutable

tup = {
    (1, 2): 3
}

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

# Lists can't be keys in a dictionary, but tuples can be keys in a dictionary

# Heaps
import heapq

# Under the hood heaps are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 1)

print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -1)

print(-maxHeap[0])

while len(maxHeap):
    print(-heapq.heappop(maxHeap))

arr = [1, 2, 4, 3, 6, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

# Functions
def func(n, m):
    return n * m

print(func(3, 4))

def outer(a, b):
    def inner(c, d):
        return c * d
    
    print(inner(a, b))

outer(3, 5)

def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2

        nonlocal val
        val *= 2
    
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)

# Classes
class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

class MyClass2:
    def __init__(self, number):
        self.number = number

    def getLength(self):
        return len(self.number)

    def getDoubleLength(self):
        return 2 * self.getLength()

obj = MyClass2([1, 2, 3])
print(obj.getLength())
print(obj.getDoubleLength())