import tkinter as tk
from tkinter import *
import tkinter.messagebox
import sqlite3
import Base
import Payment
import time


FONT = "Calibiri"
FONTSIZE = "12"


class Authentication(tk.Frame):

    def __init__(self, master=None):

        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.title("Workouts by Karo")
        self.parent.config(bg='light pink')
        self.width = 440
        self.height = 350
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.parent.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))
        self.parent.resizable(0, 0)
        self.addBaseMenu()
        self.editMenu()
        self.startFrame()

#stworzenie paska menu
    def addBaseMenu(self):
        self.menubar = tk.Menu(self.parent, background='light pink')
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                (None, None, None, None),
                ("Wyjście", self.exit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0, command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Menu", menu=fileMenu, underline=0)

#stworzenie paska edycja
    def editMenu(self):
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                (None, None, None, None),
                ("Wyczyść luki", self.clearFields, "Ctrl+N", "<Control-n>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                                     command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Edycja", menu=fileMenu, underline=0)
        pass


#czyszczenie pól - entry
    def clearFields(self, event=None):
        event = event
        [self.robocze.children[x].delete(0, 'end') for x in self.robocze.children if 'entry' in x]
        pass

#połaczenie  z bazą danych
    def database(self):
        self.conn = sqlite3.connect("members.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")


#ramka startowa z wyborem logowania lub rejestracji
    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=35)
        self.StartWindow = self.robocze
        self.label_welcome = tk.Label(self.StartWindow, text=" WORKOUTS BY", font=('Calibiri', 25),background='light pink', fg= "white")
        self.label_welcome.grid(row=0)
        self.label_name = tk.Label(self.StartWindow, text=" Karo", font=('Calibiri', 45, 'italic'),background='light pink', fg= "white")
        self.label_name.grid(row=1)
        self.button_login = Button(self.StartWindow, text="Logowanie", font=(FONT, FONTSIZE), width=35, command=self.toggleToLoginS, background='black', fg= "white")
        self.button_login.grid(row=6, columnspan=2, pady=30)
        self.button_register = Button(self.StartWindow, text="Rejestracja", font=(FONT, FONTSIZE), width=35, command=self.toggleToRegisterS, background='black', fg= "white")
        self.button_register.grid(row=7, columnspan=2)


#ramka logowania
    def loginFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP)

        self.LoginWindow = self.robocze
        self.parent.title("Logowanie")


        self.username = StringVar()
        self.password = StringVar()


        self.label_username = tk.Label(self.LoginWindow, text="Login", font=(FONT, FONTSIZE), background='light pink')
        self.label_username.grid(column=0, row=2, pady =20)
        self.entry_username = tk.Entry(self.LoginWindow, textvariable=self.username, width=30, font=(FONT, 10))
        self.entry_username.grid(column=1, row=2, pady =20)
        self.label_password = tk.Label(self.LoginWindow, text="Hasło", font=(FONT, FONTSIZE), background='light pink')
        self.label_password.grid(column=0, row=3)
        self.entry_password = tk.Entry(self.LoginWindow, textvariable=self.password, width=30, show='*', font=(FONT, 10))
        self.entry_password.grid(column=1, row=3)
        self.label_result1 = Label(self.LoginWindow, text="", font=(FONT, FONTSIZE),  background='light pink')
        self.label_result1.grid(row=6, columnspan=2)

        self.button_login = Button(self.LoginWindow, text="Zaloguj się", font=(FONT, FONTSIZE), width=35, command=self.login, background='black', fg= "pink")
        self.button_login.grid(row=5, columnspan=2, pady=40)
        self.label_register = Label(self.LoginWindow, text="Zarejestruj się", font=(FONT, FONTSIZE), background='black', fg="pink")
        self.label_register.grid(row=0, pady=30)
        self.label_register.bind('<Button-1>', self.toggleToRegister)



#ramka rejestracji
    def registerFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP)

        self.RegisterWindow = self.robocze
        self.parent.title("Rejestracja")

        self.username = StringVar()
        self.password = StringVar()
        self.checkPassword = StringVar()

        self.label_username = tk.Label(self.RegisterWindow, text="Login", font=(FONT, FONTSIZE), background='light pink')
        self.label_username.grid(column=0, row=2)
        self.entry_username = tk.Entry(self.RegisterWindow, textvariable=self.username, width=30, font=(FONT, 10))
        self.entry_username.grid(column=1, row=2)
        self.label_password = tk.Label(self.RegisterWindow, text="Hasło", font=(FONT, FONTSIZE), background='light pink')
        self.label_password.grid(column=0, row=3, pady=20)
        self.entry_password = tk.Entry(self.RegisterWindow, textvariable=self.password, width=30, font=(FONT, 10), show='*')
        self.entry_password.grid(column=1, row=3, pady=20)
        self.label_firstName = tk.Label(self.RegisterWindow, text="Powtórz hasło", font=(FONT, FONTSIZE), background='light pink')
        self.label_firstName.grid(column=0, row=4)
        self.entry_firstName = tk.Entry(self.RegisterWindow, textvariable=self.checkPassword, width=30, font=(FONT, 10), show="*")
        self.entry_firstName.grid(column=1, row=4)
        self.label_result2 = Label(self.RegisterWindow, text="", font=(FONT, FONTSIZE), background='light pink')
        self.label_result2.grid(row=6, columnspan=2)

        self.button_register = Button(self.RegisterWindow, text="Zarejestruj się", font=(FONT, FONTSIZE), width=35,
                                      command=self.register, background='black',fg= 'light pink')
        self.button_register.grid(row=5, columnspan=2, pady=30)
        self.label_login = Label(self.RegisterWindow, text="Zaloguj się", fg="light pink", font=(FONT, FONTSIZE), background='black')
        self.label_login.grid(row=0, sticky=W, pady=30)
        self.label_login.bind('<Button-1>', self.toggleToLogin)

#koniec programu
    def exit(self):
        result = tk.messagebox.askquestion('System', 'Jesteś pewny/a, że chcesz wyjść?', icon="warning")
        if result == 'yes':
            self.parent.destroy()
            exit()

#zamknięcie okna rejstracji i uruchomienie okna logowanie
    def toggleToLogin(self, event=None):
        self.RegisterWindow.destroy()
        self.loginFrame()

#zamknięcie okna logowanie i uruchomienie okna rejestracji
    def toggleToRegister(self, event=None):
        self.LoginWindow.destroy()
        self.registerFrame()

#zamknięcie startowego okna i uruchomienie okna logowania
    def toggleToLoginS(self, event=None):
        self.StartWindow.destroy()
        self.loginFrame()

#zamknięcie startowego okna i uruchomienie okna rejestracji
    def toggleToRegisterS(self, event=None):
        self.StartWindow.destroy()
        self.registerFrame()

#rejestracaja - sprawdzenie poprawności wpisywanych danych, a następnie wpisanie ich do bazy danych i uruchomienie okna płatność
    def register(self):
        self.database()
        if self.username.get == "" or self.password.get() == "" or self.checkPassword.get() == "":
            self.label_result2.config(text="Proszę uzupełnienie danych!", fg="blue")
        elif not self.checkPasswd(self.password.get()):
            self.label_result2.config(
                text="Niepoprawne hasło! - min 6 znaków\nduża i mała litera, liczba , znak specajlny", fg="red")
        elif self.password.get() != self.checkPassword.get():
            self.label_result2.config(text="Hasła różnią się!", fg="red")
        else:
            self.cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (self.username.get(),))
            if self.cursor.fetchone() is not None:
                self.label_result2.config(text="Użytkownik o takim loginie już istnieje", fg="red")
                self.cursor.close()
                self.conn.close()
            else:
                self.cursor.execute("INSERT INTO `member` (username, password) VALUES(?, ?)",
                               (str(self.username.get()), str(self.password.get())))
                self.conn.commit()
                self.label_result2.config(text="Rejestracja przebiegła pomyślnie!", fg="green")
                self.cursor.close()
                self.conn.close()
                self.parent.destroy()
                Payment.startPayment(self.username.get())


#sprawdzenie poprawności hasła
    def checkPasswd(self, password):
        low = 0
        big = 0
        sign = False
        number = 0
        counter = 0
        listOfSigns = ["!", "@", "#", "$", "%", "&", "_", "-"]
        for letter in password:
            counter += 1
            if letter.isupper():
                big = 1
            elif letter in listOfSigns:
                sign = True
            elif letter.islower():
                low = 1

        for letter in password:
            try:
                number += 1
                letter = int(letter)
            except:
                number -= 1

        if big == 1 and low == 1 and sign and number >=1 and counter >= 6:
            return True
        else:
            return False

#sprawdzenie, czy dany użytkownik już opłacił dostęp
    def checkPayment(self):
        self.database()
        self.cursor.execute("SELECT * FROM `payment` WHERE `username` = ?", (self.username.get(),))
        if self.cursor.fetchone() is not None:
            self.cursor.close()
            self.conn.close()
            Base.startBase(self.username.get())
        else:
            self.cursor.close()
            self.conn.close()
            Payment.startPayment(self.username.get())

#logowanie, połączenie z bazą danych
    def login(self):
        self.database()
        if self.username.get == "" or self.password.get == "":
            self.label_result1.config(text="Proszę o uzupełnienie danych!", fg="blue")
        else:
            self.cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",
                           (self.username.get(), self.password.get()))
            if self.cursor.fetchone() is not None:
                self.label_result1.config(text="Logowanie przebiegło pomyślnie", fg="green")
                self.cursor.close()
                self.conn.close()
                self.parent.destroy()
                self.checkPayment()
            else:
                self.label_result1.config(text="Nieprawidłowy login lub hasło", fg="red")
                self.cursor.close()
                self.conn.close()

#uruchomienie autoryzacji
def start():
    root = tk.Tk()
    app = Authentication(master=root)
    app.mainloop()
    pass

