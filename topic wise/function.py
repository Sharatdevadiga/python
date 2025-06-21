def func(n, m):
    print(n, m)
    return n * m

# nested functions
def outer(a, b):
    c = "c"

    def inner(c, d):
        return a + b + c + d

    return inner

print(outer("a", "b")("c", "d"))

# nonlocal keyword
def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        nonlocal val
        val *= 2
    
    helper()
    print(arr, val)

nums = [1,2]
val = 3
double(nums, val)