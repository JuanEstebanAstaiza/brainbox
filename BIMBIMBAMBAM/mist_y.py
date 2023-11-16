import tkinter as tk
from tkinter import messagebox, simpledialog
from user_management import UserManager as um
from exam_builder import exam_builder as eb
from examSolver import examSolver as es


class MistY:
    def __init__(self, root):
        self.root = root
        self.user_manager = um()
        self.exam_builder = eb()
        self.exam_solver = None

        self.logged_username = ""

        # Inicia la ventana de inicio de sesión
        self.login_window = LoginWindow(root, self)
        self.login_window.show()

        self.register_window = RegisterWindow(root, self)
        self.register_window.hide()

        self.exam_builder_window = ExamBuilderWindow(root, self)
        self.exam_builder_window.hide()

        self.exam_solver_window = ExamSolverWindow(root, self)
        self.exam_solver_window.hide()

    def register_user(self, username, password, user_type):
        self.user_manager.register_user(username, password, user_type)
        messagebox.showinfo("Registration", "Successfully registered!")

    def login_user(self, username, password):
        if not self.user_manager.login_user(username, password):
            messagebox.showerror("Login Error", "Invalid username or password")

        if messagebox.askyesno("Verify", "Are you a teacher?"):
            messagebox.showinfo("Login", "Successfully logged in! Redirecting to Exam Builder...")
            self.login_window.hide()
            self.exam_builder_window.show()
        else:
            messagebox.showinfo("Login", "Successfully logged in! Redirecting to Exam Solver...")
            exam_id = self.getExamId()
            self.exam_solver = es(username, exam_id)
            self.login_window.hide()
            self.exam_solver_window.show()

    def getExamId(self):
        exam_id = None
        flag = True
        while (flag):
            exam_id = simpledialog.askstring("Insert exam id",
                                             "Please  insert the exam id to load your exam solver. Ask your teacher for the code if you don't know it: ")
            if exam_id:
                flag = False
        return exam_id


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
        self.misty.logged_username = username
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
        self.exam_builder_window.geometry("800x400")

        # Campos para la creación de pregunta
        self.label_banco = tk.Label(self.exam_builder_window, text="ID Banco Preguntas")
        self.label_banco.pack()
        self.id_banco_preguntas_entry = tk.Entry(self.exam_builder_window, text="ID Banco Preguntas", width="200")
        self.id_banco_preguntas_entry.pack()

        self.label_pregunta_id = tk.Label(self.exam_builder_window, text="ID Pregunta")
        self.label_pregunta_id.pack()
        self.id_pregunta_entry = tk.Entry(self.exam_builder_window, text="ID Pregunta", width="200")
        self.id_pregunta_entry.pack()

        self.label_pregunta_nombre = tk.Label(self.exam_builder_window, text="Pregunta Nombre")
        self.label_pregunta_nombre.pack()
        self.pregunta_nombre_entry = tk.Entry(self.exam_builder_window, text="Pregunta Nombre", width="600")
        self.pregunta_nombre_entry.pack()

        self.label_pregunta_desc = tk.Label(self.exam_builder_window, text="Pregunta Desc")
        self.label_pregunta_desc.pack()
        self.pregunta_desc_entry = tk.Entry(self.exam_builder_window, text="Pregunta Desc", width="600")
        self.pregunta_desc_entry.pack()

        self.label_pregunta_text = tk.Label(self.exam_builder_window, text="Pregunta Text")
        self.label_pregunta_text.pack()
        self.pregunta_text_entry = tk.Entry(self.exam_builder_window, text="Pregunta Text", width="600")
        self.pregunta_text_entry.pack()

        self.label_opciones = tk.Label(self.exam_builder_window, text="Opciones")
        self.label_opciones.pack()
        self.opciones_entry = tk.Entry(self.exam_builder_window, text="Opciones", width="600")
        self.opciones_entry.pack()

        self.label_correcta = tk.Label(self.exam_builder_window, text="Correcta")
        self.label_correcta.pack()
        self.correcta_entry = tk.Entry(self.exam_builder_window, text="Correcta", width="600")
        self.correcta_entry.pack()

        self.label_publico = tk.Label(self.exam_builder_window, text="Publico")
        self.label_publico.pack()
        self.publico_entry = tk.Entry(self.exam_builder_window, text="Publico", width="600")
        self.publico_entry.pack()

        self.label_tema = tk.Label(self.exam_builder_window, text="Tema")
        self.label_tema.pack()
        self.tema_entry = tk.Entry(self.exam_builder_window, text="Tema", width="600")
        self.tema_entry.pack()


        # Botón para enviar la pregunta a examBuilder
        self.create_question_button = tk.Button(self.exam_builder_window, text="Create Question",
                                                command=self.create_question)
        self.create_question_button.pack()

        self.label_exam_id = tk.Label(self.exam_builder_window, text="Id Examen")
        self.label_exam_id.pack()
        self.exam_id_entry = tk.Entry(self.exam_builder_window, text="emxam id", width="200")
        self.exam_id_entry.pack()
        self.create_exam_button = tk.Button(self.exam_builder_window, text="Create Exam", command=self.create_exam)
        self.create_exam_button.pack()


    def create_question(self):
        print(self.misty.logged_username)

        # Obtén los valores de los campos
        id_pregunta = self.id_pregunta_entry.get()
        nombre = self.pregunta_nombre_entry.get()
        descripcion = self.pregunta_desc_entry.get()
        pregunta_text = self.pregunta_text_entry.get()
        opciones = self.opciones_entry.get()
        correcta = self.correcta_entry.get()
        publico = self.publico_entry.get()
        tema = self.tema_entry.get()
        id_banco_preguntas = self.id_banco_preguntas_entry.get()

        # Crea la pregunta utilizando examBuilder
        creator_id = self.misty.logged_username
        self.misty.exam_builder.create_question(id_pregunta, pregunta_text, opciones, correcta, publico, tema, id_banco_preguntas, nombre, descripcion, creator_id)

        # Muestra un mensaje de éxito
        messagebox.showinfo("Success", f"Question '{pregunta_text}' created successfully.")
    def create_exam(self):
        # Obtén los valores de los campos}

        id_examen = self.exam_id_entry.get()

        # Crea la pregunta utilizando examBuilder
        self.misty.exam_builder.create_exam(id_examen)

        # Muestra un mensaje de éxito
        messagebox.showinfo("Success", f"Exam '{id_examen}' created successfully.")

    def show(self):
        self.exam_builder_window.deiconify()

    def hide(self):
        self.exam_builder_window.iconify()


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

    def show(self):
        self.exam_solver_window.deiconify()

    def hide(self):
        self.exam_solver_window.iconify()



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
        self.misty.exam_solver.start_exam()

    def show(self):
        self.exam_solver_window.deiconify()

    def hide(self):
        self.exam_solver_window.iconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = MistY(root)
    root.mainloop()
