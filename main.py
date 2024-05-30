fitness = []
password = []
friendship = []

def register():
    friendship.append(input("Type friendship goal (who do you want to meet and what do you want to do with your time *yes literally*):"))
    usernames.append(input("Type password:"))
    passwords.append(input("choose your password:"))


def login():
    username = input("Enter your username:")
    password = input("Enter your Password:")
    if username in usernames and password in passwords:
        print("welcome")
    else:
        print("incorrect!")


while True:
    account_ans = input("choose:  a)Sign Up     b)login and shop     c)quit ")
    if account_ans == "a":
        register()
    if account_ans == "b":
        login()
    if account_ans == "c":
        break

