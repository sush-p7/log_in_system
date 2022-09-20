from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3 as sq


class logInForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        # self.window.state('zoomed')
        self.window.resizable(1,1)

        # background image
        self.bg_frame = Image.open('img\image.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg__panel = Label(self.window, image=photo)
        self.bg__panel.image = photo
        self.bg__panel.pack(fill='both', expand='no')

        # =============login frame=============
        self.log_fram = Frame(self.window, bg='#05204d', width='950', height='600')
        self.log_fram.place(x=300, y=100)

        self.txt = 'WELCOME'
        self.heading = Label(self.log_fram, text=self.txt,font=('yu gothic ui', 25, 'bold') , bg='#05204d', fg='white')
        self.heading.place(x=100, y=60, width=300, height=60)

        # background image
        # ============== left side image ============
        self.side_image = Image.open('img\Artboard1.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.log_fram, image=photo, bg='#05204d')
        self.side_image_label.image = photo
        self.side_image_label.place(x=10, y=110)

        # ============== sigin image ============
        self.sigin_image = Image.open('img\Artboard2.png')
        photo = ImageTk.PhotoImage(self.sigin_image)
        self.sigin_image_label = Label(self.log_fram, image=photo, bg='#05204d')
        self.sigin_image_label.image = photo
        self.sigin_image_label.place(x=640, y=130)

        self.sigin_label = Label(self.log_fram, text='Sign In' , bg='#05204d', fg='white', font=('yu gothic ui', 18, 'bold'))
        self.sigin_label.place(x=650, y=240)

        # ========= Username ==========
        self.user_name = Label(self.log_fram, text='Username', bg='#05204d', fg='white', font=('yu gothic ui', 14, 'bold'))
        self.user_name.place(x=550, y=300)

        self.user_n = Entry(self.log_fram, highlightthickness=0, relief=FLAT, bg='#05204d', fg='white', font=('yu gothic ui', 12, 'bold'))
        self.user_n.place(x=580, y=330, width=270)

        self.user_line = Canvas(self.log_fram, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.user_line.place(x=550, y=359, width=300)

        # ========== use icon =====================
        self.user_icon = Image.open('img/User.png')
        photo = ImageTk.PhotoImage(self.user_icon)
        self.user_icon_label = Label(self.log_fram, image=photo, bg='#05204d')
        self.user_icon_label.image = photo
        self.user_icon_label.place(x=550, y=325)

        # ========= lock ==========
        self.user_name = Label(self.log_fram, text='Password', bg='#05204d', fg='white',
                               font=('yu gothic ui', 14, 'bold'))
        self.user_name.place(x=550, y=362)

        self.user_p = Entry(self.log_fram, highlightthickness=0, relief=FLAT, bg='#05204d', fg='white',
                                font=('yu gothic ui', 12, 'bold'), show='*')
        self.user_p.place(x=580, y=391, width=220)

        self.password_line = Canvas(self.log_fram, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=420, width=300)

        # ========== lock icon =====================
        self.user_icon = Image.open('img\lock.png')
        photo = ImageTk.PhotoImage(self.user_icon)
        self.user_icon_label = Label(self.log_fram, image=photo, bg='#05204d')
        self.user_icon_label.image = photo
        self.user_icon_label.place(x=550, y=388)

        # ================= log in ======================
        self.login_button = Image.open('img/Art.png')
        photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.log_fram, image=photo, bg='#05204d')
        self.login_button_label.image = photo
        self.login_button_label.place(x=550, y=440)

        self.loginW = Button(self.login_button_label, text='Log In', font=('yu gothic ui', 14, 'bold'), width=23, bd=0, bg='#ef95b3',
                            cursor='hand2', activebackground='#ef95b3', fg='white', command = lambda : self.login(window))
        # self.login.configure(command=lambda :self.log_in_suc(window))
        self.loginW.place(x=8, y=7)

        # ===================== forget password ==================4
        self.forget_button = Button(self.log_fram, text='Forgot Password ?', font=('yu gothic ui', 12, 'bold underline'), fg='white', width=0, bd=0,
                                    bg='#05204d', activebackground='#05204d',cursor='hand2', command=self.forget_pass)
        self.forget_button.place(x=620, y=500)

        # ======================= sign in =====================
        self.sign_button = Button(self.log_fram, text='Sign in Here !!',
                                    font=('yu gothic ui', 14, 'bold'), fg='#ef95b3', width=23, bd=0,
                                    bg='#05204d', activebackground='#05204d', cursor='hand2',command=lambda :self.creatsingin(window))
        self.sign_button.place(x=560, y=530)

        # ================ hind and show password ==============
        self.show_button = Image.open('img\show.png')
        self.photo1 = ImageTk.PhotoImage(self.show_button)

        self.show_button = Button(self.log_fram, image=self.photo1, bg='pink', activebackground='pink', cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=805, y=391)

        self.hide_button = Image.open('img\hide.png')
        self.photo = ImageTk.PhotoImage(self.hide_button)

        # self.hide_button = Button(self.log_fram, image=photo, bg='pink', activebackground='pink', cursor='hand2', bd=0)
        # self.hide_button.image = photo
        # self.hide_button.place(x=805, y=391)

    def show(self):
        self.hide_button = Button(self.log_fram, image=self.photo, bg='pink', activebackground='pink', cursor='hand2',
                                  bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=805, y=391)
        self.user_p.config(show='')

    def hide(self):
        self.show_button = Button(self.log_fram, image=self.photo1, bg='pink', activebackground='pink', cursor='hand2', bd=0,
                                  command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=805, y=391)
        self.user_p.config(show='*')

    def login(self,window):
        window = window
        username = self.user_n.get()
        password = self.user_p.get()
        db = sq.connect('DB\login.db')
        # db.execute('CREATE TABLE IF NOT EXISTS login(username_db TEXT, password_db TEXT)')
        # db.execute("INSERT INTO login(username,password) VALUES (username,password)")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM loginTable where username_db = ? AND password_db = ?", (self.user_n.get(), self.user_p.get()))
        row = cursor.fetchone()
        if row:
            if self.user_n.get()==''or self.user_p.get()=='':
                messagebox.showinfo('info', ' login failed')
                return
            self.log_in_suc(window)
        else:
            messagebox.showinfo('info', ' login failed')



    def creatsingin(self,window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        # background image
        self.bg_frame = Image.open('img\image.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg__panel = Label(self.window, image=photo)
        self.bg__panel.image = photo
        self.bg__panel.pack(fill='both', expand='no')

        # =============login frame=============
        self.log_fram = Frame(self.window, bg='#05204d', width='950', height='600')
        self.log_fram.place(x=300, y=90)

        self.txt = 'Enter Your Details Here !'
        self.heading = Label(self.log_fram, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#05204d', fg='white')
        self.heading.place(x=100, y=50, width=400, height=60)

        # background image
        # ============== left side image ============
        # self.side_image = Image.open('Artboard1.png')
        # photo = ImageTk.PhotoImage(self.side_image)
        # self.side_image_label = Label(self.log_fram, image=photo, bg='#05204d')
        # self.side_image_label.image = photo
        # self.side_image_label.place(x=10, y=110)

        # ==================== accepting user details ================
        # ===================== name ==========================
        self.user_name = Label(self.log_fram, text='Name', bg='#05204d', fg='white',
                               font=('yu gothic ui', 14, 'bold'))
        self.user_name.place(x=100, y=105)

        self.user_o_name = Entry(self.log_fram, highlightthickness=0, relief=FLAT, bg='#05204d', fg='white',
                            font=('yu gothic ui', 12, 'bold'))
        self.user_o_name.place(x=100, y=140, width=220)

        self.user_o_name_line = Canvas(self.log_fram, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.user_o_name_line.place(x=100, y=160, width=300)
        # ===================== age =====================

        self.user_name = Label(self.log_fram, text='Age', bg='#05204d', fg='white',
                               font=('yu gothic ui', 14, 'bold'))
        self.user_name.place(x=100, y=170)

        self.user_o_age = Entry(self.log_fram, highlightthickness=0, relief=FLAT, bg='#05204d', fg='white',
                                 font=('yu gothic ui', 12, 'bold'))
        self.user_o_age.place(x=100, y=205, width=220)

        self.user_o_age_line = Canvas(self.log_fram, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.user_o_age_line.place(x=100, y=225, width=300)

        # ============================ username ====================
        self.user_name = Label(self.log_fram, text='Username', bg='#05204d', fg='white',
                               font=('yu gothic ui', 14, 'bold'))
        self.user_name.place(x=100, y=235)

        self.user_name_db = Entry(self.log_fram, highlightthickness=0, relief=FLAT, bg='#05204d', fg='white',
                                font=('yu gothic ui', 12, 'bold'))
        self.user_name_db.place(x=100, y=270, width=220)

        self.user_name_db_line = Canvas(self.log_fram, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.user_name_db_line.place(x=100, y=290, width=300)

        # ============================ username password ====================
        self.user_name = Label(self.log_fram, text='Password', bg='#05204d', fg='white',
                               font=('yu gothic ui', 14, 'bold'))
        self.user_name.place(x=100, y=305)

        self.user_p_db = Entry(self.log_fram, highlightthickness=0, relief=FLAT, bg='#05204d', fg='white',
                                  font=('yu gothic ui', 12, 'bold'))
        self.user_p_db.place(x=100, y=340, width=220)

        self.user_p_db_line = Canvas(self.log_fram, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.user_p_db_line.place(x=100, y=360, width=300)

        # ================================= confirm password ====================
        self.user_name = Label(self.log_fram, text='Confirm Password', bg='#05204d', fg='white',
                               font=('yu gothic ui', 14, 'bold'))
        self.user_name.place(x=100, y=370)

        self.user_cp_db = Entry(self.log_fram, highlightthickness=0, relief=FLAT, bg='#05204d', fg='white',
                                  font=('yu gothic ui', 12, 'bold'), show='*')
        self.user_cp_db.place(x=100, y=405, width=220)

        self.user_cp_db_line = Canvas(self.log_fram, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.user_cp_db_line.place(x=100, y=425, width=300)

        # ============================== phone number =======================
        self.user_name = Label(self.log_fram, text='Phone Number', bg='#05204d', fg='white',
                               font=('yu gothic ui', 14, 'bold'))
        self.user_name.place(x=100, y=440)

        self.user_num_db = Entry(self.log_fram, highlightthickness=0, relief=FLAT, bg='#05204d', fg='white',
                                font=('yu gothic ui', 12, 'bold'))
        self.user_num_db.place(x=100, y=470, width=220)

        self.user_num_db_line = Canvas(self.log_fram, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.user_num_db_line.place(x=100, y=490, width=300)

        # ============================== register =====================
        self.login_button = Image.open('img\Art.png')
        photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.log_fram, image=photo, bg='#05204d')
        self.login_button_label.image = photo
        self.login_button_label.place(x=550, y=440)

        self.loginR = Button(self.login_button_label, text='Register', font=('yu gothic ui', 14, 'bold'), width=23, bd=0,
                            bg='#ef95b3',
                            cursor='hand2', activebackground='#ef95b3', fg='white', command =lambda :self.refister(window))
        # self.login.configure(command= lambda :self.log_in_suc(window))
        self.loginR.place(x=8, y=7)
        # ============== right side image ============
        self.side_image = Image.open('img\Artboard1.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.log_fram, image=photo, bg='#05204d')
        self.side_image_label.image = photo
        self.side_image_label.place(x=500, y=0)

    def refister(self,window):
        window = window
        try:
            o_name = self.user_o_name.get()
            o_age = self.user_o_age.get()
            if self.user_p_db.get() == self.user_cp_db.get():
                o_password = self.user_cp_db.get()
            else:
                messagebox.showinfo('Error', 'Dose not match the password')
                return
            o_phone = self.user_num_db.get()
            o_username = self.user_name_db.get()
            print(o_username, o_phone, o_age, o_password, o_name)
        except:
            pass

        def insertVaribleIntoTable(o_username, o_password, o_age, o_name, o_phone):
            try:
                sqliteConnection = sq.connect('DB\login.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")

                sqlite_insert_with_param = """INSERT INTO loginTable
                                  (username_db,password_db,age,name,phone) 
                                  VALUES (?, ?, ?, ?, ?);"""

                data_tuple = (o_username, o_password, o_age, o_name, o_phone)
                cursor.execute(sqlite_insert_with_param, data_tuple)
                sqliteConnection.commit()
                print("Python Variables inserted successfully into SqliteDb_developers table")
                self.log_in_suc(window)
                cursor.close()

            except sq.Error as error:
                print("Failed to insert Python variable into sqlite table", error)
                messagebox.showinfo('error',"Failed to register\n")
                return
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        insertVaribleIntoTable(o_username, o_password, o_age, o_name, o_phone)



    def log_in_suc(self,window):
        # self.refister()
        messagebox.showinfo('info', ' login success')
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        # background image
        self.bg_frame = Image.open('img\image.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg__panel = Label(self.window, image=photo)
        self.bg__panel.image = photo
        self.bg__panel.pack(fill='both', expand='no')

        # =============login frame=============
        self.log_fram = Frame(self.window, bg='#05204d', width='950', height='600')
        self.log_fram.place(x=300, y=90)

        self.txt = 'Finally You Log In'
        self.heading = Label(self.log_fram, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#05204d', fg='white')
        self.heading.place(x=250, y=50, width=400, height=60)

        # ======================= log in suc msg ===================
        self.txt = 'Hey my name is Sush,\nAnd this system is created by me\nHope you like it.'
        self.heading = Label(self.log_fram, text=self.txt, font=('yu gothic ui', 18, 'bold'), bg='#05204d', fg='white')
        self.heading.place(x=200, y=250, width=500)

    def forget_pass(self):
        messagebox.showinfo('notice','Still under development')



def page():
    window = Tk()
    logInForm(window)
    window.title("Log In Page")
    window.mainloop()


if __name__ == '__main__':
    page()

