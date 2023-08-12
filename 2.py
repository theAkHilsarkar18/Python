# Python Number

# int
# float
# complex

# Python Casting

# x = int(10)
# y = float(23.45)
# z = int("3")
# print(type(z))

# Python String

# single line string
# x = "Hello"
# y = 'World'

# multi line string by ''' , """
# z = '''Hello how are you,
# May be you wil be fine'''
# a = """ hii may name is akhil 
# what is your name"""

# print(z)
# print(a)

# String Slicing

# x = "Hello World"
# print(x[:5]) # hello
# print(x[6:11]) # world

# String function/ modify String

# x = "  Hello World  "
# print(x.upper())
# print(x.lower())
# print(x.strip()) # to remove white space before and after
# print(x.replace('Hello','Hii')) # to replace string one to another
# print(x.split(' ')) # split string and return list ['hello','world']


# String concatenation

# x = "Hello"
# y = "World"
# print(x+y)
# print(x+" "+y)

# String format

# to add number into string
# x = "My age is {}" # use curly bracket
# y = 22
# # print(x+y) # it will show erro
# print(x.format(y))

# to use multiple numbers into print string

# age = 22
# per = 90.67
# intro = "My name is Akhil My age is {} and my percentage is {}"
# intro = "My name is Akhil My age is {1} and my percentage is {0}"
# also you can pass index number to fix value..
# print(intro.format(age,per))

# Escape sequence character

# when you want to use "" into string it will be show error.

# x = "My name is great "Akhil" sarkar" <- it will be show erro
# x = "My name is the great \"Akhil Sarkar\" developer"
# print(x)

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# a = "\'akhil\'"
# print(a)
# b = "akhil\\"
# print(b)
# c = "Hello\nWorld"
# print(c)
# d = "Hello\rWorld"
# print(d)
# e = "Hello\tWorld"
# print(e)
# f = "Hello\bWorld"
# print(f)
# g = "Hello\fWorld"
# print(g)
