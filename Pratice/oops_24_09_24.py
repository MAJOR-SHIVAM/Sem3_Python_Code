# class MyClass:
#     x = 5


# p1 = MyClass()
# print(p1.x)


#----------------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.n = name
#         self.a = age
# p1 = Person("John", 36)
# print(p1.n)
# print(p1.a)

#-------------------------------------------------------------



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# def __str__(self):
#     return f"{self.name}({self.age})"
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)


#----------------------------------------------


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)
# p1 = Person("John", 36)
# p1.myfunc()


#------------------------------------------

# Use the words mysillyobject and abc instead of self:
# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age
#     def myfunc(abc):
#         print("Hello my name is " + abc.name)
# p1 = Person("John", 36)
# p1.myfunc()
