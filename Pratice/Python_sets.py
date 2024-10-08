# #Create a Set:
# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# #Note: Sets are unordered, so you cannot be sure in which order the items will appear.




# Duplicate values will be ignored:
# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)




# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)




# Get the number of items in a set:
# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))





# String, int and boolean data types:
# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}



# A set with strings, integers and boolean values:
# set1 = {"abc", 34, True, 40, "male"}




# What is the data type of a set?
# myset = {"apple", "banana", "cherry"}
# print(type(myset))




# Using the set() constructor to make a set:
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)





# Loop through the set, and print the values:
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)




# Check if "banana" is present in the set:
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)




# Add an item to a set, using the add() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)




# Add elements from tropical into thisset:
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)





# Add elements of a list to at set:
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)



# Remove "banana" by using the remove() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)
# # Note: If the item to remove does not exist, remove() will raise an error.






# Remove "banana" by using the discard() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)
# # Note: If the item to remove does not exist, discard() will NOT raise an error.




# Remove a random item by using the pop() method:
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)
# # Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


# Keep the items that exist in both set x, and set y:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)





# Return a set that contains the items that exist in both set x, and set y:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)




# Keep the items that are not present in both sets:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)




# Return a set that contains all items from both sets, except items that are present in both:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)




# True and 1 is considered the same value:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)