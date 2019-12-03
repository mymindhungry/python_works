# # # print('Hello Python')
# #
# # x = 10
# # print('the number',format(x))
#
# # ----------------------------------------
# # name = 'admin'
# # age = 20
# # #
# # print ('your name is : ' + (name))
# # print('your age is', format(age))
#
#
# # print(type(age))
# # print(type(name))
#
# # -----------------------------------------
# #
#
#
# # is is not in not in  (new special operator)
# # + _ * % aithmetic data types
# #
# # print(x + y)
# # print(x - y)
# # print(x * y)
# # print(x % y)
# # print(x ** y)  # exponetial
#
# name = "ram karki"
# # print(name.upper())
# print(dir(name))
#
# --------------------------------------

# -------python data types ----------
# integer int float complex
# string
# boolean
# sequence type list tuple dic set
#
# """input value of x and y to use airthmetic operators"""

# x = input('enter the value of X : ')
# y = input('enter the value of Y : ')
#
# print(x + y)
# print(x - y)
# print(x * y)
# print(x % y)
# print(x ** y)


"""using 3 variables in one line"""
# x, y, z = "orange", "banana", "apple"
# print(x)
# print(y)
# print(z)


# as, and , break, class, continue, def, del , if, else, elif,except, global,
# in , import, pass, or, not, yield, with, while,for, from, finally,
# return, try, True, False, none, assert, lambda, nonlocal, raise
#
# ------------------------------------------------------------------
#
""" Type casting for interger """
# x = int(input("Enter the value of X : "))
# y = int(input("enter the value of Y : "))
#
# print("The total sum is", (x + y))
# print("Total multiplication of x adn y is :", (x * y))
#
# #------------------------------------------------------------

# x = 10
# y = 20
#
# if x > y:
#     print("x is large")
# else:
#     print("y is large")

# == > < >= <= !=

#

#
# x = input("Enter X ")
# y = input("Enter Y ")
#
# username = x
# password = y
#
# x = "admin"
# y = "admin002"
#
# if x == y:
#     print("welcome admin")
# else:
#     print("access denied")


# username="admin"
# password="admin123"
#
# if username=="admin" and password == "admin123":
#     print (f'wlecome {username}')
#
# else:
#     print ('invalid acess')
# #
#
# """ 3 number checking """
# x = 10
# y = 20
# z = 30
#
# if x > y and x > z:
#     print("x")
# elif y > x and y > z:
#     print("y")
#
# else:
#     print("z")
#
# """ subject marks"""
# # total, percentage, division,pass, or fail      - HOMEWORK -1
# englis = input(" English Mark ")
#
# dell = int(input("Enter Dell Qty 10000"))
# mac = int(input('enter mac Qty 50000'))
# toshiba = int(input("enter toshiba Qty 30000"))
#
# delivery = input("select home/pickup")
# if delivery ='home':
#     price = 1000
#
#     else
#
#


""" Marksheet Program using conditional statements"""
#
# english = int(input('insert english mark : '))
# a = english
# nepali = int(input('insert nepali mark : '))
# b = nepali
# math = int(input('insert math mark : '))
# c = math
# science = int(input('insert science mark : '))
# d = science
# social = int(input('insert social mark : '))
# e = social
# computer = int(input('insert computer mark : '))
# f = computer
# health = int(input('insert health mark : '))
# g = health
# physics = int(input('insert physics mark : '))
# h = physics
#
# """ for total Marks"""
# t = a + b + c + d + e + f + g + h
# print('Your Total Marks is : ', t)
#
# """ for Total percentage """
# print('Your Total percentage is ', t * 12.5 / 100, '%')
# p = t * 12.5 / 100
#
# """ for Division """
#
# if t < 360 and t > 280:
#     print('Your Result is : Third Division')
# if t < 480 and t > 360:
#     print('Your Result is : Second Division')
# if t < 600 and t > 480:
#     print('Your Result is : First Division')
# if t < 720 and t > 600:
#     print('Your Result is : Dictintion')
# if t < 801 and t > 720:
#     print('Your Result is : Board Topper')
# else:
#     print('')
#
# """ for Pass or Fail """
#
# if print(a < 35 and b < 35):
#     print(" Fail in Subject")
# else:
#     print('Pass in all subject')


"""----------------------------------------------"""

# dellrs = 50000
# d = dellrs
# macrs = 90000
# m = macrs
# toshibars = 65000
# tb = toshibars
# dellqty = int(input("Enter Dell Qty Rs.50000 : "))
# dq = dellqty
# macqty = int(input('enter mac Qty Rs.90000 : '))
# mq = macqty
# toshibaqty = int(input("enter toshiba Qty Rs.65000 : "))
# tbq = toshibaqty
#
# t = (d * dq) + (m * mq) + (tb * tbq)
# delivery = input("select home/pick-up : ")
# if delivery == 'home':
#     dprice = 1000
#     print(t + dprice, ('with home delivery'))
# else:
#     print(t, ' Free Pick-up from Shop')
#
# """ Packaging  Charge """
#
# packaging = input('plastic/bag/gift-box: ')
# if packaging == 'plastic':
#     plastic = 500
# if packaging == 'bag':
#     bag = 1000
# if packaging == 'gift-box':
#     Gift = 500
# else:
#     print('no charge for packaging')
#     print(t + dprice, ('with home delivery'))
#
# """ Location """
#
# location = input('Kathmandu/birgunj/pokhara: ')
# if location == 'kathmandu':
#     kathmandu = 500
# if location == 'birgunj':
#     birgunj = 1000
# if location == 'pokhara':
#     pokhara = 1500
# else:
#     print('City is not selected')
#
# print('VAT AMOUNT : ', t*13 / 100)
# vat=(t*13/100)
# print('Gtotal :',t+vat)

""" python data types"""
# Number = int, floadt, complex
# string
# list  -- array()
# tuple
# set
# dic

# data = 2 + 5j
# print(data.real)
# print(data.imag)
#
# data = 5 + 4j
# print(data)

""" List - array"""
# data = ['ram', 'shyam', 'hari', 'sita', 'gita', 8787]
# print(type(data))
# print(data)
# data[3] = 'madan'
# print(data[3])

# # Tuple
# data = ('hari', 'gita', 'sophia', 'hari') """ duplication data can entry"""
# print(data)
#
# #set
# data = {('hari', 'gita', 'sophia', 'hari'}  """ no duplication data can entry"""
#
# print(data)

#
# data = {
#     'name': 'ram',
#     'age': 20,
#     'phone': 984854
#
# }
#
# print = (f"your name is {data['name']}")
#
#
# data = [
#     ['ram', 'hari'],
#     ['sita', 'gira'],
#     ['madan', 'raj'],
#     {'name': 'bimala', 'age': 20},
#     {'address':['ktm',
#     'bkt'
# ]}
# ]
# #
# # # print(type(data))
# # # print(data[2][1])
# # # print(data[3]['name'])
# print(data[4]['address'][1])
#
#
# #is is not
# #in not in
# name ='ram'
#       print('b' not in name)

#
# """ loop = for, while, yield"""    Homework


# is   ----- identity
# ==   ----- comparision
#
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]
# y = x
# print(id(x))
# print(id(y))
#
# if x is y:
#     print(True)
# else:
#     print(False)
# data = [1, 3, 4, 5, 6, 7]
#
# for x in data:
#     print(x)

# data = [
#     ['ram', 'hari', 'sita', 'gita'],
#     ['gopal', 'madan', 'binita', 'sunita'],
#     ['nadira', 'mandira', 'laxmi', 'kabita'],
# ]
# for x in data:
#     for y in x:
#         print(y)


# for x in range(1,11):
#     print(x)
#

#
# x = 1
#
# while x < 10:
#     print(x)
#     x += 1

# x = 1
# while x < 10:
#     print(input("Enter the Numnber of Employee"), (x))
# x += 1
#
# stu_num = int(input('Enter the number if student'))
# x = 0
# student_list = [1]
# while x < stu_num:
#     name = input('Enter name')
#     student_list.append(name)
#     x += 1
# for s in student_list:
#     print(f'Your Nwme is {s}')

# data = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for x in data:
#     if x == 3 and 7:
#         continue
#
#
#         print(x)
