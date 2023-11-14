import hashlib
import mysql.connector
import random

from user_management import UserManager
class root:


        def listaOpciones(self):
            user_manager = UserManager()

            adminOptions= input("press 1 to create an student, press 2 to create an professor, press 3 to delete an student, press 4 to delete a professor")

            if (adminOptions==1):

               id_estudiante=input("create a personalized id for the student")
               student_name=input("enter the name of the student")
               student_lastname=input("enter the last name of the student")
               student_grade=input("enter the grade of the student")
               student_username=input("enter the username of the student")
               student_pwd=input("enter the password of the student")
               student_type=1


               user_manager.register_user(student_username,student_pwd,student_type)







