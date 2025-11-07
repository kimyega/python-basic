print(abs(3))
print(abs(-3))
print(abs(-1.2))

print(all([1,2,3]))
print(all([1,2,3,0]))

print(any([1,2,3,0]))
print(any([0,""]))

print(chr(97))
print(chr(48))

print(divmod(7,3))
print(divmod(1.3, 0.2))

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4,3)'))

print(hex(234))
print(hex(3))

a = 3
print(id(3))
print(id(a))

b = a
print(id(b))

a = input()
print(a)

b = input("Enter: ")
print(b)

print(int('3'))
print(int(3.4))
