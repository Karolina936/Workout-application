import tkinter as tk
from tkinter import *
import tkinter.messagebox
import Base
import sqlite3
from datetime import date
import time
import Authentication

FONT = "Calibiri"
FONTSIZE = "12"
user=""
success = False


class Payment(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.title("Płatność")
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


#dodanie paska menu
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

#dodanie paska edit
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

#wyczyszczenie pól entry
    def clearFields(self, event=None):
        event = event
        [self.robocze.children[x].delete(0, 'end') for x in self.robocze.children if 'entry' in x]
        pass

#wyjście z aplikacji
    def exit(self):
        result = tk.messagebox.askquestion('System', 'Jesteś pewny/a, że chcesz wyjść?', icon="warning")
        if result == 'yes':
            self.parent.destroy()
            exit()

#metoda do napisania - sprawdzanie poprawności pól entry
    def check(self):
        pass

#ramka startowa z wyborem metody płatności
    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP)
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="PŁATNOŚĆ", font=('Calibiri', 25),background='light pink', fg= "white")
        self.label_start.grid(row=0, pady =20)
        self.button_blik = Button(self.StartWindow, text="\nBLIK\n", font=(FONT, FONTSIZE), width=30, command=self.toogleToBlik, background='light pink', fg= "white")
        self.button_blik.grid(row=1, rowspan=3, pady=10)
        self.button_karta = Button(self.StartWindow, text="\nKARTA\n", font=(FONT, FONTSIZE), width=30, command=self.toogleToKarta, background='light pink', fg= "white")
        self.button_karta.grid(row=4, rowspan=3, pady=10)
        self.button_powrot = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=10,
                                   command=self.toogleToLogin, background='black', bd=0, fg="light pink")
        self.button_powrot.grid(row=7, pady=20)


#zamknięcie okna startowego i uruchomienie okna z autoryzacją
    def toogleToLogin(self):
        self.parent.destroy()
        Authentication.start()

#zamknięcie okna startowego i uruchomienie okna z blikiem
    def toogleToBlik(self):
        self.parent.destroy()
        startBLIK()

#zamknięcie okna startowego i uruchomienie okna z kartą
    def toogleToKarta(self):
        self.parent.destroy()
        startKarta()

#połączenie z bazą danych i stworzenie tabeli payment
    def database(self):
        self.conn = sqlite3.connect("members.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS `payment` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT)")

#płatność - sprawdzenie poprawności wpisywanych danych i dodanie użytkownika do bazy danych do tabeli payment
    def pay(self):
        global success
        self.database()
        self.check()
        if success == True:
            self.cursor.execute("SELECT * FROM `payment` WHERE `username` = ?", (str(user),))
            if self.cursor.fetchone() is not None:
                self.label_result2.config(text="Konto jest już opłacone", fg="blue")
            else:
                self.cursor.execute("INSERT INTO `payment` (username) VALUES(?)",(str(user),))
                self.conn.commit()
                self.label_result2.config(text="Płatność zakończona!", fg="green")
                self.cursor.close()
                self.conn.close()
            self.parent.destroy()
            Base.startBase(user)
        else:
            self.cursor.close()
            self.conn.close()


#płatność BLIKiem
class BLIK(Payment):
    def __init__(self, master=None):
        Payment.__init__(self, master)
        self.StartWindow.destroy()
        self.payment()

#okna płatności BLIK
    def payment(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=20)

        self.BLIKWindow = self.robocze
        self.parent.title("BLIK")

        self.kod = IntVar()
        self.button_powrot = Button(self.BLIKWindow, text="Płatność", font=(FONT, 17), width=23,
                                   command=self.toogleToPayment,
                                   background='light pink', fg="white")
        self.button_powrot.grid(row=0, columnspan=2, pady=10)
        self.label_zaplata = tk.Label(self.BLIKWindow, text="Do zapłaty 99 zł", font=(FONT, 14),
                                      background='light pink', fg="white")
        self.label_zaplata.grid(row=1, column=0, pady=10, columnspan=2)
        self.label_kod = tk.Label(self.BLIKWindow, text="kod BLIK", font=(FONT, FONTSIZE), background='light pink')
        self.label_kod.grid(row=2, column=0, pady=10)
        self.entry_BLIK = tk.Entry(self.BLIKWindow, textvariable=self.kod, width=10, font=(FONT, FONTSIZE))
        self.entry_BLIK.grid(row=2, column=1, pady=20)
        self.button_check = Button(self.BLIKWindow, text="Zapłać", font=(FONT, FONTSIZE), width=23,
                                   command=self.pay,
                                   background='black', fg="white")
        self.button_check.grid(row=3, columnspan=2, pady=10)
        self.label_result2 = Label(self.BLIKWindow, text="", font=(FONT, FONTSIZE), background='light pink')
        self.label_result2.grid(row=4, columnspan=2, pady=15)


#sprawdzenie poprawności podanego BLIKa
    def check(self):
        global success
        if self.entry_BLIK.get() == "":
            self.label_result2.config(text="Uzupełnij dane!", fg="red")
        if self.entry_BLIK.get().isdigit():
            counter = 0
            for number in self.entry_BLIK.get():
                counter +=1
            if counter == 6:
                success = True
            else:
                self.label_result2.config(text="Niepoprawny kod BLIK!", fg="red")
                success = False
        else:
            self.label_result2.config(text="Niepoprawny kod BLIK!", fg="red")
            success = False

#zamknięcie okna BLIK i uruchomienie okna startowego
    def toogleToPayment(self):
        self.BLIKWindow.destroy()
        self.startFrame()

#metoda płatności - karta
class Karta(Payment):
    def __init__(self, master=None):
        Payment.__init__(self, master)
        self.StartWindow.destroy()
        self.payment()

#okno metody płatności -karta
    def payment(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=20)

        self.KartaWindow = self.robocze
        self.parent.title("Karta")

        self.karta = IntVar()
        self.cvv = IntVar()
        self.data = StringVar()

        self.karta.set("")
        self.cvv.set("")

        self.button_powrot = Button(self.KartaWindow, text="Płatność", font=(FONT, 17), width=23,
                                   command=self.toogleToPayment,
                                   background='light pink', fg="white")
        self.button_powrot.grid(row=0, columnspan=2, pady=10)
        self.label_zaplata = tk.Label(self.KartaWindow, text="Do zapłaty 99 zł", font=(FONT, 14),
                                      background='light pink', fg="white")
        self.label_zaplata.grid(row=1, column=0, pady=10, columnspan=2)
        self.label_karta = tk.Label(self.KartaWindow, text="Numer karty", font=(FONT, FONTSIZE), background='light pink')
        self.label_karta.grid(row=2, column=0, pady=5)
        self.entry_karta = tk.Entry(self.KartaWindow, textvariable=self.karta, width=18, font=(FONT, FONTSIZE))
        self.entry_karta.grid(row=2, column=1, pady=5)
        self.label_cvv = tk.Label(self.KartaWindow, text="CVV/CVC", font=(FONT, FONTSIZE),
                                    background='light pink')
        self.label_cvv.grid(row=3, column=0)
        self.entry_cvv = tk.Entry(self.KartaWindow, textvariable=self.cvv, width=18, font=(FONT, FONTSIZE))
        self.entry_cvv.grid(row=3, column=1, pady=5)
        self.label_data = tk.Label(self.KartaWindow, text="Data ważności", font=(FONT, FONTSIZE),
                                  background='light pink')
        self.label_data.grid(row=4, column=0)
        self.entry_data = tk.Entry(self.KartaWindow, textvariable=self.data, width=18, font=(FONT, FONTSIZE))
        self.entry_data.grid(row=4, column=1, pady=5)
        self.button_check = Button(self.KartaWindow, text="Zapłać", font=(FONT, FONTSIZE), width=23,
                                   command=self.pay,
                                   background='black', fg="white")
        self.button_check.grid(row=5, columnspan=2, pady=20)
        self.label_result2 = Label(self.KartaWindow, text="", font=(FONT, FONTSIZE), background='light pink')
        self.label_result2.grid(row=6, columnspan=2)

#sprawdzenie poprawności podanej karty, numeru CVV/CVC i daty ważności
    def check(self):
        global success
        if self.entry_karta.get() != "" and  self.entry_cvv.get() != "" and  self.entry_data.get() != "":
            if self.entry_karta.get().isdigit() and self.entry_cvv.get().isdigit():
                counter = 0
                for number in self.entry_karta.get():
                    counter += 1
                if counter == 16:
                    counter = 0
                    for nr in self.entry_cvv.get():
                        counter += 1
                    if counter == 3:
                        try:
                            if self.data.get()[2] == "/":
                                month = int(self.data.get()[0]) * 10 + int(self.data.get()[1])
                                year = int(self.data.get()[3]) * 10 + int(self.data.get()[4])
                                if date.today().year % 2000 < year:
                                    success = True
                                elif date.today().year % 2000 == year and date.today().month <= month and month <= 12:
                                    success = True
                                else:
                                    success = False
                                    self.label_result2.config(text="Niepoprawna data!", fg="red")
                            else:
                                success = False
                                self.label_result2.config(text="Niepoprawna data!", fg="red")
                        except:
                            success = False
                            self.label_result2.config(text="Niepoprawna data!", fg="red")
                    else:
                        success = False
                        self.label_result2.config(text="Niepoprawny numer CVV/CVC!", fg="red")
                else:
                    success = False
                    self.label_result2.config(text="Niepoprawny numer karty!", fg="red")
            else:
                success = False
                self.label_result2.config(text="Proszę podawać wyłącznie liczby naturalne!", fg="red")
        else:
            success = False
            self.label_result2.config(text="Wpisz brakujące dane!", fg="blue")


#zamknięcie okna karty i uruchomienie okna startowego
    def toogleToPayment(self):
        self.KartaWindow.destroy()
        self.startFrame()

#uruchomienie płatności kartą
def startKarta():
    root = tk.Tk()
    app = Karta(master=root)
    app.mainloop()
    pass

#uruchomienie płatności BLIKiem
def startBLIK():
    root = tk.Tk()
    app = BLIK(master=root)
    app.mainloop()
    pass

#uruchomienie płatności
def startPayment(usern):
    global user
    user = usern
    root = tk.Tk()
    app = Payment(master=root)
    app.mainloop()
    pass


