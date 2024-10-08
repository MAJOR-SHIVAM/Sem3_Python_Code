# # Create a Tuple:
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)



#Tuples allow duplicate values:
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)



#Print the number of items in the tuple:
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))


# Print the second item in the tuple:
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])
# print(type(thistuple))




# Print the last item of the tuple:
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])



# Return the third, fourth, and fifth item:
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])



# This example returns the items from the beginning to, but NOT included, "kiwi":
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])



# This example returns the items from "cherry" and to the end:
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])




# Convert the tuple into a list to be able to change it:
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)





# Convert the tuple into a list, add "orange", and convert it back into a tuple:
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)




# Create a new tuple with the value "orange", and add that tuple:
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)




# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)




# The del keyword can delete the tuple completely:
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists




# Unpacking a tuple:
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)




# Assign the rest of the values as a list called "red":
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)




# Assign the rest of the values as a list called "red":
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)



# Add a list of values the "tropic" variable:
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)



# Iterate through the items and print the values:
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)





# Print all items by referring to their index number:
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])




