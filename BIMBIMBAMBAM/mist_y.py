import tkinter as tk
from tkinter import messagebox
from user_management import UserManager as um

class MistY:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, user_type):
        # Implementar lógica de registro aquí
        self.users[username] = {'password': password, 'type': user_type}

    def login_user(self, username, password):
        # Implementar lógica de inicio de sesión aquí
        if username in self.users and self.users[username]['password'] == password:
            return True
        else:
            return False

class GUI:
    def __init__(self, root):
        self.root = root
        self.user_manager = um()

        # Ventana de registro
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

        # Ventana de inicio de sesión
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

        self.login_button = tk.Button(self.login_window, text="Login", command=self.login_user)
        self.login_button.pack()

    def register_user(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()
        user_type = self.register_type_entry.get()
        self.user_manager.register_user(username, password, user_type)
        messagebox.showinfo("Registration", "Successfully registered!")

    def login_user(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        if self.user_manager.login_user(username, password):
            messagebox.showinfo("Login", "Successfully logged in!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
