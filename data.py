# w create
# append
# read


# handle = open('users.txt', 'w')
# handle.write('hellow python')
# handle.close()
#


# handle = open('users.txt', 'a')
# handle.write(' hellow python')
# handle.close()


# handle = open('users.txt', 'a')
# handle.write(' hellow python')
# handle.close()
#
#
# handle = open('users.txt', 'r').read()
#
# print(handle)

#
# handle = open('users.txt', 'r').readline()
#
# print(handle)

# handle = open('users.txt', 'r').readlines()
#
# print(handle)


# handle = open('users.txt', 'a')
# name=input('Enter your name')
# handle.write(name)
# handle.write('\n')
# handle.close()


# def data(username, password):
#     username = admin
#     password = 123
#     return

#
# username = input('Enter your username')
# password = input('Enter your Password')
#
# if username == username and password == password:
#     handle = open('users.txt', 'a')
#     handle = open('users.txt', 'a')
#     name = input('Enter your name')
#     handle.write(name)
#     handle.write('\n')
#     handle.close()
# else:
#     print('invalid username & Password')


def register():
    name = input('Enter your username: ')
    if name in open('users.txt', 'r').read():
        print("username already exist")
        register()

    password = input('Enter your Password: ')
    c_password = input('confirm password: ')
    if password != c_password:
        print('Password not Match')
        register()

    handle = open('users.txt', 'a')
    handle.write(name)
    handle.write(' ')
    handle.write(password)
    handle.write('\n')
    handle.close()

def login():
    name = input('Enter username: ')
    password = input('Enter password: ')
    with open('users.txt', 'r') as file:
        users_data = []
        for data in file.readlines():
            users_data.append(data.split())

        total_users = len(users_data)
        increment = 0
        login_success = 0

        while increment < total_users:
            username = users_data[increment][0]
            upassword = users_data[increment][1]
            if username == name and password == upassword:
                login_success = 1
            increment += 1

        if login_success == 1:
            print("login success Welcome : " + name)
        else:
            print("username & password not match")


message = input("do you have an account y/n")

if message == 'y':
    login()
else:
    register()
