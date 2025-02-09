# dynamically typed language
n = 0
print(n)

n = "abc"
print('n =', n)

n,m = 0, "abc";

n = n+ 1
n += 1
# n++ invalid

# None
n = 4
n = None
print('n =', n)


if n > 2:
    print('n > 2')
elif n == 2:
    print('n 2= 2')
elif n == 0:
    print('n = 0')
else:
    print('n < 2')


# and or
b, m = 1, 2
if (n > 2 and 
    m > 2 or
    n == m):
    print('n > 2 and m > 2') 


print(5 / 2)
print( 5 // 2)

print(10 / 2)
print(10 // 2)
# print( - 3 // 2) round down
print(int(-3 / 2))
print(10 % 3)
print(-10 % 3)

import math
print (math.fmod(-10, 3))
print(math.floor(10/ 3))
print(math.ceil(10 / 3))
print(math.sqrt(2))
print(math.pow(2, 3))


float("inf")
float("-inf")

print (float("Inf"))
print(float("-Inf"))

print(math.pow(2, 200) < float("Inf"))