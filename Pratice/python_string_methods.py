'''# Replace "AIM" with bolded character "AIM"
text = "AIM : Prove Ohm's Law"
bold = text.replace("AIM", "<b>AIM</b>")
bold1 = text.replace("AIM", "\033[1mAIM\033[0m]]")
bold2 = "\033[1m"AIM"\033[0m]]
print(bold)
print(bold1)
print(bold2)'''


#


# count all "i" and "I" in this text

# text = "Jaypee University Of Information Technology"
# x = text.count("i")
# y = text.count("I")
# print(x + y)




# find the position of all "i" and "I" in this text

text = "Jaypee University Of Information Technology"

x = text.find("i")
y = text.find("I")
print(x,y)



# replace j wuth U and find count of university in this text

text = "Jaypee University Of Information Technology"

a = text.replace("J", "U")
x = text.find("University")

print(a)
print(x)




# replace j wuth U and find count of university in this text

text = "Jaypee University Of Information Technology"

t = text.lower() 
print(t)
# print(text.find("university"))
# print(text.index("University"))



text = "Jaypee University Of Information Technology"

t = text.swapcase() 
print(t)









