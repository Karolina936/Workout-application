import tkinter as tk
from tkinter import *
import tkinter.messagebox
import sqlite3
import Base
import Authentication

FONT = "Calibiri"
FONTSIZE = "13"
priority = 0
username = ""

class Account(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.title("Konto")
        self.parent.config(bg='light pink')
        self.width = 550
        self.height = 570
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.parent.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))
        self.parent.resizable(0, 0)
        self.addBaseMenu()
        self.baseAccount()
        self.editMenu()

#dodanie paska menu
    def addBaseMenu(self):
        self.menubar = tk.Menu(self.parent, background='light pink')
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("Wyjście", self.exit, "Ctrl+Q", "<Control-q>"),
                (None, None, None, None),
                ("Wyloguj się", self.toogleToLogin, "Ctrl+X", "<Control-x>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0, command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Menu", menu=fileMenu, underline=0)

#dodanie paska edycja
    def editMenu(self):
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("Wyczyść luki", self.clearFields, "Ctrl+N", "<Control-n>"),
                (None, None, None, None),
                ("Zmień hasło", self.toogleToChange, "Ctrl+A", "<Control-a>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                                     command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Edycja", menu=fileMenu, underline=0)
        pass


#wyjście z aplikacji
    def exit(self):
        result = tk.messagebox.askquestion('System', 'Jesteś pewny/a, że chcesz wyjść?', icon="warning")
        if result == 'yes':
            self.parent.destroy()
            exit()

#wyłączenie okna startowego i włączenie okna autoryzacji (wylogowanie)
    def toogleToLogin(self):
        self.parent.destroy()
        Authentication.start()

#wyczyszczenie pól - entry
    def clearFields(self, event=None):
        event = event
        [self.robocze.children[x].delete(0, 'end') for x in self.robocze.children if 'entry' in x]
        pass

#stwórzenie startowego okna z polami do wpisania odnośnie statowych i aktualnych pomiarów
    def baseAccount(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP)

        self.Account = self.robocze
        self.parent.title("Konto")


        self.waga = StringVar()
        self.talia = StringVar()
        self.biodra = StringVar()
        self.udo = StringVar()
        self.ramie = StringVar()
        self.lydka = StringVar()
        self.waga2 = StringVar()
        self.talia2 = StringVar()
        self.biodra2 = StringVar()
        self.udo2 = StringVar()
        self.ramie2 = StringVar()
        self.lydka2 = StringVar()


        self.label_username = tk.Label(self.Account, text="Witaj "+username, font=("Calibiri", 25, 'bold italic'),
                                       background='light pink')
        self.label_username.grid(row=0, column=0, columnspan=4,pady=30)
        self.label_start = tk.Label(self.Account, text="Start", font=(FONT, FONTSIZE),
                                   background='light pink')
        self.label_start.grid(column=1, row=2, pady=10, padx=20)
        self.label_obecnie = tk.Label(self.Account, text="Obecnie", font=(FONT, FONTSIZE),
                                    background='light pink')
        self.label_obecnie.grid(column=2, row=2, pady=10, padx=20)
        self.label_waga = tk.Label(self.Account, text="Waga", font=(FONT, FONTSIZE),
                                       background='light pink')
        self.label_waga.grid(column=0, row=3, pady=10, padx = 20)
        self.entry_waga = tk.Entry(self.Account, textvariable=self.waga, width=10, font=(FONT, FONTSIZE))
        self.entry_waga.grid(column=1, row=3, pady=10, padx =20)
        self.entry_waga2 = tk.Entry(self.Account, textvariable=self.waga2, width=10, font=(FONT, FONTSIZE))
        self.entry_waga2.grid(column=2, row=3, pady=10, padx=20)
        self.label_kg = tk.Label(self.Account, text="kg", font=(FONT, FONTSIZE),
                               background='light pink')
        self.label_kg.grid(column=3, row=3, pady=10, padx=20)
        self.label_talia = tk.Label(self.Account, text="Talia", font=(FONT, FONTSIZE),
                                   background='light pink')
        self.label_talia.grid(column=0, row=4, pady=10, padx =20)
        self.entry_talia = tk.Entry(self.Account, textvariable=self.talia, width=10, font=(FONT, FONTSIZE))
        self.entry_talia.grid(column=1, row=4, pady=10, padx =20)
        self.entry_talia2 = tk.Entry(self.Account, textvariable=self.talia2, width=10, font=(FONT, FONTSIZE))
        self.entry_talia2.grid(column=2, row=4, pady=10, padx=20)
        self.label_j = tk.Label(self.Account, text="cm", font=(FONT, FONTSIZE),
                                 background='light pink')
        self.label_j.grid(column=3, row=4, pady=10, padx=20)
        self.label_biodra = tk.Label(self.Account, text="Biodra", font=(FONT, FONTSIZE),
                                    background='light pink')
        self.label_biodra.grid(column=0, row=5, pady=10, padx =20)
        self.entry_biodra = tk.Entry(self.Account, textvariable=self.biodra, width=10, font=(FONT, FONTSIZE))
        self.entry_biodra.grid(column=1, row=5, pady=10, padx =20)
        self.entry_biodra2 = tk.Entry(self.Account, textvariable=self.biodra2, width=10, font=(FONT, FONTSIZE))
        self.entry_biodra2.grid(column=2, row=5, pady=10, padx=20)
        self.label_j2 = tk.Label(self.Account, text="cm", font=(FONT, FONTSIZE),
                                background='light pink')
        self.label_j2.grid(column=3, row=5, pady=10, padx=20)
        self.label_udo = tk.Label(self.Account, text="Udo", font=(FONT, FONTSIZE),
                                     background='light pink')
        self.label_udo.grid(column=0, row=6,pady=10, padx =20)
        self.entry_udo = tk.Entry(self.Account, textvariable=self.udo, width=10, font=(FONT, FONTSIZE))
        self.entry_udo.grid(column=1, row=6,pady=10, padx =20)
        self.entry_udo2 = tk.Entry(self.Account, textvariable=self.udo2, width=10, font=(FONT, FONTSIZE))
        self.entry_udo2.grid(column=2, row=6, pady=10, padx=20)
        self.label_j3 = tk.Label(self.Account, text="cm", font=(FONT, FONTSIZE),
                                background='light pink')
        self.label_j3.grid(column=3, row=6, pady=10, padx=20)
        self.label_ramie = tk.Label(self.Account, text="Ramię", font=(FONT, FONTSIZE),
                                  background='light pink')
        self.label_ramie.grid(column=0, row=7,pady=10, padx =20)
        self.entry_ramie = tk.Entry(self.Account, textvariable=self.ramie, width=10, font=(FONT, FONTSIZE))
        self.entry_ramie.grid(column=1, row=7,pady=10, padx =20)
        self.entry_ramie2 = tk.Entry(self.Account, textvariable=self.ramie2, width=10, font=(FONT, FONTSIZE))
        self.entry_ramie2.grid(column=2, row=7, pady=10, padx=20)
        self.label_j4 = tk.Label(self.Account, text="cm", font=(FONT, FONTSIZE),
                                background='light pink')
        self.label_j4.grid(column=3, row=7, pady=10, padx=20)
        self.label_lydka = tk.Label(self.Account, text="Łydka", font=(FONT, FONTSIZE),
                                   background='light pink')
        self.label_lydka.grid(column=0, row=8,pady=10, padx =20)
        self.entry_lydka = tk.Entry(self.Account, textvariable=self.lydka, width=10, font=(FONT, FONTSIZE))
        self.entry_lydka.grid(column=1, row=8,pady=10, padx =20)
        self.entry_lydka2 = tk.Entry(self.Account, textvariable=self.lydka2, width=10, font=(FONT, FONTSIZE))
        self.entry_lydka2.grid(column=2, row=8, pady=10, padx=20)
        self.label_j5 = tk.Label(self.Account, text="cm", font=(FONT, FONTSIZE),
                                background='light pink')
        self.label_j5.grid(column=3, row=8, pady=10, padx=20)
        self.button_zapisz = Button(self.Account, text="Zapisz", font=(FONT, FONTSIZE),
                              width=35,
                              command=self.saveAll, background='black', fg="pink")
        self.button_zapisz.grid(row=9, column=0,columnspan=4, pady = 25)
        self.label_result2 = Label(self.Account, text="", font=(FONT, FONTSIZE), background='light pink')
        self.label_result2.grid(row=10, columnspan=5)
        self.button_powrot = Button(self.Account, text="Powrót", font=(FONT, FONTSIZE),
                                    width=9,
                                  command=self.toogleToBase, background='black', fg="light pink", bd=0)
        self.button_powrot.grid(column=0, row=2, pady=10, padx=15)

        self.setEntry()
        self.setEntryActually()


#zapisanie wszystkich podanych danych w oknie startowym
    def saveAll(self):
        self.save()
        self.saveActually()

#okno do zmiany hasła
    def changePassword(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP)

        self.Password = self.robocze
        self.parent.title("Zmiana hasła")

        self.password0 = StringVar()
        self.password = StringVar()
        self.password2 = StringVar()


        self.button_powrot = Button(self.Password, text="Konto", font=(FONT, 20), width=20,
                                  command=self.toogleToAccount, background='light pink', fg='black')
        self.button_powrot.grid(row=0, column=0, columnspan=2, pady=50)
        self.label_password0 = tk.Label(self.Password, text="Aktualne hasło", font=(FONT, FONTSIZE),
                                        background='light pink')
        self.label_password0.grid(column=0, row=3, pady=20, padx=10)
        self.entry_password0 = tk.Entry(self.Password, textvariable=self.password0, width=30, font=(FONT, 10),
                                        show='*')
        self.entry_password0.grid(column=1, row=3, pady=20)
        self.label_password = tk.Label(self.Password, text="Nowe hasło", font=(FONT, FONTSIZE),
                                       background='light pink')
        self.label_password.grid(column=0, row=4, pady=20, padx =10)
        self.entry_password = tk.Entry(self.Password, textvariable=self.password, width=30, font=(FONT, 10),
                                       show='*')
        self.entry_password.grid(column=1, row=4, pady=20)
        self.label_password2 = tk.Label(self.Password, text="Powtórz nowe\n hasło", font=(FONT, FONTSIZE),
                                        background='light pink')
        self.label_password2.grid(column=0, row=5,pady=20, padx =10)
        self.entry_password2 = tk.Entry(self.Password, textvariable=self.password2, width=30,
                                        font=(FONT, 10), show="*")
        self.entry_password2.grid(column=1, row=5, pady=20)
        self.label_result2 = Label(self.Password, text="", font=(FONT, FONTSIZE), background='light pink')
        self.label_result2.grid(row=7, columnspan=2)
        self.button_zmien = Button(self.Password, text="Zmień hasło", font=(FONT, FONTSIZE), width=35,
                                   command=self.newPassword, background='black', fg='light pink')
        self.button_zmien.grid(row=6, columnspan=2, pady=30)
        #self.button_powrot = Button(self.Password, text="Powrót", font=(FONT, FONTSIZE), width=20,
        #                           command=self.toogleToAccount, background='black', fg='light pink')
        #self.button_powrot.grid(row=8, column=0, pady=30)

#wyłączenie okna startowego i włączenie okna z bazą trenigów
    def toogleToBase(self):
        self.parent.destroy()
        Base.startBase(username)

#wyłączenie okna konta  i włączenie okna do zmiany hasła
    def toogleToChange(self):
        self.Account.destroy()
        self.changePassword()

#wyłączenie okna ze zmiana hasła i włączenie okna konta
    def toogleToAccount(self):
        self.Password.destroy()
        self.baseAccount()

#połączenie z bazą danych i stworzenie tabeli data - starowego pomiary użytkownika
    def databaseStart(self):
        self.database()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS `data` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, "
            "waga TEXT, talia TEXT, biodra TEXT, udo TEXT, ramie TEXT, lydka TEXT)")

#połączenie z bazą danych i stworzenie tabeli newData - obecna pomiary użytkownika
    def databaseActually(self):
        self.database()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS `newData` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, "
            "waga2 TEXT, talia2 TEXT, biodra2 TEXT, udo2 TEXT, ramie2 TEXT, lydka2 TEXT)")

#połączenie z bazą danych
    def database(self):
        self.conn = sqlite3.connect("members.db")
        self.cursor = self.conn.cursor()

#sprawdzenie, czy podana wartość jest liczbą
    def checkNumber(self, number):
        if number == "":
            return True
        try:
            number = float(number)
        except:
            return False
        if number > 0:
            return True
        else:
            return False


#zapisanie danych startowych podanych przez użytkownika (sprawdzenie + zapisanie w bazie)
    def save(self):
        global priority
        self.databaseStart()
        if self.waga.get() == "" and self.talia.get() == "" and self.biodra.get() == "" and\
                self.udo.get() == "" and self.ramie.get() == "" and self.lydka.get() == "" :
            self.label_result2.config(text="Proszę o uzupełnienie danych startowych!", fg="blue")
            priority =1
        elif not (self.checkNumber(self.waga.get()) and self.checkNumber(self.talia.get()) and self.checkNumber(self.biodra.get()) \
                  and self.checkNumber(self.udo.get()) and self.checkNumber(self.lydka.get()) and self.checkNumber(self.ramie.get()) ):
            self.label_result2.config(text="Nieprawne wartości!", fg="red")
            priority =2
        else:
            self.cursor.execute("SELECT * FROM `data` WHERE `username` = ?", (username,))
            if self.cursor.fetchone() is not None:
                self.sql = ''' UPDATE 'data'
                                SET waga = ? ,
                                    talia = ? ,
                                    biodra = ? ,
                                    udo = ? ,
                                    ramie = ?,
                                    lydka = ? 
                                 WHERE username = ?'''
                self.cursor.execute(self.sql, (str(self.waga.get()), str(self.talia.get()),str(self.biodra.get()),
                                               str(self.udo.get()),str(self.ramie.get()), str(self.lydka.get()),
                                               (str(username))))
                self.conn.commit()
                self.label_result2.config(text="Dane zostały zmienione!", fg="green")
                priority = 0
            else:
                self.cursor.execute("INSERT INTO `data` (username,  waga, talia, biodra,udo, ramie, lydka) VALUES(?, ?,?, ?, ?, ?,?)",
                               (str(username), str(self.waga.get()), str(self.talia.get()), str(self.biodra.get()),
                                 str(self.udo.get()), str(self.ramie.get()), str(self.lydka.get())))
                self.conn.commit()
                self.label_result2.config(text="Dane zostały zapisane!", fg="green")
                priority = 0
            self.cursor.close()
            self.conn.close()

#pobranie z bazy i wpisanie danych użytkownika
    def setEntry(self):
        self.databaseStart()
        self.cursor.execute("SELECT * FROM `data` WHERE `username` = ?" ,(username,))
        self.result = self.cursor.fetchone()
        if self.result is not None:
            self.waga.set(self.result[2])
            self.talia.set(self.result[3])
            self.biodra.set(self.result[4])
            self.udo.set(self.result[5])
            self.ramie.set(self.result[6])
            self.lydka.set(self.result[7])
        else:
            self.label_result2.config(text="Podaj swoje wymiary", fg="blue")
        self.cursor.close()
        self.conn.close()

# zapisanie obecnych podanych przez użytkownika (sprawdzenie + zapisanie w bazie)
    def saveActually(self):
        global priority
        self.databaseActually()
        if self.waga2.get() == "" and self.talia2.get() == "" and self.biodra2.get() == "" and \
                self.udo2.get() == "" and self.ramie2.get() == "" and self.lydka2.get() == "":
            self.cursor.close()
            self.conn.close()
        elif not (self.checkNumber(self.waga2.get()) and self.checkNumber(self.talia2.get()) and self.checkNumber(
                self.biodra2.get()) \
                  and self.checkNumber(self.udo2.get()) and self.checkNumber(self.lydka2.get()) and self.checkNumber(
                    self.ramie2.get())):
            self.label_result2.config(text="Nieprawne wartości!", fg="red")
        else:
            self.cursor.execute("SELECT * FROM `newData` WHERE `username` = ?", (username,))
            if self.cursor.fetchone() is not None:
                self.sql = ''' UPDATE 'newData'
                                   SET waga2 = ? ,
                                       talia2 = ? ,
                                       biodra2 = ? ,
                                       udo2 = ? ,
                                       ramie2 = ?,
                                       lydka2 = ? 
                                    WHERE username = ?'''
                self.cursor.execute(self.sql, (str(self.waga2.get()), str(self.talia2.get()), str(self.biodra2.get()),
                                               str(self.udo2.get()), str(self.ramie2.get()), str(self.lydka2.get()),
                                               (str(username))))
                self.conn.commit()
                if priority == 0:
                    self.label_result2.config(text="Dane zostały zmienione!", fg="green")

            else:
                self.cursor.execute(
                    "INSERT INTO `newData` (username,  waga2, talia2, biodra2,udo2, ramie2, lydka2) VALUES(?, ?,?, ?, ?, ?,?)",
                    (str(username), str(self.waga2.get()), str(self.talia2.get()), str(self.biodra2.get()),
                     str(self.udo2.get()), str(self.ramie2.get()), str(self.lydka2.get())))
                self.conn.commit()
                if priority == 0:
                    self.label_result2.config(text="Dane zostały zapisane!", fg="green")
            self.cursor.close()
            self.conn.close()
            priority =0

# pobranie z bazy obecnych pomiarów użytkownika i wpisanie ich do pól
    def setEntryActually(self):
        self.databaseActually()
        self.cursor.execute("SELECT * FROM `newData` WHERE `username` = ?", (username,))
        self.result = self.cursor.fetchone()
        if self.result is not None:
            self.waga2.set(self.result[2])
            self.talia2.set(self.result[3])
            self.biodra2.set(self.result[4])
            self.udo2.set(self.result[5])
            self.ramie2.set(self.result[6])
            self.lydka2.set(self.result[7])
        else:
            self.label_result2.config(text="Podaj swoje wymiary", fg="blue")
        self.cursor.close()
        self.conn.close()

#sprawdzenie aktualnego hasła użytkownika
    def previousPassword(self):
        self.database()
        self.cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (username,))
        self.result = self.cursor.fetchone()
        if self.result is not None:
            return self.result[2]
        else:
            self.label_result2.config(text="Podaj swoje wymiary", fg="blue")
            return None

#sprawdzenie poprawności podanego hasła
    def checkPasswd(self, password):
        low = 0
        big = 0
        sign = False
        number = 0
        counter = 0
        listOfSigns = ["!", "@", "#", "$", "%", "&", "_"]
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

#ustawienie nowego hasła dla użytkownika i zapisanie go w bazie
    def newPassword(self):
        self.database()
        if self.password0.get() == "" or self.password.get() == "" or self.password2.get() == "":
            self.label_result2.config(text="Proszę o uzupełnienie danych!", fg="blue")
        elif self.previousPassword() is None or self.previousPassword() != self.password0.get():
            self.label_result2.config(text="Niepoprawne aktualne hasło!", fg="red")
        elif not self.checkPasswd(self.password.get()):
            self.label_result2.config(text="Niepoprawne hasło! - min 7 znaków,\nw tym duża i mała litera, liczba, znak specjalny", fg="red")
        elif self.password.get() != self.password2.get():
            self.label_result2.config(text="Hasła różnią się!", fg="red")
        else:
            self.cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (username,))
            if self.cursor.fetchone() is not None:
                self.sql = ''' UPDATE 'member'
                                SET password = ?  
                                 WHERE username = ?'''
                self.cursor.execute(self.sql, (self.password.get(),username))
                self.conn.commit()
                self.label_result2.config(text="Hasło zostało zmienione!", fg="green")

            else:
                self.label_result2.config(text="Coś poszło nie tak...", fg="green")
        self.cursor.close()
        self.conn.close()

#uruchomienie okna konta
def startAccount(user):
    global username
    username = user
    root = tk.Tk()
    app = Account(master=root)
    app.mainloop()
    pass