# You will get an error if you use double quotes inside a string that
txt = "We are the so-called \'Vikings\' from the north."
print(txt)

txt = "We are the so-called \\'Vikings\\' from the north."
print(txt)


txt = "We are the so-called \n'Vikings\' from the north."
print(txt)


txt = "We are the so-called \r'Vikings\r' from the north."
print(txt)


txt = "We are the so-called \'Vikings\t' from the north."
print(txt)


txt = "We are the so-called \'Vikings\b' from the north."
print(txt)



txt = "We are the so-called \f'Vikings\' from the north."
print(txt)


txt = "We are the so-called \'Vikings\ooo' from the north."
print(txt)


txt = "We are the so-called \xhh'Vikings\xhh' from the north."
print(txt)