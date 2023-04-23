from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

MySQLPassword = 'manas'
DatabaseName = 'cp'
Username = 'root'


class Loan:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Fund Management System")

        self.var_ltype=StringVar()
        self.var_name = StringVar()
        self.var_aadhar = StringVar()
        self.var_LoanAmount = StringVar()
        self.var_occupation = StringVar()


        lbl_tile = Label(self.root, text="Loan Waiver", font=(
            'times new roman', 37, 'bold'), fg='darkblue', bg='white')
        lbl_tile.place(x=0, y=0, width=1530, height=50)

        # Logo
        img_logo = Image.open("images/logo.jpg")
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=270, y=0, width=50, height=50)

        # Image Frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=50, width=1235, height=160)

        # 1st Image
        img_1 = Image.open("images/21404.jpg")
        img_1 = img_1.resize((540, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img_1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)

        # 2nd Image
        img_2 = Image.open("images/4565.jpg")
        img_2 = img_2.resize((540, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img_2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=600, y=0, width=540, height=160)

        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=220, width=1500, height=560)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white',
                                 text='Citizen Information', font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1235, height=230)

        # Name
        lbl_name = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Name:', bg='white')
        lbl_name.grid(row=0, column=0, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(
            upper_frame, textvariable=self.var_name, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=0, column=1, padx=2, pady=7)

        # ret Year
        lbl_retYear = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Aadhar Number:', bg='white')
        lbl_retYear.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_retYear = ttk.Entry(
            upper_frame, textvariable=self.var_aadhar, width=22, font=('arial', 11, 'bold'))
        txt_retYear.grid(row=0, column=3, padx=2, pady=7)

        # Salary
        lbl_salary = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Loan Amount:', bg='white')
        lbl_salary.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_salary = ttk.Entry(
            upper_frame, textvariable=self.var_LoanAmount, width=22, font=('arial', 11, 'bold'))
        txt_salary.grid(row=0, column=5, padx=2, pady=7)

        # Aadhar
        lbl_aadhar = Label(upper_frame, font=('arial', 12, 'bold'),
                           text='Loan Type:', bg='white')
        lbl_aadhar.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_aadhar = ttk.Entry(upper_frame, textvariable=self.var_ltype,
                               width=22, font=('arial', 11, 'bold'))
        txt_aadhar.grid(row=2, column=1, padx=2, pady=7)

        # Age
        lbl_age = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Occupation:', bg='white')
        lbl_age.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_age = ttk.Entry(upper_frame, textvariable=self.var_occupation,
                            width=22, font=('arial', 11, 'bold'))
        txt_age.grid(row=2, column=3, padx=2, pady=7)

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1040, y=0, width=180, height=210)

        btn_add = Button(button_frame, text="Apply", font=(
            'arial', 15, 'bold'), width=13, bg='blue', fg='white',command=self.add_data)
        btn_add.grid(row=0, column=0, padx=1, pady=5)

    def add_data(self):

        try:
            conn = mysql.connector.connect(
                host='localhost', user=Username, password=MySQLPassword, database=DatabaseName)
            my_cursor = conn.cursor()
            loanAmount = int(self.var_LoanAmount.get())
            my_cursor.execute('insert into loan values(%s,%s,%s,%s,%s)', (

                # Variables
                self.var_aadhar.get(),
                self.var_name.get(),
                loanAmount,
                self.var_ltype.get(),
                self.var_occupation.get(),

            ))
            conn.commit()
            conn.close()
            messagebox.showinfo(
                'Success', 'Citizen details updated !', parent=self.root)

        except Exception as es:
            messagebox.showerror(
                'Error', f'Due to:{str(es)}', parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Loan(root)
    root.mainloop()
