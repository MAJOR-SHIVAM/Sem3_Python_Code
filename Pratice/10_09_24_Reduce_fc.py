import functools
# n = 300
# C = functools.reduce(lambda x, y: x+y, range(1,n+1))
# print(C)



# f = lambda a,b: a if (a > b) else b
# B = functools.reduce(f, [47, 11, 42, 102, 13])
# print(B)


# def x100y(x, y):
#     return 100*x + y
# print(functools.reduce(x100y, [13]))
# print(functools.reduce(x100y, [13], 1))
# print(functools.reduce(x100y, [2, 5, 9]))
# print(functools.reduce(x100y, [2, 5, 9], 7))


[47, 11, 42, 102, 13]
f = lambda a,b : (a*b)
B = functools.reduce(f, [47, 11, 42, 102, 13])
print(B)

