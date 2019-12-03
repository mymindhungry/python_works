
################ ERROR HANDLING

# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass
#


####################### try catch - error handling


def add(x,y):
    if y==0:
        raise Exception('y is zero')
    return x+y


try:
    add(2,0)

except Exception as error:
    print(error)

else:
    print(x)




finally:
    print('all done!')


#  MUltiple Exception - HOMEWORK
# postman - download
# webstorm - download- 30 days trail
# dictionary file is more important for API
