import random
# Get the character at position 1 (remember that the first character h
a = "Hello, World!"
print(a[3])
print("\n")


a = "Hello, World!"
print(a[0:2])
print(a[2:])
print(a[2:12])
print()


#Loop through the letters in the word "banana":
for x in "banana":
    print(x)


# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))


# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)


x = "banana"
for i in range(0,6):
    print(x[i])

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


redmi = "Shivam has three frnds with two male and one female"
if "Shivam" in redmi:
    print("Yes, 'Shivam' is present")

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)


# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
