r = lambda x, y: [i for i in range(1, 1000) if i % x == 0 or i % y == 0]
print(r(3,5))