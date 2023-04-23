from tkinter import *
from tkinter import messagebox
import mysql.connector
from pension import Pension
from scholarship import Scholarship

root = Tk()

root.title('Login')

root. geometry("1920x1080")
root.configure(bg="#fff")
root.resizable(False, False)

# Connect to MySQL database ------------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="govfund"
)


# Create a cursor object
mycursor = mydb.cursor()
img = PhotoImage(file='images/signup.png')
Label(root, image=img, bg="white").place(x=400, y=265)

frame = Frame(root, width=500, height=350, bg="white")
frame. place(x=820, y=290)

heading = Label(frame, text="Choose a Scheme", fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 25, 'bold'))
heading. place(x=95, y=5)

def pension():
    Pension(root)

def scholarship():
    Scholarship(root)

def loan():
    # root.destroy()
    import loan


Button(frame, width=32, pady=7, text='Loan', bg='#57a1f8',
       fg='white', border=0,font=('Microsoft YaHei UI Light', 16, 'bold'),command=loan) .place(x=35, y=110)

Button(frame, width=32, pady=7, text='Pension', bg='#57a1f8',
       fg='white', border=0,font=('Microsoft YaHei UI Light', 16, 'bold'),command=pension) .place(x=35, y=185)
Button(frame, width=32, pady=7, text='Scholarship', bg='#57a1f8',
       fg='white', border=0,font=('Microsoft YaHei UI Light', 16, 'bold'),command=scholarship) .place(x=35, y=260)

root.mainloop()