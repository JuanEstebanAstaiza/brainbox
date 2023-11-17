from user_management import UserManager as um
from root import root as rt
from Exam_stadistics_controller import statsController as st

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

def userScan(username):

    user_manager = um()

    print("Welcome to the user scan Test!")

    username_insert = input("Write the username to search: ")
    if user_manager.user_exists(username_insert):

        print("user found!")
    else: print("user not found!")

def ornitorrinco():

    user_manager = um()

    print("Welcome to the delete Test!")

    username_insert = input("Write the username to delete: ")

    if user_manager.user_exists(username_insert):
        x=1
        print("user found!")

        if x==1:
            user_manager.delete_user(username_insert)


    else: x=0; print("user not found!")


def bimbimbambam():

    user_manager = um()
    root= rt()

    print("welcome to the admin Test!")

    root.listaOpciones()

def rootLogin():

    user_manager = um()
    root= rt()

    print("welcome to the admin login Test!")

    username_insert = input("Write your username: ")
    password_insert = input("Write your password: ")

    user_manager.login_user(username_insert, password_insert)

    if username_insert=="root" and password_insert=="root":
        root.listaOpciones()
    else: print(".")

#sapa jedionda
#anmial rastrero

def delete_subject():

    user_manager = um()

    subject= input("write the subject to delete: ")

    user_manager.delete_subject_data(subject)


def drpepper():

    user_manager = um()
    stats =st()

    print("Welcome to the exam student results test!")

    exam=input("write the exam id: ")
    student=input("write the student username: ")

    stats.get_student_results(exam,student)

def jimmyfallon():

    stats = st()

    print("Welcome to the general grading method")

    exam = input("write the exam id: ")

    stats.get_exam_statistics(exam)





if __name__ == "__main__":

    #rootLogin()
    #bimbimbambam()
    #ornitorrinco()
    #userScan()
    #main()
    #login()
    #delete_subject()
    #drpepper()
    jimmyfallon()
