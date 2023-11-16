#GUI
import tkinter as tk
from tkinter import messagebox
from user_management import UserManager

def create_account():
    top = tk.Toplevel(root)
    top.title("Create Account")
    top.geometry("500x200")

    tk.Label(top, text="Username:").pack()
    tk.Entry(top).pack()

    tk.Label(top, text="Password:").pack()
    tk.Entry(top, show="*").pack()

    tk.Label(top, text="UserType:").pack()
    tk.Entry(top).pack()


    def registro():

        user_manager = UserManager()
       # user_manager.register_user(email.entry.get(),password.entry.get(),Usertype.entry.get())
        messagebox.showinfo("Account Created","Account Successfully created!")
        top.destroy()
    tk.Button(top, text="Create Account", command=registro).pack()



def forgot_password():
    messagebox.showinfo("Forgot Password", "Please contact the system administrator to reset your password.")

def login():
    if entry_email.get() == "email@example.com" and entry_password.get() == "password":
        messagebox.showinfo("Login Successful", "Welcome back!")
    else:
        messagebox.showerror("Login Failed", "Incorrect email or password. Please try again.")

root = tk.Tk()
root.title("Login")
root.geometry("300x200")

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

check_var = tk.IntVar()
tk.Checkbutton(root, text="Remember me", variable=check_var).pack()

tk.Button(root, text="Login", command=login).pack()

tk.Button(root, text="Forgot Password?", command=forgot_password).pack()

tk.Button(root, text="Not registered? Create an account!", command=create_account).pack()

root.mainloop()