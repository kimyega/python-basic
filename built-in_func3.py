print(max([1, 2, 3]))
print(max("python"))
print(min([1, 2, 3]))
print(min("python"))

print(ord('a'))
print(ord('0'))

print(pow(2, 4))
print(pow(3, 3))

print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))

print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))

a = [3, 1, 2]
result = a.sort()
print(result)
print(a)

print(str(3))
print(str('hi'))
print(str('hi'.upper()))

print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

print(type("abc"))
print(type([]))
print(type(open("test", "w")))

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))