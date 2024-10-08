# fib = [0, 1, 1, 2, 3, 5, 8, 13 , 21, 34, 55]
# odd_numbers = list(filter(lambda x: x % 2, fib))
# print("Odd Numbers: ", odd_numbers)
# even_numbers = list(filter(lambda x: x % 2 == 0, fib))
# print("Even Numbers: ", even_numbers)




sentence = "The LRC Python Training is a great opportunity to learn P"
vowels = 'aeiou'
vowel_free = list(filter(lambda x: x not in vowels, sentence))
print("".join(vowel_free))


