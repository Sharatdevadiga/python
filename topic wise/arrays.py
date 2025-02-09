#  called lists in python
arr = [1,2,3,4,]
print(arr)

# can be used as stack
arr.append(0)
print(arr.pop())
print(arr)

# O(n)
arr.insert(1, 7)
arr.insert(2, 4)
arr.insert(3, 8)

arr[0] = 4
arr[2] = 5
arr[3] = 10
arr[4] = 12

n = 5
arr = [0] * n
print(arr[-1])
print(arr[-3])
print(arr[-2])


# slicing the array
print(arr[1:3])
print(arr[2: 4])
print(arr[2:4])

# unpacking
a,b,c = [1,2,3]
print(a,b,c)

arr = [1,2,3,4,4,5]
for i in range(len(arr)):
    print(arr[i])

nums = [1,2,3,4,5,5]
for n in nums:
    print(n)

for i, n in enumerate(nums):
    print(n, i)

arr = [1,2,3,4,5]

for i in range(len(arr)): print(arr[i])
for n in arr: print(n)
for i, n in enumerate(arr): print(n, i)

nums1 = [1,2,3,4, 4]
nums2 = [2,3,4,5,6]

for n1,n2 in zip(nums1, nums2):
    print(n1, n2)

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
nums.reverse()
print(nums)
nums.sort()
print(nums)

nums.sort(reverse = True)

arr = ["bob", "alice", "charlie", "done"]
arr.sort(arr)
print(arr)

arr.sort(key = lambda x: len(x))
arr.sort(key = lambda x: len(x))
arr.sort(key = lambda x: len(x))
arr.sort(key = lambda x: len(x))
arr.sort(key = lambda x: len(x))


# list comprehension

arr = [i for i in range(5)]
arr2 = [i for i in range(10)]
arr3 = [i for i in range(0, 20, 2)]
arr4 = [i + i for i in range(5)]


# 2 d list
arr = [[0] * 4 for i in range(4)]
print(arr)

arr = [[0] * 4 for i in range(4)]
print(arr)


arr2 = [[0] * 4 for i in range(5)]
print(arr2)


