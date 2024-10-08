# x = [i for i in range(10)]
# print(x)



# squares = [x**2 for x in range(10)]
# print(squares)



# def double(x):
#     return x*2
# print(double(10))
# B = [double(x) for x in range(10) if x%2==0]
# print(B)



# string = "Hello 12345 World"
# numbers = [x for x in string if x.isdigit()]
# print(numbers)



# C = [x+y for x in [10,30,50] for y in [20,60]]
# print(C)



# from math import pi
# D = [str(round(pi, i)) for i in range(1, 6)]
# print(D)


# noprimes = [j for i in range(2, 8) for j in range(i*2, n, i)]
# primes = [x for x in range(2, n) if x not in noprimes]
# print(primes)



# def count_negatives_lc(my_list):
#     return len([num for num in my_list if num < 0])
# count_negatives_lc(my_list)


# N= 200
# lc_list = [num for num in range(1, N) if num % 2 == 0 and num % 3 == 0]
# print(lc_list)



# numbers = [-6, 7, 13, -1005, 6, 24, 35, -111, 237, 9]
# print(numbers)
# even_odd_numbers = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
# print(even_odd_numbers)



# from random import random
# n = 10
# results = []
# for x in range(n):
#     results.append(int(round(random())))
# print(results)


# We want to simulate a series of coin tosses where 0 is heads and 1 is tails using lsit comprehension
# from random import random
# n = 10
# tosses = [int(round(random())) for x in range(n)]
# print(tosses)




# Use list comprehension to remove all the vowels from the sentence: Remove all the vowels from senetence and again print the senetence

sentence = "The GSFC Python Bootcamp is a great opportunity to learn"
vowels = 'aeiou'
no_vowels = [char for char in sentence if char not in vowels]
print("".join(no_vowels))
