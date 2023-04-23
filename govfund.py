from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


MySQLPassword = 'manas'
DatabaseName = 'cp'
Username = 'root'


class Citizen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Fund Management System")

        # Variables
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_aadhar = StringVar()
        self.var_pan = StringVar()
        self.var_occupation = StringVar()
        self.var_disability = StringVar()
        self.var_city = StringVar()
        self.var_bankacc = StringVar()
        self.var_bankifsc = StringVar()

        lbl_tile = Label(self.root, text="Fund Management System", font=(
            'Microsoft YaHei UI Light', 37, 'bold'), fg='darkblue', bg='white')
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

        # Aadhar
        lbl_aadhar = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Aadhar:', bg='white')
        lbl_aadhar.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_aadhar = ttk.Entry(
            upper_frame, textvariable=self.var_aadhar, width=22, font=('arial', 11, 'bold'))
        txt_aadhar.grid(row=0, column=3, padx=2, pady=7)

        # Lbl Occupation
        lbl_occupation = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Occupation:', bg='white')
        lbl_occupation.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_occupation = ttk.Entry(
            upper_frame, textvariable=self.var_occupation, width=22, font=('arial', 11, 'bold'))
        txt_occupation.grid(row=1, column=1, padx=2, pady=7)

        # Email
        lbl_email = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Email:', bg='white')
        lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_email = ttk.Entry(
            upper_frame, textvariable=self.var_email, width=22, font=('arial', 11, 'bold'))
        txt_email.grid(row=1, column=3, padx=2, pady=7)

        # PAN
        lbl_pan = Label(upper_frame, font=('arial', 12, 'bold'),
                        text='Pan Card:', bg='white')
        lbl_pan.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_pan = ttk.Entry(upper_frame, textvariable=self.var_pan,
                            width=22, font=('arial', 11, 'bold'))
        txt_pan.grid(row=2, column=1, padx=2, pady=7)

        # Disability
        lbl_disable = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Disability:', bg='white')
        lbl_disable.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        com_txt_disability = ttk.Combobox(
            upper_frame, textvariable=self.var_disability, state='readonly', font=('arial', 12, 'bold'), width=18)
        com_txt_disability['value'] = ("Y", "N")
        com_txt_disability.current(0)
        com_txt_disability.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Date of Birth
        lbl_dob = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='DOB:', bg='white')
        lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_dob = ttk.Entry(upper_frame, textvariable=self.var_dob,
                            width=22, font=('arial', 11, 'bold'))
        txt_dob.grid(row=3, column=1, padx=2, pady=7)

        # Age
        lbl_age = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Age:', bg='white')
        lbl_age.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_age = ttk.Entry(upper_frame, textvariable=self.var_age,
                            width=22, font=('arial', 11, 'bold'))
        txt_age.grid(row=3, column=3, padx=2, pady=7)

        # Gender
        lbl_gender = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Gender:', bg='white')
        lbl_gender.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        com_txt_gender = ttk.Combobox(
            upper_frame, textvariable=self.var_gender, state='readonly', font=('arial', 12, 'bold'), width=18)
        com_txt_gender['value'] = ("Male", "Female", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4, column=1, sticky=W, padx=2, pady=7)

        # Phone Number
        lbl_phone = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Phone No:', bg='white')
        lbl_phone.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_phone = ttk.Entry(
            upper_frame, textvariable=self.var_phone, width=22, font=('arial', 11, 'bold'))
        txt_phone.grid(row=0, column=5, padx=2, pady=7)

        # City
        lbl_city = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='City:', bg='white')
        lbl_city.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_city = ttk.Entry(
            upper_frame, textvariable=self.var_city, width=22, font=('arial', 11, 'bold'))
        txt_city.grid(row=1, column=5, padx=2, pady=7)

        # Bank Acc
        lbl_bankacc = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='Bank A/C:', bg='white')
        lbl_bankacc.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        txt_bankacc = ttk.Entry(
            upper_frame, textvariable=self.var_bankacc, width=22, font=('arial', 11, 'bold'))
        txt_bankacc.grid(row=2, column=5, padx=2, pady=7)

        # IFSC Code
        lbl_ifsc = Label(upper_frame, font=(
            'arial', 12, 'bold'), text='IFSC Code:', bg='white')
        lbl_ifsc.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        txt_ifsc = ttk.Entry(
            upper_frame, textvariable=self.var_bankifsc, width=22, font=('arial', 11, 'bold'))
        txt_ifsc.grid(row=3, column=5, padx=2, pady=7)


        def schemeChoose():
            root.destroy()
            import choosingScheme

        Button(root, width=25, pady=7, text='Save Details', bg='#57a1f8',
               fg='white', border=0, font=('Microsoft YaHei UI Light', 16, 'bold'), command=self.add_data) .place(x=600, y=500)

        Button(root, width=32, pady=7, text='Apply for Schemes', bg='#57a1f8',
               fg='white', border=0, font=('Microsoft YaHei UI Light', 16, 'bold'), command=schemeChoose) .place(x=550, y=650)


    def add_data(self):

        try:
            conn = mysql.connector.connect(
                host='localhost', user=Username, password=MySQLPassword, database=DatabaseName)
            my_cursor = conn.cursor()
            age = int(self.var_age.get())
            my_cursor.execute('insert into citizen values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (

                # Variables
                self.var_name.get(),
                age,
                self.var_dob.get(),
                self.var_gender.get(),
                self.var_phone.get(),
                self.var_email.get(),
                self.var_aadhar.get(),
                self.var_pan.get(),
                self.var_occupation.get(),
                self.var_disability.get(),
                self.var_city.get(),
                self.var_bankacc.get(),
                self.var_bankifsc.get(),

            ))
            conn.commit()
            conn.close()
            messagebox.showinfo(
                'Success', 'citizen has been addded!', parent=self.root)
            

        except Exception as es:
            messagebox.showerror(
                'Error', f'Due to:{str(es)}', parent=self.root)





def start():
    if __name__ == "__main__":
        root = Tk()
        obj = Citizen(root)
        root.mainloop()
