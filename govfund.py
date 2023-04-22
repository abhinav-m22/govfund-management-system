from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class Citizen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Fund Management System")

        # Variables
        self.var_id = int()
        self.var_name = StringVar()
        self.var_age = int()
        self.var_bankacc = StringVar()
        self.var_bankifsc = StringVar()
        self.var_occupation = StringVar()
        self.var_dob = StringVar()
        self.var_disability = StringVar()
        self.var_aadhar = StringVar()
        self.var_pan = StringVar()
        self.var_city = StringVar()
        self.var_phone = StringVar()
        # self.var_country=StringVar()
        # self.var_salary=StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()

        lbl_tile = Label(self.root, text="FUND MANAGEMENT SYSTEM", font=(
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

        # # Email
        # lbl_email=Label(upper_frame, font=('arial',12,'bold'),text='Email:',bg='white')
        # lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        # txt_email=ttk.Entry(upper_frame,textvariable=self.var_email, width=22, font=('arial', 11, 'bold'))
        # txt_email.grid(row=1, column=3, padx=2, pady=7)

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

        # # Gender
        # lbl_gender=Label(upper_frame, font=('arial',12,'bold'),text='Gender:',bg='white')
        # lbl_gender.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        # com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender, state='readonly', font=('arial',12,'bold'),width=18)
        # com_txt_gender['value']=("Male", "Female", "Other")
        # com_txt_gender.current(0)
        # com_txt_gender.grid(row=4,column=1,sticky=W, padx=2, pady=7)

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

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1040, y=0, width=180, height=210)

        btn_add = Button(button_frame, text="Save", command=self.add_data, font=(
            'arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=1, pady=5)

        btn_update = Button(button_frame, text="Update", command=self.update_data, font=(
            'arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_update.grid(row=1, column=0, padx=1, pady=5)

        btn_delete = Button(button_frame, text="Delete", command=self.delete_data, font=(
            'arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_delete.grid(row=2, column=0, padx=1, pady=5)

        btn_clear = Button(button_frame, text="Clear", command=self.reset_data, font=(
            'arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_clear.grid(row=3, column=0, padx=1, pady=5)

        # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white',
                                text='Citizen Information Table', font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=240, width=1235, height=230)

        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white',
                                  text='Search Citizen Information', font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1235, height=60)

        search_by = Label(search_frame, font=("arial", 11, "bold"),
                          text="Search By:", fg="white", bg="red")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # search
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame, textvariable=self.var_com_search,
                                      state="readonly", font=("arial", 12, "bold"), width=18)

        com_txt_search['value'] = (
            "Select Option", "citizen_phone", "citizen_aadhar")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(
            search_frame, textvariable=self.var_search, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_frame, bg='blue', text='Search', command=self.search_data, font=(
            'arial', 11, 'bold'), fg='white', width=14)
        btn_search.grid(row=0, column=3, padx=5)

        btn_ShowAll = Button(search_frame, bg='blue', text="Show All", command=self.fetch_data, font=(
            'arial', 11, 'bold'), fg='white', width=14)
        btn_ShowAll.grid(row=0, column=4, padx=5)

        # =========== Citizen table===========

        # Table frame
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=48, width=1230, height=130)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.citizen_table = ttk.Treeview(table_frame, column=("citizen_id", "citizen_name", "citizen_age", "citizen_dob", "citizen_phone", "citizen_aadhar", "citizen_pan",
                                          "citizen_occupation", "citizen_disability", "citizen_city", "citizen_bank_accno", "citizen_bank_ifsc"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.citizen_table.xview)
        scroll_y.config(command=self.citizen_table.yview)

        self.citizen_table.heading('citizen_id', text='ID')
        self.citizen_table.heading('citizen_name', text='Name')
        self.citizen_table.heading('citizen_age', text='Age')
        self.citizen_table.heading('citizen_dob', text='DOB')
        self.citizen_table.heading('citizen_phone', text='Phone No')
        self.citizen_table.heading('citizen_aadhar', text='Aadhar')
        self.citizen_table.heading('citizen_pan', text='PAN')
        self.citizen_table.heading('citizen_occupation', text='Occupation')
        self.citizen_table.heading('citizen_disability', text='Disability')
        self.citizen_table.heading('citizen_city', text='City')
        self.citizen_table.heading('citizen_bank_accno', text='Bank Acc No')
        self.citizen_table.heading('citizen_bank_ifsc', text='IFSC Code')
        # self.citizen_table.heading('country', text='Country')
        # self.citizen_table.heading('salary', text='Salary')

        self.citizen_table['show'] = 'headings'
        self.citizen_table.column('citizen_id', width=100)
        self.citizen_table.column('citizen_name', width=100)
        self.citizen_table.column('citizen_age', width=100)
        self.citizen_table.column('citizen_dob', width=100)
        self.citizen_table.column('citizen_phone', width=100)
        self.citizen_table.column('citizen_aadhar', width=100)
        self.citizen_table.column('citizen_pan', width=100)
        self.citizen_table.column('citizen_occupation', width=100)
        self.citizen_table.column('citizen_disability', width=100)
        self.citizen_table.column('citizen_city', width=100)
        self.citizen_table.column('citizen_bank_accno', width=100)
        self.citizen_table.column('citizen_bank_ifsc', width=100)
        # self.citizen_table.column('country', width=100)
        # self.citizen_table.column('salary', width=100)

        self.citizen_table.pack(fill=BOTH, expand=1)

        self.citizen_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # *************Function Declarations****************

    def add_data(self):
        # if self.var_id.get()=="" or self.var_bankacc.get()=="":
        #     messagebox.showerror('Error','All Fields are required')
        # else:
        try:
            conn = mysql.connector.connect(
                host='localhost', username='root', password='2424', database='govfund')
            my_cursor = conn.cursor()
            self.var_id = 13
            my_cursor.execute('insert into citizen values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (

                # Variables
                13,
                self.var_name.get(),
                12,
                self.var_dob.get(),
                self.var_phone.get(),
                self.var_aadhar.get(),
                self.var_pan.get(),
                self.var_occupation.get(),
                self.var_disability.get(),
                self.var_city.get(),
                self.var_bankacc.get(),
                self.var_bankifsc.get(),



            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                'Success', 'citizen has been addded!', parent=self.root)

        except Exception as es:
            messagebox.showerror(
                'Error', f'Due to:{str(es)}', parent=self.root)

    # Fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', username='root', password='2424', database='govfund')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from citizen')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.citizen_table.delete(*self.citizen_table.get_children())
            for i in data:
                self.citizen_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor

    def get_cursor(self, event=""):
        cursor_row = self.citizen_table.focus()
        content = self.citizen_table.item(cursor_row)
        data = content['values']

        # self.var_id.get(),
        self.var_name.set(data[1])
        self.var_aadhar.set(data[5])
        self.var_bankacc.set(data[10])
        self.var_city.set(data[9])
        self.var_occupation.set(data[7])
        self.var_dob.set(data[3])
        self.var_bankifsc.set(data[11])
        # self.var_email.set()
        # self.var_gender.set()
        self.var_pan.set(data[6])
        self.var_phone.set(data[4])
        self.var_disability.set(data[8])
        self.var_age.set(data[2])

    def update_data(self):
        # if self.var_id.get()=="" or self.var_bankacc.get()=="":
        #     messagebox.showerror('Error','All Fields are required')
        # else:
        try:

            update = messagebox.askyesno(
                'Update', 'Are you sure to update this citizen data?')
            if update > 0:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='2424', database='govfund')
                my_cursor = conn.cursor()
                my_cursor.execute('update citizen set citizen_name=%s,citizen_age=%s,citizen_dob=%s,citizen_phone=%s,citizen_aadhar=%s,citizen_pan=%s,citizen_occupation=%s,citizen_disability=%s,citizen_city=%s,citizen_bank_accno=%s,citizen_bank_ifsc=%s where citizen_aadhar=%s', (
                ))

            else:
                if not update:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                'Success', 'Citizen Successfully Updated!', parent=self.root)

        except Exception as es:
            messagebox.showerror(
                'Error', f'Due to:{str(es)}', parent=self.root)

    # Delete

    def delete_data(self):
        # if self.var_pan.get()=="":
        #     messagebox.showerror('Error','All fields are required')
        # else:
        try:
            Delete = messagebox.askyesno(
                'Delete', 'Are you sure to delete this citizen data?', parent=self.root)
            if Delete > 0:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='2424', database='govfund')
                my_cursor = conn.cursor()
                sql = 'delete from citizen where citizen_aadhar=%s'
                value = (self.var_pan.get(),)
                my_cursor.execute(sql, value)
            else:
                if not Delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                'Delete', 'citizen Successfully Deleted!', parent=self.root)

        except Exception as es:
            messagebox.showerror(
                'Error', f'Due to:{str(es)}', parent=self.root)

    # Clear

    def reset_data(self):

        self.var_name.set("")
        self.var_aadhar.set("")
        self.var_bankacc.set("")
        self.var_city.set("")
        self.var_occupation.set("")
        self.var_dob.set("")
        self.var_bankifsc.set("")
        # self.var_email.set()
        # self.var_gender.set()
        self.var_pan.set("")
        self.var_phone.set("")
        self.var_disability.set(Y)
        self.var_age.set("")

    # Search
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror('Error', 'Please Select Option')
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='2424', database='govfund')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from citizen where ' + str(
                    self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get() + "%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.citizen_table.delete(
                        *self.citizen_table.get_children())
                    for i in rows:
                        self.citizen_table.insert("", END, values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    'Error', f'Due to:{str(es)}', parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Citizen(root)
    root.mainloop()
