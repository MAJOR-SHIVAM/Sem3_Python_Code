#Wap that a string is given of varible "X" inside this string is given 'A18 1a 2b 3c 4d 5e'. Find the word "A18". If A18 is present print "yes, its present" then further ask the user to enter number if he enters number 1 , then from using varibale "x" search the numbers and  if variable says 1 then print 1=a, 2=b, 3=c, 4=d, 5=e and furthermore 2=b, 3=c,4=d, 5=e and 3=c, 4=d, 5=e and  4=d, 5=e  and 5=e solve using loop but take all the numbers using varibale "x"

# x = "A18 1a 2b 3c 4d 5e"
# if "A18" in x:
#     print("yes, its present")
#     n = int(input("Enter a number: "))
#     if n == 1:
#         print("1=a" "\n" "2=b" "\n" "3=c" "\n" "4=d" "\n" "5=e")
#     elif n == 2:
#         print("2=b" "\n" "3=c" "\n" "4=d" "\n" "5=e")
#     elif n == 3:
#         print("3=c, 4=d, 5=e")
#     elif n == 4:
#         print("4=d, 5=e")
#     elif n == 5:
#         print("5=e")
#     else:
#         print("Not present")
# else:
#     print("Not present")

#231030308


# x = "A18 1a 2b 3c 4d 5e"
# if "A18" in x:
#     print("yes, its present")
#     n = int(input("Enter a number: "))
#     if n == 1:
#         for i in range(1,6):
#             print(str(i) + "=" + x[x.find(str(i))+1])
#     if n == 2:
#         for i in range(1,6):
#             print(str(i) + "=" + x[x.find(str(i))+1])
            
#     if n ==3:
#         for i in range(1,6):
#             print(str(i) + "=" + x[x.find(str(i)) + 1])
    
#     if n==4:
#         for i in range (1,6):
#             print(str(i) + "=" + x [x.find(str(i)) + 1])

#     else:
#         print("not present")
# else:
#     print("not present")





# x = "A18 1a 2b 3c 4d 5e"
# if "A18" in x:
#     print("yes, its present")
#     n = int(input("Enter a number: "))
#     if n == 1:
#         for i in range(1,6):
#             print(str(i) + "=" + x[x.find(str(i))+1])
#     if n == 2:
#         for i in range(2,6):
#             print(str(i-1) + "=" + x[x.find(str(i))+2])
#     if n == 3:
#         for i in range(3,6):
#             print(str(i-2) + "=" + x[x.find(str(i))+3])
#     if n == 4:
#         for i in range(4,6):
#             print(str(i-3) + "=" + x[x.find(str(i))+3])
#     if n == 5:
#         for i in range(5,6):
#             print(str(i-4) + "=" + x[x.find(str(i))+1])
# else:
#     print("not present")



# X = 'A18 1a 2b 3c 4d 5e'

# if 'A18' in X:
#     print("yes, it's present")
#     num = int(input("Enter a number: "))
#     if num in range(1, 6):
#         for i in range(num, 6):
#             print(f'{i}={X[X.index(str(i)) + 1]}')
# else:
#     print("A18 is not present in the string.")




# X = 'A18 1a 2b 3c 4d 5e'

# if 'A18' in X:
#     print("yes, it's present")
#     num = int(input("Enter a number: "))
#     while num not in range(1, 6):
#         num = int(input("Invalid number. Please enter a number between 1 and 5: "))
    
#     for i in range(num, 6):
#         print(f'{i}={X[X.index(str(i)) + 1]}')
# else:
#     print("A18 is not present in the string.")



#---------------------------------------------------------------------------------------------------------------



#aske user for 5 students name .i.e, First name in all small letters and you need to filter out students name started with 'a' store them in a list whose names start with 'a' and rest all the students name should stores in another list. Those names which are starting from 'a' make them in uppercase and lest names should be in reverse order. then merge all the names in a single sorted list in an ascending order


# name_list = []
# a_list = []
# for i in range(5):
#     name = input("Enter the name of the student: ")
#     name_list.append(name)

#     if name[0] == 'a':
#         a_list.append(name.upper())
#     else:
#         name_list[name_list.index(name)] = name[::-1]
        

# final_list = a_list + sorted(name_list)
# print(final_list)





# name_list = [input("Enter the name of the student: ") for _ in range(5)]
# a_list = [name.upper() for name in name_list if name[0] == 'a']
# name_list = [name[::-1] if name[0] != 'a' else name for name in name_list]
# final_list = a_list + sorted(name_list)
# print(final_list)
#Shivam_Sharma
#231030308




# ---------------------------------------------------------------------------------------------------------------



#thistuple = ("apple", "mango", "papaya", "pineapple", "apple", "cherry")take this as input in first tuple, need to create second tuple...which sould contain first letter of individual of repeated item i.e., ""....create third tuple and in this there should be non repeated data




# thistuple = ("apple", "mango", "papaya", "pineapple", "apple", "cherry")
# repeated_items = []
# unique_items = []
# first_letter_of_repeated_items = []
# for item in thistuple:
#     if thistuple.count(item) > 1:
#         repeated_items.append(item)
#         first_letter_of_repeated_items.append(item[0])
#     else:
#         unique_items.append(item)
# second_tuple = tuple(first_letter_of_repeated_items)
# third_tuple = tuple(unique_items)
# print("Second Tuple:", second_tuple)
# print("Third Tuple:", third_tuple)




# thistuple = ("apple", "mango", "papaya", "pineapple", "apple", "cherry")

# second_tuple = tuple(item[0] for item in thistuple if thistuple.count(item) > 1)


# third_tuple = tuple(item for item in thistuple if thistuple.count(item) == 1)

# print("Second tuple:", second_tuple)
# print("Third tuple:", third_tuple)





#---------------------------------------------------------------------------------------------------------------




#Ask the user to give input like 1 space 2 space 3 space and need to store all three values in a list with square brackets and then print the reverse value like 3 2 1. Dont make another list use the same list.



# thislist = list((input("Enter three values with space: ").split()))
# thislist.reverse()
# print(thislist)

#Ask the user to give input like 1 space 2 space 3 space and need to store all three values in a list with square brackets and then print the values in reverse but without using reverse methods like 3 2 1. Dont make another list use the same list.


# thislist = list((input("Enter three values with space: ").split()))
# temp = thislist[0]
# thislist[0] = thislist[len(thislist)-1]
# thislist[len(thislist)-1] = temp
# temp = thislist[1]
# thislist[1] = thislist[len(thislist)-2]
# thislist[len(thislist)-2] = temp
# print(thislist)



#----------------------------------------------------------------------------------------------------------------



#17/08/24

#  make one set in which abusing words will be stored "abuse_words = {'hate', 'fucking', 'shit', 'bitch', 'bastard'}".  input is  "I hate you fucking bastard bitch" string format, rewrite that sentence, but remove abuse words from the string and store the sentence again in string after rmoving abusive words.




# abuse_words = {'hate', 'fucking', 'shit', 'bitch', 'bastard'}
# input_string = "I hate you fucking bastard bitch"

# # Remove abusive words using list comprehension
# filtered_sentence = ' '.join(word for word in input_string.split() if word not in abuse_words)

# # The filtered sentence will be without the abusive words
# filtered_sentence




# abuse_words = {'hate', 'fucking', 'shit', 'bitch', 'bastard'}
# sentence = input("I hate you")

# for word in abuse_words:
#     if word in sentence:
#         sentence = sentence.replace(word, '')

# print(sentence)






# abuse_words = {'hate', 'fucking', 'shit', 'bitch', 'bastard'}
# sentence = input("I hate you ")

# sentence = ' '.join(word for word in sentence.split() if word.lower() not in abuse_words)

# print(sentence)



# abuse_words = {'hate', 'fucking', 'shit', 'bitch', 'bastard'}
# sentence = input("I hate you fucking bastard bitch: ")

# for word in abuse_words:
#     if word in sentence:
#         sentence = sentence.replace(word, '')

# print(sentence)







# abuse_words = {'hate', 'fucking', 'shit', 'bitch', 'bastard'}
# sentence = print("I hate you fucking bastard bitch")
# #sentence = input("Enter a sentence: ")

# for word in abuse_words:
#     if word in sentence:
#         sentence = sentence.replace(word, '')

# print(sentence)

    



# abuse_words = {'hate', 'fucking', 'shit', 'bitch', 'bastard'}
# sentence = "I hate you fucking bastard bitch"

# new_sentence = ' '.join([word for word in sentence.split() if word.lower() not in abuse_words])

# print(new_sentence)






# One string is already given "Jaypee University Of Information Technology". Need to find out all vowels in the given string.But there should be no repetiotion of vowels. Make this program within 5 lines. Witout using loops


# x = "Jaypee University Of Information Technology"
# vowels = set("aeiouAEIOU")
# unique = set(x) & vowels
# print(sorted(unique, key=x.index))



# having a Info.txt file containing name and roll number, and in that list two names are same if names are same then print the details of one by one of those details like name and roll number. dont use loops i.e., for or while and if else condition


# info = {}
# with open('Pratice\Info.txt', 'r') as f:
#     for line in f:
#         name, roll = line.strip().split(',')
#         if name not in info:
#             info[name] = []
            
#         info[name].append(roll.strip())
        


# dict = {}
# count = 0
# with open('Pratice\Info.txt', 'r') as Info:
#     roll_no = Info.readline().split(", ")
#     for i in roll_no:
#         dict.update({i.split(":")[0] : i.split(":")[1]})

# print(dict)


# for key, values in info.items():
#     if len(values) > 1:
#         for value in values:
#             print(f'Name: {key}, Roll Number: {value}')







# one dictionary is given l = {'1' : 10, '2' : 20, '3' : 30,} when 1 multiply with 10 give 10, when 2 multiply with 10 give 20, when 3 multiply with 10 give 30. Using list comprehension give code in one line.


# l = {'1' : 10, '2': 20, '3' : 30}
# print([int(key)*value for key,value in l.items()])

# print([value/int(key) if value%2==0 else int(key)*value for key,value in l.items()])


# print([value/int(key) if value%2==0 else value*int(key) for key,value in l.items()])





#10-09-24 avg task
# default value is given now u have to calculaye the devision of the student where condition is if a student has obtained the marks of 80 to 90 print A grade, 70 - 80 print B grade and 80 - 70 print C grade. then find the avg marks and according to that print the division of the stduent in which he is lying. u can use either map, list, lambda
# import functools
# m = [80, 71, 92, 65, 78]

# avg = sum(m)/len(m)

# grade = list(map(lambda x: 'A' if 80<=x<=90 else 'B' if 70<=x<80 else 'C', m))

# print("Grade of student is : ", grade)
# print("Average mark of student is : ", avg)
# print("Average marks of student grade is : ",)

# a = lambda x,y : (x+y)
# print(a)



# avg = functools



#--------------------------------------------17/09/24-------------------------------------------------



# There are five students roll and marks and u need to sort and then find the first three students who have topped the exam. use enum and use less line as much it can


# from enum import Enum
# class marks:
#     101 = 91
#     104 = 93
#     106 = 95
#     107 = 97
#     109 = 99
# for x in sorted(student, key)



# from enum import Enum

# class Students(Enum):
#     a1 = 85
#     b2 = 92
#     c3 = 76
#     d4 = 89
#     e5 = 95

# [print(x.name, x.value) for x in sorted(Students, key=lambda s: s.value, reverse = True)[:3]]



#------------------------------------------------------------------------------------------------------------


#24/09/24

# create a class and you need to initialize twi parameters one roll no and name, intiliaze one class where class and name and another will print roll no


# class Student:
#     def __init__(self, roll, name):
#         self.roll = roll
#         self.name = name

# class Name(Student):
#     def __init__(self, roll, name):
        
#         self.roll = roll
#         self.name = name

#     def print_name(self):
#         print(self.name)


# class Roll(Student):
#     def __init__(self, roll, name):
       
#         self.roll = roll
#         self.name = name

#     def print_roll(self):
#         print(self.roll)

# n = Name(308, "Shivam")
# r = Roll(308, "Shivam")

# n.print_name()  
# r.print_roll()  




# define one class with two parameter and u need to define two functions search for vowels
# first parameter will store input from user and user will input string
# second parameter will be used for to search for any of the letter and letter will be default i.e., vowels
# then return the count of vowels

# class Vowels:
#     def __init__(self, string, letter='aeiouAEIOU'):
#         self.string = string
#         self.letter = letter

    

#     def vowels(self):
#         return len([i for i in self.string if i in self.letter])

#     def print_vowels(self):
#         print("Vowels in the string are: ")
#         for i in self.string:
#             if i in self.letter:
#                 print(i, end=" ")
#         print()  

# v = Vowels("Jaypee University of Information Technology")
# print(v.vowels())
# v.print_vowels()



