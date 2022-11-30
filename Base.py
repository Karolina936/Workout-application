import tkinter as tk
from tkinter import *
import tkinter.messagebox
import Trainings
import Account
import Authentication

username=""


class Base(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.title("Treningi")
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
        self.baseFrame()

#dodanie paska menu
    def addBaseMenu(self):
        self.menubar = tk.Menu(self.parent, background='light pink')
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("Wyloguj się", self.toogleToLogin, "Ctrl+X", "<Control-x>"),
                (None, None, None, None),
                ("Wyjście", self.exit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0, command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Menu", menu=fileMenu, underline=0)

#wyjście z aplikacji
    def exit(self):
        result = tk.messagebox.askquestion('System', 'Jesteś pewny/a, że chcesz wyjść?', icon="warning")
        if result == 'yes':
            self.parent.destroy()
            exit()

#wyłączenie okna startowego i włączenie okna uwierzytelniania
    def toogleToLogin(self):
        self.parent.destroy()
        Authentication.start()

#okno startowe zestawów ćwiczeń
    def baseFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP)
        self.BaseWindow = self.robocze
        self.label_workouts = tk.Label(self.BaseWindow, text="TRENINGI", font=("Calibiri", 25, "bold"),background='light pink', fg="white")
        self.label_workouts.grid(row=0,column=1,pady=15)
        self.label_fb = tk.Label(self.BaseWindow, text="Full body", font=("Calibiri", 15), background='light pink',fg="black")
        self.label_fb.grid(row=1,column=1, pady=15)
        self.label_fb1 = tk.Button(self.BaseWindow, text="Full body 1.1", font=("Calibiri", 12), command=self.fullBody1, background='light pink',fg="black")
        self.label_fb1.grid(row=2, column=0)
        self.label_fb2 = tk.Button(self.BaseWindow, text="Full body 2.1", font=("Calibiri", 12), command=self.fullBody2, background='light pink',fg="black")
        self.label_fb2.grid(row=2, column=1)
        self.label_fb2 = tk.Button(self.BaseWindow, text="Full body 3.1", font=("Calibiri", 12), command=self.fullBody3, background='light pink',fg="black")
        self.label_fb2.grid(row=2, column=2)
        self.label_as = tk.Label(self.BaseWindow, text="Lower body", font=("Calibiri", 15), background='light pink',
                                 fg="black")
        self.label_as.grid(row=4, column=1, pady=15)
        self.label_as1 = tk.Button(self.BaseWindow, text="Lower body 1.1", font=("Calibiri", 12), command=self.lowerBody1,
                                   background='light pink', fg="black")
        self.label_as1.grid(row=5, column=0)
        self.label_as2 = tk.Button(self.BaseWindow, text="Lower body 2.1", font=("Calibiri", 12), command=self.lowerBody2,
                                   background='light pink', fg="black")
        self.label_as2.grid(row=5, column=1)
        self.label_as2 = tk.Button(self.BaseWindow, text="Lower body 3.1", font=("Calibiri", 12), command=self.lowerBody3,
                                   background='light pink', fg="black")
        self.label_as2.grid(row=5, column=2)
        self.label_ub = tk.Label(self.BaseWindow, text="Upper body", font=("Calibiri", 15), background='light pink',
                                fg="black")
        self.label_ub.grid(row=6, column=1, pady=15)
        self.label_ub1 = tk.Button(self.BaseWindow, text="Upper body 1.1", font=("Calibiri", 12), command=self.upperBody1,
                                  background='light pink', fg="black")
        self.label_ub1.grid(row=7, column=0)
        self.label_ub2 = tk.Button(self.BaseWindow, text="Upper body 2.1", font=("Calibiri", 12), command=self.upperBody2,
                                  background='light pink', fg="black")
        self.label_ub2.grid(row=7, column=1)
        self.label_ub2 = tk.Button(self.BaseWindow, text="Upper body 3.1", font=("Calibiri", 12), command=self.upperBody3,
                                  background='light pink', fg="black")
        self.label_ub2.grid(row=7, column=2)
        self.label_et = tk.Label(self.BaseWindow, text="Extra training", font=("Calibiri", 15), background='light pink',
                                 fg="black")
        self.label_et.grid(row=8, column=1, pady=15)
        self.label_fb = tk.Button(self.BaseWindow, text="Flat belly", font=("Calibiri", 12),
                                   command=self.flatBelly,
                                   background='light pink', fg="black")
        self.label_fb.grid(row=9, column=1)
        self.label_ac = tk.Button(self.BaseWindow, text="Konto", font=("Calibiri", 15),
                                   command=self.toogleToAccount,
                                   background='black', fg="light pink", width=15)
        self.label_ac.grid(row=11, column=1, pady=30)


#wyłączenie okna startowego i włączenie okna konta użytkownika
    def toogleToAccount(self):
        self.parent.destroy()
        Account.startAccount(username)

#wyłączenie okna startowego i włączenie pierwszego zestawu ćwiczeń
    def fullBody1(self):
        self.parent.destroy()
        Trainings.startFullBody1(username)

# wyłączenie okna startowego i włączenie drugiego zestawu ćwiczeń
    def fullBody2(self):
        self.parent.destroy()
        Trainings.startFullBody2(username)

# wyłączenie okna startowego i włączenie trzeciego zestawu ćwiczeń
    def fullBody3(self):
        self.parent.destroy()
        Trainings.startFullBody3(username)

# wyłączenie okna startowego i włączenie czwartego zestawu ćwiczeń
    def lowerBody1(self):
        self.parent.destroy()
        Trainings.startLowerBody1(username)

# wyłączenie okna startowego i włączenie piątego zestawu ćwiczeń
    def lowerBody2(self):
        self.parent.destroy()
        Trainings.startLowerBody2(username)

# wyłączenie okna startowego i włączenie szóstego zestawu ćwiczeń
    def lowerBody3(self):
        self.parent.destroy()
        Trainings.startLowerBody3(username)

# wyłączenie okna startowego i włączenie siódmego zestawu ćwiczeń
    def upperBody1(self):
        self.parent.destroy()
        Trainings.startUpperBody1(username)

# wyłączenie okna startowego i włączenie ósmego zestawu ćwiczeń
    def upperBody2(self):
        self.parent.destroy()
        Trainings.startUpperBody2(username)

# wyłączenie okna startowego i włączenie dziewiątego zestawu ćwiczeń
    def upperBody3(self):
        self.parent.destroy()
        Trainings.startUpperBody3(username)

# wyłączenie okna startowego i włączenie dziesiątego zestawu ćwiczeń
    def flatBelly(self):
        self.parent.destroy()
        Trainings.startFlatBelly(username)

#uruchomienie bazy z treningami
def startBase(user):
    global username
    username = user
    root = tk.Tk()
    app = Base(master=root)
    app.mainloop()
    pass
