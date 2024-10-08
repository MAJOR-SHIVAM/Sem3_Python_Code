# add = lambda x, y : x + y
# x = add(2,1)
# print(x)



# remainder = lambda num: num % 2
# print(remainder(5))
# print(remainder(42))



# def convert_from_celcius_to_fahrenheit(T):
#     return ((float(9)/5)*T + 32)
# def convert_from_fahrenheit_to_celsius(T):
#     return (float(5)/9)*(T-32)
# temperatures = (36.5, 37, 37.5, 39)
# fahr = list(map(convert_from_celcius_to_fahrenheit, temperatures))
# print(fahr)
# cel = list(map(convert_from_fahrenheit_to_celsius, fahr))
# print(cel)



# a = [1, 2, 3, 4]
# b = [17, 12, 11, 10]
# c = [-1, -4, 5, 9]
# print("a+b: ", list(map(lambda x,y:x+y, a,b)))
# print("a+b+c: ", list(map(lambda x,y,z:x+y+z, a,b,c)))
# print("a+b-c: ", list(map(lambda x,y,z:x+y-z, a,b,c)))


words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = list()
for w in words:
    stuff.append([w.upper(), w.lower(), len(w)])
print(stuff)
l = list(words)
print(l)

print(list(map(lambda w: [w.upper(), w.lower(), len(w)], words)))