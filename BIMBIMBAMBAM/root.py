import hashlib
import mysql.connector
import random

from user_management import UserManager


class root:

    def listaOpciones(self):
        user_manager = UserManager()

        adminOptions = input(
            "Press 1 to create a student, press 2 to create a professor, press 3 to delete a student, press 4 to delete a professor: ")

        if adminOptions == "1":
            id_estudiante = input("Create a personalized id for the student: ")
            student_name = input("Enter the name of the student: ")
            student_lastname = input("Enter the last name of the student: ")
            student_grade = input("Enter the grade of the student: ")
            student_username = input("Enter the username of the student: ")
            student_pwd = input("Enter the password of the student: ")
            student_type = 1

            user_manager.register_user(student_username, student_pwd, student_type)
            user_manager.insertStudentData(id_estudiante, student_name, student_lastname, student_grade,
                                           student_username)




        elif adminOptions == "2":
            professor_id = input("Enter the id of the professor: ")
            professor_name = input("Enter the name of the professor: ")
            subject_id = input("Enter the subject_id of the professor: ")
            user_manager.insert_subject_data(subject_id)

            professor_username = input("Enter the username of the professor: ")
            professor_pwd = input("Enter the provisional password of the professor: ")
            professor_type = 2

            user_manager.register_user(professor_username, professor_pwd, professor_type)

            user_manager.professor_data(professor_name, professor_id, subject_id, professor_username)

        elif adminOptions == "3":
            student_username = input("Enter the username of the student to delete: ")

            if user_manager.user_exists(student_username):
                print("User found!")
                user_manager.delete_student(student_username)
                user_manager.delete_user(student_username)
            else:
                print("User not found!")

        elif adminOptions == "4":
            professor_username = input("Enter the username of the professor to delete: ")

            if user_manager.user_exists(professor_username):
                print("User found!")
                user_manager.delete_user(professor_username)
                user_manager.delete_professor(professor_username)
            else:
                print("User not found!")
