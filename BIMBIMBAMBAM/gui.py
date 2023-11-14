import tkinter as tk
from tkinter import messagebox
import user_management as um
import ttk
from user_management import UserManager

class RegisterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Registration')

        self.label_username = tk.Label(self.master, text='Username:')
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(self.master, text='Password:')
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(self.master, show='*')
        self.entry_password.grid(row=1, column=1)

        self.label_professor = tk.Label(self.master, text='Are you a student or a professor?')
        self.label_professor.grid(row=2, column=0)
        self.checkbox_professor = tk.BooleanVar()
        self.checkbox_professor.set(False)
        self.checkbutton_professor = tk.Checkbutton(self.master, variable=self.checkbox_professor, onvalue=True, offvalue=False, text='I am a professor')
        self.checkbutton_professor.grid(row=2, column=1)

        self.button_register = tk.Button(self.master, text='Register', command=self.register)
        self.button_register.grid(row=3, column=1)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        is_professor = self.checkbox_professor.get()

        print('Username:', username)
        print('Password:', password)
        print('Is a professor:', is_professor)

        um.UserManager.register_user(self,username, password)



class LoginGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Login')

        self.label_username = tk.Label(self.master, text='Username:')
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(self.master, text='Password:')
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(self.master, show='*')
        self.entry_password.grid(row=1, column=1)

        self.button_login = tk.Button(self.master, text='Login', command=self.login)
        self.button_login.grid(row=2, column=1)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == 'user' and password == 'pass':
            messagebox.showinfo('Success', 'Login successful!')
        else:
            messagebox.showerror('Error', 'Incorrect username or password.')


        um.UserManager.login_user(self,username,password)




