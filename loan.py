from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()

root.title('Loan')

root. geometry("1920x1080")
root.configure(bg="#fff")
root.resizable(False, False)

# Connect to MySQL database ------------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manas",
    database="cp"
)


# Create a cursor object
mycursor = mydb.cursor()
img = PhotoImage(file='images/signup.png')
Label(root, image=img, bg="white").place(x=400, y=265)

root.mainloop()