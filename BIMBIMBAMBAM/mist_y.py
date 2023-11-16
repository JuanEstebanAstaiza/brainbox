import tkinter as tk
from tkinter import messagebox
from user_management import UserManager as um

class MistY:
    def __init__(self, root):
        self.root = root
        self.user_manager = um()

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

if __name__ == "__main__":
    root = tk.Tk()
    app = MistY(root)
    root.mainloop()

