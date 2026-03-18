from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("LOGIN WINDOW")
root.iconbitmap("pixel2.ico")

root.geometry('500x500+0+0')
root.configure(background="#1E1E2F")   # dark background

def login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or password == "":
        messagebox.showwarning("Warning", "Please enter Email and Password")

    elif email == "admin@gmail.com" and password == "1234":
        messagebox.showinfo("Success", "Login Successful")

        # open new window
        dashboard = Toplevel(root)
        dashboard.title("MITRA EYE CARE")
        dashboard.geometry("300x200")

        Label(dashboard,
              text="Welcome to Mitra Eye Care!",
              font=("Arial",16,"bold")).pack(pady=50)

    else:
        messagebox.showerror("Error", "Invalid Email or Password")

# image
img = Image.open('mi.jpeg')
resize_img = img.resize((120,100))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root, image=img, bg="#1E1E2F")
img_label.pack(pady=10)

# title
text_label = Label(root,
                   text="MITRA EYE CARE",
                   font=('Arial',18,'bold'),
                   bg="#D4AF37",
                   fg="black")
text_label.pack(pady=10)

# email
email_label = Label(root,
                    text="Email",
                    font=('Arial',16,'bold'),
                    bg="#1E1E2F",
                    fg="white")
email_label.pack(pady=(20,5))

email_entry = Entry(root,
                    font=('Arial',16),
                    bg="white",
                    fg="black",
                    width=25)
email_entry.pack(pady=5)
                 
# password
password_label = Label(root,
                       text="Password",
                       font=('Arial',16,'bold'),
                       bg="#1E1E2F",
                       fg="white")
password_label.pack(pady=(20,5))

password_entry = Entry(root,
                       font=('Arial',16),
                       bg="white",
                       fg="black",
                       width=25,
                       show="*")
password_entry.pack(pady=5)

login_btn = Button(root,
                   text="Login",
                   font=('Arial',16,'bold'),
                   bg="#E63946",
                   fg="white",
                   width=10,
                   command=login)
login_btn.pack(pady=20)

root.mainloop()
