# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])


"""Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):"""
b = "Hello, World!"
print(b[-5:-2])


b = "Hello, World!"
print(b[: -4])  #Hello, Wo


a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())



a = " Hello, World!   "
print(len(a))
print(a.strip()) # returns "Hello, World!"
#print(len(a.strip))


a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("W", "H"))


ori = "Hello, World"
new = ori.replace(" ", "")

print(new)  

x = "For texting  I have texted a text"
new = x.replace("text", "T")
print(new)


def replace_last_word(input_string, old_word, new_word):
    words = input_string.split()
    if words[-1] == old_word:
        words[-1] = new_word
    return ' '.join(words)

input_string = "For texting  I text have texted a "
old_word = "text"
new_word = "t"

result = replace_last_word(input_string, old_word, new_word)
print(result)


#replce "text" with  "TEXT" with in "For texting  I have texted a text"
# Original string
original_string = "For texting I have texted a text"
ori1 = "For text texting I have texted a "

# Replace 'text' with 'TEXT'
modified_string = original_string.replace("text", "TEXT")
modi = ori1.replace("text", "TEXT")

print(modified_string)
print(modi)

