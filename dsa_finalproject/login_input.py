
import sqlite3
import tkinter as tk
from tkinter import messagebox, PhotoImage, Toplevel


import subprocess
# init data
def init_db():
    conn = sqlite3.connect("admin3.db")
    cursor = conn.cursor()

    # create admins table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        user_id REAL
    )
    """)

    # create users table without pet_preference
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        user_id REAL
    )
    """)


    # sample ng admin data
    cursor.execute("SELECT COUNT(*) FROM admins")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO admins (username, password, user_id) VALUES (?, ?, ?)", ("admin", "admin123", "123456"))

    # sample ng user data 
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, password, user_id) VALUES (?, ?, ?)",
                       ("user1", "user123", "123456"))
        cursor.execute("INSERT INTO users (username, password, user_id) VALUES (?, ?, ?)",
                       ("user2", "user234", "123456"))
        # sample data
        cursor.execute("SELECT COUNT(*) FROM userid")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO userid (username, password, user_id) VALUES (?, ?, ?)",
                           ("user1", "user123",  "12345"))
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?, ?)",
                           ("user2", "user234", "123456"))

    conn.commit()
    conn.close()


# Function login
def login():
    user_id = user_id_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()

    conn = sqlite3.connect("admin3.db")
    cursor = conn.cursor()

    if role == "Admin":
        cursor.execute("SELECT * FROM admins WHERE username=? AND password=?", (username, password))
    else:
        cursor.execute("SELECT * FROM users WHERE id=? AND username=? AND password=?", (user_id, username, password))

    result = cursor.fetchone()
    if result:
        if role == "Admin":
            subprocess.run(["python", "admin_dashboard.py"])
        else:
            subprocess.run(["python", "user_dash_ver2.py"])
    else:
        messagebox.showerror("Login Failed", "Invalid user ID, username, or password!")

    conn.close()

#Register
def open_registration_window():
    reg_window = Toplevel(root)
    reg_window.title("Register New User")
    reg_window.geometry("400x400")
    reg_window.resizable(False, False)

    tk.Label(reg_window, text="Register New Account", font=("Arial", 18, "bold")).place(x=80, y=20)
    tk.Label(reg_window, text="Username", font=("Arial", 14)).place(x=50, y=80)
    reg_username_entry = tk.Entry(reg_window, font=("Arial", 14), width=30)
    reg_username_entry.place(x=40, y=110)

    tk.Label(reg_window, text="Password", font=("Arial", 14)).place(x=50, y=160)
    reg_password_entry = tk.Entry(reg_window, font=("Arial", 14), show="*", width=30)
    reg_password_entry.place(x=40, y=190)

    tk.Label(reg_window, text="User ID", font=("Arial", 14)).place(x=50, y=240)
    reg_user_id_entry = tk.Entry(reg_window, font=("Arial", 14), width=30)
    reg_user_id_entry.place(x=40, y=270)

    def register_user():
        username = reg_username_entry.get()
        password = reg_password_entry.get()
        user_id = reg_user_id_entry.get()

        if not username or not password or not user_id:
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect("admin3.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, user_id) VALUES (?, ?, ?)",
                           (username, password, user_id))
            conn.commit()
            messagebox.showinfo("Success", "User  registered successfully!")
            reg_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
        finally:
            conn.close()

    tk.Button(reg_window, text="Register", font=("Arial", 14, "bold"), bg="#0073cf", fg="#ffffff", command=register_user).place(x=150, y=320)


# window
root = tk.Tk()
root.title("Pet Adoption System")
root.geometry("1400x700")
root.resizable(False, False)

# Bg Image#change---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bg_image = PhotoImage(file="adoption.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=330, y=0, width=1400, height=700)

# Header
tk.Label(root, text="Cats, Dogs and Even Dinosaurs\nAdopt Any Pet You Like!", font=("Arial", 30, "bold"), bg="#ffffff", fg="#333333", justify="left", wraplength=600).place(x=50, y=30)
tk.Label(root, text="Find your perfect pet companion and give them a forever home.", font=("Arial", 18), bg="#ffffff", fg="#555555", wraplength=500, justify="left").place(x=50, y=130)

# panel
login_frame = tk.Frame(root, bg="#FFFFFF", bd=10, relief="ridge")
login_frame.place(x=110, y=190, width=500, height=480)

tk.Label(login_frame, text="Login to Your Account", font=("Arial", 30, "bold"), bg="#ffffff", fg="#333333").place(x=40, y=20)

tk.Label(login_frame, text="User  ID", font=("Arial", 16), bg="#ffffff", fg="#333333").place(x=50, y=100)
user_id_entry = tk.Entry(login_frame, font=("Arial", 14), width=30, bd=1, relief="solid")
user_id_entry.place(x=50, y=140)

tk.Label(login_frame, text="Username", font=("Arial", 16), bg="#ffffff", fg="#333333").place(x=50, y=180)
username_entry = tk.Entry(login_frame, font=("Arial", 14), width=30, bd=1, relief="solid")
username_entry.place(x=50, y=220)

tk.Label(login_frame, text="Password", font=("Arial", 16), bg="#ffffff", fg="#333333").place(x=50, y=260)
password_entry = tk.Entry(login_frame, font=("Arial", 14), show="*", width=30, bd=1)
password_entry.place(x=50, y=300)

tk.Label(login_frame, text="Role", font=("Arial", 16), bg="#ffffff", fg="#333333").place(x=50, y=340)
role_var = tk.StringVar(value="User ")
tk.Radiobutton(login_frame, text="User ", variable=role_var, value="User ", bg="#ffffff").place(x=120, y=340)
tk.Radiobutton(login_frame, text="Admin", variable=role_var, value="Admin", bg="#ffffff").place(x=200, y=340)

tk.Button(login_frame, text="Login", font=("Arial", 14, "bold"), bg="#0073cf", fg="#ffffff", width=20, command=login).place(x=50, y=380)
tk.Button(login_frame, text="Register", font=("Arial", 12), bg="#ffffff", fg="#0073cf", bd=0, command=open_registration_window).place(x=50, y=420)
tk.Button(login_frame, text="Forgot Password?", font=("Arial", 12), bg="#ffffff", fg="#0073cf", bd=0, command=lambda: messagebox.showinfo("Forgot Password", "Kuwawa sayo anak 😠 .")).place(x=320, y=420)

# footer
tk.Label(root, text="© 2024 Pet Adoption System - All rights reserved.", font=("Arial", 12), bg="#ffffff", fg="#777777").place(x=550, y=670)

# Init Data
init_db()

root.mainloop()