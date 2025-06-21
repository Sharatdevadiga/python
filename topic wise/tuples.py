# tuples ar likke arrays but are immutable
tup = {1, 3, 2}
print(tup)
print(tup[0])
print(tup[2])

myMap = {(1, 2): 3}

print(myMap[(1,2)])
mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# Lists cant be keys in the map
# so we can use the tuples as the keys

