from user_management import UserManager as um

def main():
    user_manager = um()

    print("Welcome to the Registration Test!")

    username_insert = input("Write your username: ")
    password_insert = input("Write your password: ")
    type_insert = input("type 1 for student or 2 for teacher: ")

    user_manager.register_user(username_insert, password_insert, type_insert)

    print("Successfully registered!")

    if user_manager.user_exists(username_insert):
        print("This user already exists. Try again with another username.")
    else:
        print("Registration and login test completed successfully.")


def login():

    user_manager = um()

    print("Welcome to the login Test!")

    username_insert = input("Write your username: ")
    password_insert = input("Write your password: ")

    user_manager.login_user(username_insert, password_insert)

    print("successfully logged in!")



if __name__ == "__main__":
    main()
    login()

