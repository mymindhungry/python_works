# Function return a value not variable
#
# def test():
#     print('Hellow Python')
#
#
#
# test()
#
# def user(name, age):
#     print(f'your name is {name}')
#     print(f'your age is {age}')
#
#
# user('ram', 20)


# """ simple intrest  (PTR) """  # homework
#
#
# def take_value():
#     x = int(input('Enter x'))
#     y = int(input('Enter y'))
#     z = int(input('Enter z'))
#     return [x, y, z]
#
#
# def calc():
#     data = take_value()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p * t * r / 100
#
#
# def display():
#     print(calc())
#
#
# display()

""" in not puting parenthesis () then function will run but allocation only  adress
    put
    """


#
# def students():
#     return "Hello Python"
#
#
# print(students())
#
# print(students.__doc__)


# def students(name, age=0):
#     print(f'your name is {name}')
#     if age > 0:
#         print(age)
#
#
# students('sita')


# Array arguments   & keywords arguments
#
# def students(*name, **age, *address):
#     print(name)
#     print(age)
#
#
# students('sita', 'madan', 'ram', name='ram', age=20, address='ktm')


# '''local and global  value'''
# x = 10
#
#
# def abc():
#     global x
#     x = x * 2
#     print(x)
#
#
# abc()


#
# # rplaceing print by pr
# def pr(data):
#     print(data)
#
# pr('hello')
#
#


#
#
# ''' my repeat
#
# function decorator    Homework'''
#
# def uppercase_decorator (function):
#     def wrapper():
#         func=function()
#         make_uppercase=func.upper()
#         return make_uppercase
#
#     return wrapper
#
# def say_hi():
#     return 'hello Python'
#
#
# decorate = uppercase_decorator(say_hi)
# decorate()


# def add(x, y):
#     return x + y
#
#
# print(add(10, 20))
#

