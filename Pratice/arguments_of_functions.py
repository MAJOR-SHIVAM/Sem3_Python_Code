# def driver():
#         x = int(input('Provide an integer: '))
#         if (x < 0):
#             print("The number {:} is negative!".format(x))
#         elif(x < 100):
#             print("The number {:} is reasonable!".format(x))
#         else:
#             print("The number {:} is too large!".format(x))
# driver()






# provide the temperature of the patient.
# Write this in a form of function
# def temperature(temp):

#     if temp > 105.8:
#         return 'The patient has a very high fever.'
#     elif temp > 103.1:
#         return 'The patient has a high fever.'
#     elif temp > 100.4:
#         return 'The patient has fever.'
#     elif temp > 97.9:
#         return 'The patient is fine.'
#     else:
#         return 'The temperature of the patient is low.'

# temp = float(input('Enter the temperature of the patient: '))
# print(temperature(temp))





# def student_title(fname='Bob', lname='Brown'):
#     print(f"{fname.capitalize():<10}, {lname.capitalize():>30}")
# student_title()
# student_title(lname='Smith')
# student_title(lname='Smith', fname='Joe')




# def f(y, x=1):
#     return y + x**2
# #print(f)
# print(f(5))
# #print(f(x=27))





def add_numbers(*numbers):
    total = 10
    for n in numbers:
        total += n
    return total
print(add_numbers())
print(add_numbers(8))
print(add_numbers(1, 2, 3, 4, 5, 6, 7))
