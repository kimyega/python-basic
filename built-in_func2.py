print(int('11', 2))
print(int('1A', 16))

class Person:
    pass

a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))

sum = lambda a, b: a + b
sum(3, 4)

def sum(a, b):
    return a + b

myList = [lambda a, b: a+ b, lambda a, b: a*b]

print(myList)
print(myList[0])
print(myList[0](3,4))
print(myList[1](3,4))

print(len("python"))
print(len([1,2,3]))
print(len((1, 'a')))

print(list("python"))
print(list((1,2,3)))

a = [1, 2, 3]
b = list(a)
print(b)

print(id(a))
print(id(b))


