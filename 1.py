# python basics

# print function
# print("Hello Python")

# declaring variable
# a = 10
# b = 20
# print(a+b)

# datatype (to set datatype of variable nedd to cast variable).
# num1 = 10
# print(type(num1)) # to check datatype of variable use type()

# name = str("Akhil")
# x = int(10)
# y = float(10)

# print(name)
# print(x)
# print(y)
# print(type(x))

# Create multiple variable

# x, y, z = "Akhil", 98.25, 9825486060
# print(x) # x is int
# print(y) # y is float
# print(z) # z id int/double/big value

# give same value to the multiple variable

# a = b = c = "Akhil"
# print(a)
# print(b)
# print(c)

# Unpack a collection
# if you have collection of values you can unpack and store into variables

# fruits = ["Apple","Orange","Banana"] # must element of collection and number of variable are same.
# x,y,z = fruits # must element of collection and number of variable are same.
# print(x)
# print(y)
# print(z)
#  what will be datatype of collection / tupple ?
# x = [1,2,3,4,5]
# print(type(x)) #list
# tuple is also one type of collection
# x = (1,2,3,4)
# print(type(x)) #tuple


# print() function
# print() function used to output variable.

# x = "Hello Python"
# print(x)

# x = "Hello"
# y = "Python"
# print(x,y)

# x = "Helo"
# y = "Python"
# z = "How are you"
# print(x,y,z) # output : Hello Pyhon How are you
# print(x+y+z) # output : HelloPythonHow are you


# Global variable
# Which variable is created outside the function its called global variable.

# x = "Python" # global variable

# def myfun() :
#     x = "Core Python" #local variable
#     y = "Advanced Python"
#     print(x)
# myfun()

# print(x) # print value of global x
# print(y) # cant access y because its declared in function.

# global keyword
# when you want create a global variable inside the function,that time use global keyword

# def myfun() :
#     global x
#     x = "Core"
#     global y
#     y = "Python"
# myfun()
# also can change value of gloabal variable declared in fun.
# x = "Advanced"
# y = "AI"
# print(x,y)

# Built in datatype in Python

# Text Type:	str
# x = "Hello Python"
# print(type(x))

# Numeric Types:	int, float, complex
# x = 10
# print(type(x))
# x = 10.78
# print(type(x))
# x = 1j
# print(type(x))

# Sequence Types:	list, tuple, range
# list
# x = ["Apple","Banana",'Mango']
# print(type(x))

#tupple
# x = ("Apple","Banana","Mango")
# print(type(x))

# range is function which return a sequence starting by defaault 0, increament by 1 and stop before specified number.
# x = range(6)
# print(type(x))
# print(x)

# Mapping Type:	dict
# dict is collection of key value
# x = {"id":1010,"name":"Akhil"}
# print(x["id"])
# print(x["name"])
# print(x)

# Set Types:	set, frozenset
# set : 
# x = {"apple","banana","mango"}
# print(x)
# print(type(x))
# frozen set
# x = ({"apple","mango","banana"})
# print(x)
# print(type(x))

# Boolean Type:	bool
# x = True
# y = False
# print(x)
# print(y)
# print(type(x))
# print(type(y))
# z = bool(True)

# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType




