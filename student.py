from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self, root):
        # --------------  Program window --------------------------
        self.root = root
        self.root.geometry('1480x800+40+10')  # Program dimensions
        self.root.title('School management program')  # Project Title
        self.root.resizable(False, False)  # screen's lock
        self.root.configure(background='silver')  # Background color
        title = Label(self.root,
                      text='student registration',
                      bg='#15FDB3',
                      font=('monospace', 14, 'bold'),
                      fg='#318969'
                      )
        title.pack(fill=X)
        # ----------------- Variable ------------------------------
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.del_var = StringVar()
        self.qualifi_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.address_var = StringVar()
        self.search_by = StringVar()
        self.search_var = StringVar()
        # ----------------- Program control tools ---------------------
        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=1269, y=29, width=210, height=450)
        # -------------------------id----------------
        lbl_id = Label(manage_frame, bg='white', text=' Id user', font=12)
        lbl_id.pack()
        id_entry = Entry(manage_frame, textvariable=self.id_var, bd='3', bg='silver', justify='center')
        id_entry.pack()
        # --------------------name ---------------
        lbl_name = Label(manage_frame, text='Name student ', bg='white', font=(14))
        lbl_name.pack()
        name_entery = Entry(manage_frame, textvariable=self.name_var, bd='3', bg='silver', justify='center')
        name_entery.pack()
        # -------------------- email --------------
        lbl_email = Label(manage_frame, text='Email student', font=(14), bg='white')
        lbl_email.pack()
        email_entery = Entry(manage_frame, textvariable=self.email_var, bd='3', bg='silver', justify='center')
        email_entery.pack()
        # -------------------- phone student ------------
        lbl_phone = Label(manage_frame, bg='white', text='phone student', font=(14))
        lbl_phone.pack()
        phone_entery = Entry(manage_frame, textvariable=self.phone_var, bd='3', bg="silver", justify='center')
        phone_entery.pack()
        # -------------------- Student qualifications ------------------
        lbl_qualifi = Label(manage_frame, bg='white', text='Student qualifications', font=(14))
        lbl_qualifi.pack()
        qualifi_entery = Entry(manage_frame, textvariable=self.qualifi_var, bd='3', bg="silver", justify='center')
        qualifi_entery.pack()
        # ---------------------- gender student --------------------------
        lbl_gender = Label(manage_frame, text='gender student', font=(14), bg='white')
        lbl_gender.pack()
        combo_gender = ttk.Combobox(manage_frame, width=17, textvariable=self.gender_var)
        combo_gender['value'] = ('male', 'female')
        combo_gender.pack()
        # --------------------- address student ---------------------------
        lbl_address = Label(manage_frame, bg='white', text='address student', font=(14))
        lbl_address.pack()
        address_entry = Entry(manage_frame, textvariable=self.address_var, bd='3', bg='silver', justify='center')
        address_entry.pack()
        # ------------------- botten del -------------------------------
        lbl_del = Label(manage_frame, fg='red', bg='white', text='Delete the student name')
        lbl_del.pack()
        del_entry = Entry(manage_frame, textvariable=self.del_var, bd='3', bg='silver', justify='center')
        del_entry.pack()

        # ------------------------- Programming the buttons ------------
        botton_frame = Frame(self.root, bg='white')
        botton_frame.place(x=1269, y=485, width=210, height=310)
        title1 = Label(botton_frame, text='control Board', font=('deco', 14), bg='#2327FE', fg='white')
        title1.pack(fill=X)
        # ----------------  ADD_BOTTEN -----------------
        add_but = Button(botton_frame, bg='#01FC18', text='add', fg="white", font=(22), command=self.add_student)
        add_but.place(x=20, y=40, width=170, height=30)

        del_but = Button(botton_frame, bg='#FC0101', text='delete', fg="white", font=(22), command=self.del_student)
        del_but.place(x=20, y=80, width=170, height=30)

        update_but = Button(botton_frame, bg='#013AFC', text='update', fg="white", font=(22),command=self.update_student)
        update_but.place(x=20, y=120, width=170, height=30)

        clear_but = Button(botton_frame, bg='#404040', text='clear', fg="white", font=(22), command=self.cle_student)
        clear_but.place(x=20, y=160, width=170, height=30)

        about_but = Button(botton_frame, bg='#84A554', text='about', fg="white", font=(22),command=self.about)
        about_but.place(x=20, y=200, width=170, height=30)

        exit_but = Button(botton_frame, bg='black', text='exit', fg="white", font=(22),command=root.quit)
        exit_but.place(x=20, y=240, width=170, height=30)
        # ----------------- search mange ---------------
        search_frame = Frame(self.root, bg='white')
        search_frame.place(x=1, y=29, width=1270, height=50)
        # ------------------
        lbl_Search = Label(search_frame, bg='white', text='search a student', font=('deco', 12, 'bold'))
        lbl_Search.place(x=1, y=12)
        combo_search = ttk.Combobox(search_frame, justify='center',textvariable=self.search_by)
        combo_search['value'] = ('ID', 'name')
        combo_search.place(x=150, y=15)

        search_enter = Entry(search_frame, textvariable=self.search_var, justify='left', bg='silver', bd='3')
        search_enter.place(x=300, y=15)
        search_botton = Button(search_frame, text='search', bg='#FFE400', fg='white', command=self.search_student)
        search_botton.place(x=445, y=13, width=100, height=25)
        # ---------------------- Database ----------------------
        database_frame = Frame(self.root, bg='#D0CBCB')
        database_frame.place(x=0, y=80, width=1268, height=719)
        # ----------------------- scroll ------------------
        scroll_x = Scrollbar(database_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(database_frame, orient=VERTICAL)
        # -----------------------   tree view -------
        self.student_table = ttk.Treeview(database_frame,
                                          columns=(
                                          'ID', 'Name', 'Email', 'address', 'qualifications', 'Phone', 'Gender'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        self.student_table.place(x=18, y=1, width=1260, height=700)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
        self.student_table['show'] = 'headings'
        self.student_table.heading('ID', text='ID')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('address', text='address')
        self.student_table.heading('qualifications', text='qualifications')
        self.student_table.heading('Phone', text='Phone')
        self.student_table.heading('Gender', text='Gender')

        self.student_table.column('ID', width=80)
        self.student_table.column('Name', width=80)
        self.student_table.column('Email', width=80)
        self.student_table.column('address', width=80)
        self.student_table.column('qualifications', width=80)
        self.student_table.column('Phone', width=80)
        self.student_table.column('Gender', width=80)
        self.student_table.bind("<ButtonRelease-1>", self.get_curser)
        # --------- cont add ----------------------
        self.fetch_all()

    def add_student(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='student')
        cur = con.cursor()
        cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s)',
                    (self.id_var.get(),
                     self.name_var.get(),
                     self.email_var.get(),
                     self.phone_var.get(),
                     self.qualifi_var.get(),
                     self.gender_var.get(),
                     self.address_var.get(),

                     ))

        con.commit()
        self.fetch_all()
        self.cle_student()
        con.close()

    def fetch_all(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='student'
        )
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def del_student(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='student'
        )
        cur = con.cursor()
        cur.execute('delete from student where  Name = %s', (self.del_var.get()))
        con.commit()
        self.fetch_all()
        con.close()

    def cle_student(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.gender_var.set('')
        self.qualifi_var.set('')
        self.address_var.set('')

    def get_curser(self, ev):
        cursor_row = self.student_table.focus()
        contans = self.student_table.item(cursor_row)
        row = contans['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.phone_var.set(row[3])
        self.qualifi_var.set(row[4])
        self.gender_var.set(row[5])
        self.address_var.set(row[6])

    def update_student(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='student'
        )
        cur = con.cursor()
        cur.execute(
            'UPDATE student set name=%s, email=%s, phone=%s, qualifi=%s, gender=%s, address=%s Where id=%s',
            (self.name_var.get(),
             self.email_var.get(),
             self.phone_var.get(),
             self.qualifi_var.get(),
             self.gender_var.get(),
             self.address_var.get(),
             self.id_var.get()
             ))

        con.commit()
        self.fetch_all()
        self.cle_student()
        con.close()

    def search_student(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='student'
        )
        cur = con.cursor()
        cur.execute("select * from student where " +
        str(self.search_by.get())+ " LIKE '%" + str(self.search_var.get()) +"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def about(self):
        messagebox.showinfo('developer ahmed ayman','welcome tow our project ')


root = Tk()
ob = Student(root)
root.mainloop()
