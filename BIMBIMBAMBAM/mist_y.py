import tkinter as tk
from tkinter import messagebox
from user_management import UserManager as um
from exam_builder import exam_builder as eb
from examSolver import examSolver as  es

class MistY:
    def __init__(self, root):
        self.root = root
        self.user_manager = um()
        self.exam_builder = eb()
        self.exam_solver = es()

        # Inicia la ventana de inicio de sesión
        self.login_window = LoginWindow(root, self)
        self.login_window.show()

        self.register_window = RegisterWindow(root, self)
        self.register_window.hide()


    def register_user(self, username, password, user_type):
        self.user_manager.register_user(username, password, user_type)
        messagebox.showinfo("Registration", "Successfully registered!")

    def login_user(self, username, password):
        if self.user_manager.login_user(username, password):
            messagebox.showinfo("Login", "Successfully logged in!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password")


class RegisterWindow:
    def __init__(self, root, misty):
        self.root = root
        self.misty = misty

        self.register_window = tk.Toplevel(root)
        self.register_window.title("Register")

        self.register_username_label = tk.Label(self.register_window, text="Username:")
        self.register_username_label.pack()
        self.register_username_entry = tk.Entry(self.register_window)
        self.register_username_entry.pack()

        self.register_password_label = tk.Label(self.register_window, text="Password:")
        self.register_password_label.pack()
        self.register_password_entry = tk.Entry(self.register_window, show="*")
        self.register_password_entry.pack()

        self.register_type_label = tk.Label(self.register_window, text="User type (1 for student, 2 for teacher):")
        self.register_type_label.pack()
        self.register_type_entry = tk.Entry(self.register_window)
        self.register_type_entry.pack()

        self.register_button = tk.Button(self.register_window, text="Register", command=self.register_user)
        self.register_button.pack()

        self.already_have_account_button = tk.Button(self.register_window, text="Already have an Account? Login!",
                                                     command=self.close_register_window_and_open_login)
        self.already_have_account_button.pack()

    def register_user(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()
        user_type = self.register_type_entry.get()
        self.misty.register_user(username, password, user_type)

    def close_register_window_and_open_login(self):
        # Cierra la ventana de registro y muestra la ventana de inicio de sesión
        self.hide()
        self.misty.login_window.show()

    def show(self):
        self.register_window.deiconify()

    def hide(self):
         self.register_window.iconify()

class LoginWindow:
    def __init__(self, root, misty):
        self.root = root
        self.misty = misty

        self.login_window = tk.Toplevel(root)
        self.login_window.title("Login")

        self.login_username_label = tk.Label(self.login_window, text="Username:")
        self.login_username_label.pack()
        self.login_username_entry = tk.Entry(self.login_window)
        self.login_username_entry.pack()

        self.login_password_label = tk.Label(self.login_window, text="Password:")
        self.login_password_label.pack()
        self.login_password_entry = tk.Entry(self.login_window, show="*")
        self.login_password_entry.pack()

        self.forgot_password_button = tk.Button(self.login_window, text="Forgot your Password?",
                                                command=self.forgot_password)
        self.forgot_password_button.pack()

        self.login_button = tk.Button(self.login_window, text="Login", command=self.login_user)
        self.login_button.pack()

        self.dont_have_account_button = tk.Button(self.login_window, text="Don't have an Account? Register now!",
                                                  command=self.open_register_window)
        self.dont_have_account_button.pack()

    def login_user(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        self.misty.login_user(username, password)

    def open_register_window(self):
        # Cierra la ventana de inicio de sesión y muestra la ventana de registro
        self.hide()
        self.misty.register_window.show()

    def forgot_password(self):
        messagebox.showinfo("Forgot Password", "Contact the admin for a password reset.")

    def show(self):
        self.login_window.deiconify()

    def hide(self):
        self.login_window.iconify()

class ExamBuilderWindow:
    def __init__(self, root, misty):
        self.root = root
        self.misty = misty

        self.exam_builder_window = tk.Toplevel(root)
        self.exam_builder_window.title("Exam Builder")

        # Campos para la creación de pregunta
        self.id_pregunta_entry = tk.Entry(self.exam_builder_window, text="ID Pregunta")
        self.id_pregunta_entry.pack()

        self.pregunta_text_entry = tk.Entry(self.exam_builder_window, text="Pregunta Text")
        self.pregunta_text_entry.pack()

        self.opciones_entry = tk.Entry(self.exam_builder_window, text="Opciones")
        self.opciones_entry.pack()

        self.correcta_entry = tk.Entry(self.exam_builder_window, text="Correcta")
        self.correcta_entry.pack()

        self.publico_entry = tk.Entry(self.exam_builder_window, text="Publico")
        self.publico_entry.pack()

        self.tema_entry = tk.Entry(self.exam_builder_window, text="Tema")
        self.tema_entry.pack()

        self.id_banco_preguntas_entry = tk.Entry(self.exam_builder_window, text="ID Banco Preguntas")
        self.id_banco_preguntas_entry.pack()

        # Botón para enviar la pregunta a examBuilder
        self.create_question_button = tk.Button(self.exam_builder_window, text="Create Question", command=self.create_question)
        self.create_question_button.pack()

    def create_question(self):
        # Obtén los valores de los campos
        id_pregunta = self.id_pregunta_entry.get()
        pregunta_text = self.pregunta_text_entry.get()
        opciones = self.opciones_entry.get()
        correcta = self.correcta_entry.get()
        publico = self.publico_entry.get()
        tema = self.tema_entry.get()
        id_banco_preguntas = self.id_banco_preguntas_entry.get()

        # Crea la pregunta utilizando examBuilder
        eb.create_question(id_pregunta, pregunta_text, opciones, correcta, publico, tema, id_banco_preguntas)

        # Muestra un mensaje de éxito
        messagebox.showinfo("Success", f"Question '{pregunta_text}' created successfully.")

class ExamSolverWindow:
    def __init__(self, root, misty):
        self.root = root
        self.misty = misty

        self.exam_solver_window = tk.Toplevel(root)
        self.exam_solver_window.title("Exam Solver")

        # Campos para el examSolver
        self.user_id_entry = tk.Entry(self.exam_solver_window, text="User ID")
        self.user_id_entry.pack()

        self.exam_id_entry = tk.Entry(self.exam_solver_window, text="Exam ID")
        self.exam_id_entry.pack()

        # Botón para iniciar el examSolver
        self.start_exam_button = tk.Button(self.exam_solver_window, text="Start Exam", command=self.start_exam)
        self.start_exam_button.pack()

    def start_exam(self):
        # Obtén los valores de los campos
        user_id = self.user_id_entry.get()
        exam_id = self.exam_id_entry.get()

        # Inicia el examSolver
        es.start_exam()

if __name__ == "__main__":
    root = tk.Tk()
    app = MistY(root)
    root.mainloop()

