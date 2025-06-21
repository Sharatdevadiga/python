
# strings ar immutable
s = "abc"
print(s[0: 2])
print(s[1: 2])

s += "def"
print(s)
print(s[0: 2])

# conversion
print(int("123") + int("123"))
print(str(123) + str(123))

print(ord('a'))
print(ord('b'))

strings = ["abc", "def", "ghi"]
print("-".join(strings))
print("/".join(strings))
print("*".join(strings))

a = "Abc"
print(a.lower())
print(a.upper())

# so in strings
#  ord(), lower(), upper(), "".join(), abc[0, 2], int(), str()
