myMap = {}
myMap["alice"] = 88

myMap["bob"] = 99

print(len(myMap))
print(len(myMap))
print("alice" in myMap)
print("bob" in myMap)

myMap.pop("bob")

myMap = {"alice": 90, "bob": 100}


# DICT COMPREHENSION
myMap = {i: 2*i for i in range(3)}
print(myMap)


myMap2 = {i: [] for i in range(4)}
print(myMap2)


# looping the map
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)
# looping the map
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)