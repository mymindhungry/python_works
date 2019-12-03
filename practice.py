#
# # -*- 1. print hello world -*-
# print("hello world!")
# # -*- coding: encoding -*-

# -*- 2. comments (single / multiple lines) -*-

# this is first line comment
spam = 1  # and this is the second comment
# ... and now a third!

text = "this is not a comment because it's inside quotes"

# -*- 3. using python as a calculator -*-
# a = 1
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a + b * a)

# -*- 3.1.2. Strings¶-*-

# print('spam eggs') # single quotes
# print('doesn\'t') # use \' to escape the single quotes
# print('"Yes." they said') # ... or use double quotes instead
#
# print('C:\some\name')
# print(r'c:\some\name')

# -*- 3. using multilines comments -*-
# print(""" multi
#  line
# comments
# """)
#
# print(3*'un' + 'ium')
# print('py' 'thon') #Two or more string literals
# # (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
#
# text = ('Put several strings within parentheses '
#         'to have them joined together.')
# print(text)

# f you want to concatenate variables or a variable and a literal, use +:
# prifix = 'py'
#
# print(prifix + 'thon')


word = 'python'
# print(word[0])
# print(word[4])
#
#
# print(word[0:2])
# print(word[-1])
# print(word[-2])
# print(word[-6])
# print(word[:3])
# print(word[3:])
# print(word[-3:])
# print(word[42:])
# print(word[4:42])

#
# print('J' + word[1:])
# print(word[:2] + 'py')
#
# s='fhsdjgfhsdbhdsbfbhdfgdsfhdgshfg'
# print(len(s))


# -*- 3.1.3. Lists¶-*-

# squares = [1, 3, 5, 7, 9, 15, 24]
# print(squares)
#
# print(squares[0])
# print(squares[-1])
# print(squares[-3:])
# print(squares[:-3])
# print(squares[:])
# print(squares + [54, 16, 34, 54, 90, 1]) # something wrong  here
#
# cubes = [1, 8, 27, 65, 125]
# print(4 ** 3) # the cube of 4 is 64 not 65
# cubes[3]=64 # replace the wrong value
# print(cubes)

# ============Letter=========

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# letters[2:5] = []
# print(letters)
#
# letters[:]=[]
# print(letters)
#
# letters=['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(len(letters))

# a = ['a', 'b', 'c', 'd']
# n = [1, 2, 3]
# x = [a, n]
# print(x)
# print(x[0])
# print(x[0][1])

# ========3.2. First Steps Towards Programming¶ ==========

# Fibonacci series:
# the sum of two elements defines the next
# a, b = 0, 1
# #
# # print(a)
# # print(b)
#
# while a < 10:
#     print(a)
#     a, b =b, a + b


# =============================

# i = 256 * 256
# print('The value of i is', i)

# =============================

# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a + b

#  ============  4. More Control Flow Tools¶ =================

# 4.1. if Statements

# x = int(input("Please enter an number: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


#  ========4.2. for Statements¶===============


# words=['cat','window','defenestrate']
# for w in words:
#     print(w, len(w))


# =====================
#
# for user,status in users.copy().items():
#     if status=='inactive':
#         del users[user]
#
# active_users={}
# for user, status in users.items():
#     if status=='active':
#         active_users[user]=status


#  ======== 4.3. The range() Function¶==============

# for i in range(5):
#     print(i)

# ======================


# print(sum(range(4)))

# ========================

# a= ['welcome','to','nepal']
# for i in range(len(a)):
#     print(i, a[i])


# ==========4.4. break and continue Statements, and else Clauses on Loops¶========

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equal', x, '*', n // x)
#             break
#     else:
#         print(n, 'is a prime number')

# =======================================

for num in range(2, 10):
    if num % 2 == 0:
        print("found an even number", num)
        continue
    print("found a number", num)