import tkinter as tk
from tkinter import *
import tkinter.messagebox
import Base
import time
import Authentication



FONT = "Calibiri"
FONTSIZE = "12"
username=""


class Training(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.title("Workouts by Karo")
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
        self.addTimer()
        self.startFrame()

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

# dodanie paska menu do okien ćwiczeń
    def addBaseToWorkout(self):
            self.menubar = tk.Menu(self.window1, background='light pink')
            self.window1["menu"] = self.menubar
            fileMenu = tk.Menu(self.menubar)
            for label, command, shortcut_text, shortcut in (
                    (None, None, None, None),
                    ("Wyczyść luki", self.clearFields, "Ctrl+X", "<Control-x>")):
                if label is None:
                    fileMenu.add_separator()
                else:
                    fileMenu.add_command(label=label, underline=0, command=command, accelerator=shortcut_text)
                    self.parent.bind(shortcut, command)
            self.menubar.add_cascade(label="Edycja", menu=fileMenu, underline=0)

#uruchomienie okna startowego
    def startFrame(self):
        pass

#wyczyszczenie pól -entry
    def clearFields(self, event=None):
         event = event
         [self.window1.children[x].delete(0, 'end') for x in self.window1.children if 'entry' in x]
         pass

#yłączenie okna startowego i włączenie uwierzytelniania(wylogowanie)
    def toogleToLogin(self):
        self.parent.destroy()
        Authentication.start()

#dodanie paska minutnik
    def addTimer(self):
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                (None, None, None, None),
                ("Start", self.timeCounter, "Ctrl+X", "<Control-x>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                                     command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Minutnik", menu=fileMenu, underline=0)
        pass


#dodanie funkcjonalności - minutnik - okno
    def timeCounter(self):
        self.timer = tk.Toplevel(self.parent)
        self.timer.title("Minutnik")
        self.timer.config(bg='light pink')
        self.timer.resizable(0, 0)
        self.width = 400
        self.height = 200


        self.hour = StringVar()
        self.minute = StringVar()
        self.second = StringVar()

        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

        self.entry_hour = tk.Entry(self.timer, textvariable=self.hour, width=3, font=(FONT, 17))
        self.entry_hour.place(x=20, y=30)
        self.entry_minute = tk.Entry(self.timer, textvariable=self.minute, width=3, font=(FONT, 17))
        self.entry_minute.place(x=80, y=30)
        self.entry_second = tk.Entry(self.timer, textvariable=self.second, width=3, font=(FONT, 17))
        self.entry_second.place(x=140, y=30)
        self.button_start = tk.Button(self.timer, text='Start', background="black", fg="light pink", width=15,
                                      command=self.setTimer, font=(FONT, 13))
        self.button_start.place(x=30, y=100)
        self.label_result = Label(self.timer, text="", font=(FONT, 13), background='light pink')

#metoda, która inicjujce działanie minutnika
    def setTimer(self):
        self.label_result.config(text="")
        try:
            if (int(self.hour.get()) > -1 or  int(self.hour.get()) == "00") \
                    and (int(self.minute.get()) > -1 or int(self.minute.get()) =="00")\
                and (int(self.second.get()) > -1 or  int(self.second.get()) == "00"):
                temp = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.second.get())
                while temp > -1:
                    mins, secs = divmod(temp, 60)
                    hours = 0
                    if mins > 60:
                        hours, mins = divmod(mins, 60)

                    self.hour.set("{0:2d}".format(hours))
                    self.minute.set("{0:2d}".format(mins))
                    self.second.set("{0:2d}".format(secs))

                    self.parent.update()
                    time.sleep(1)

                    if temp == 0:
                        self.label_result.place(x=60, y=150)
                        self.label_result.config(text="Czas minął!", fg="blue")

                    temp -= 1
            else:
                self.label_result.place(x=25, y=150)
                self.label_result.config(text="Nieprawne wartości!", fg="red")
        except:
            self.label_result.place(x=25, y=150)
            self.label_result.config(text="Nieprawne wartości!", fg="red")

#wyjście z aplikacji
    def exit(self):
        result = tk.messagebox.askquestion('System', 'Jesteś pewny/a, że chcesz wyjść?', icon="warning")
        if result == 'yes':
            self.parent.destroy()
            exit()

#wyłączenie okna startowego i uruchomienie okna z bazą treningów
    def toogleToBase(self):
        self.parent.destroy()
        Base.startBase(username)


#poniżej znajdują się ramki dla wszystkich ćwiczeń użytych w treningach zawierające opisy, zdjęcia,
    # serie do odznaczenia oraz informacje o ilości powtórzeń i serii
    def przysiad(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Przysiady")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("7/20kg")
        self.seria2.set("7/20kg")
        self.seria3.set("7/20kg")
        self.seria4.set("7/20kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  5-7     Przerwa: 2 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/Przysiad.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4,pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Chwytamy sztangę szeroko i wchodzimy pod nią opierając sztangę na kapturach.\n"
                                 "Ściągamy łopatki, klatka piersiowa wypchnięta do przodu,brzuch i pośladki napięte,\n"
                                 "łokcie trzymamy wzdłuż tułowia. Podnosimy sztangę i wykonujemy krok w tył. Stopy\n"
                                 "ustawiamy szerzej niż szerokość bioder.Utrzymując prawidłową pozycję wyjściową\n"
                                 "i naturalną krzywiznę kręgosłupa, wykonujemy przysiad. Następnie wydychając\n "
                                 "powietrze wracamy do pozycji wyjściowej.")
        self.label6.grid(row=8, columnspan=4, column=0)


    def wyciskanieHantli(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wyciskanie hantli skos dodatni 30 st")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("7/10kg")
        self.seria2.set("7/10kg")
        self.seria3.set("7/10kg")
        self.seria4.set("7/10kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  5-7     Przerwa: 2 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wyciskanieHantli.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text= "Połóż się na ławce ustawionej pod kątem 30st. Ściągnij łopatki i wypchnij klatkę. \n"
                                  "Unieś hantle w górę. Ramiona na szerokość barków prostopadle do podłoża. \n"
                                  "Utrzymując poprawną pozycję opuść hantle do klatki piersiowej. Wróć do pozycji  \n"
                                  "początkowej - pamiętaj jednak aby nie zderzać ze sobą hantli. Unikaj przeprostu  \n"
                                  "w stawie łokciowym.")
        self.label6.grid(row=8, columnspan=4, column=0)

    def hipThrust(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Hip thrust")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("8/30kg")
        self.seria2.set("8/30kg")
        self.seria3.set("8/30kg")
        self.seria4.set("8/30kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  6-8     Przerwa: 2 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/hipThrust.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Opieramy się tułowiem o ławeczkę pod kątem na wysokości łopatek, palce u stóp \n"
                                 "skierowane na zewnątrz. Podwiń miednicę, napnij mięśnie brzucha i unieś sztangę \n"
                                 "biodrami. W momencie gdy uniesiesz sztangę kąt w kolanie powinien wynosić 90st. \n"
                                 "Kolana powinny rozchodzić się na zewnątrz. W końcowej fazie ruchu maksymalnie \n"
                                 "napnij pośladki i przytrzymaj napięcie przez ok 2-3 sekundy. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def facepull(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Facepull")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12/10kg")
        self.seria2.set("12/10kg")
        self.seria3.set("12/10kg")
        self.seria4.set("12/10kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/facepull.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Linkę wyciągu górnego chwytasz oburącz i odchodzisz na odległość tak aby\n "
                                 "w momencie gdy masz wyprostowane ręce w łokciach ciężar i napięcie wyciągu\n"
                                 "nie znikało. Łopatki ściągnięte ,brzuch napięty, łokcie zrotowane do zewnątrz.\n"
                                 "Przyciągnij linki w kierunku twarzy , łokcie kierując na boki. Pilnuj aby\n"
                                 "barki nie unosiły się. Powoli wróć do pozycji wyjściowej.")
        self.label6.grid(row=8, columnspan=4, column=0)



    def martwyCiag(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Martwy ciąg")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("9/20kg")
        self.seria2.set("9/20kg")
        self.seria3.set("9/20kg")
        self.seria4.set("9/20kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  7-9     Przerwa: 2 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/martwyCiag.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Ustaw stopy na szerokość bioder, chwyć hantle, napnij brzuch, ściągnij łopatki  \n"
                                  "i wyprostuj się. Z tej pozycji zacznij powolne opuszczanie hantli. Ruch ten  \n"
                                  "powinen odbywać się poprzez cofanie bioder - utrzymuj przez cały ruch ściągnięte \n"
                                  "łopatki i napięte mięśnie brzucha aby utrzymać naturalną krzywiznę kręgosłupa. \n "
                                  "Hanle opuszczaj do momentu gdy poczujesz, że nie jesteś już w stanie cofnąć \n "
                                   "bioder.Powróć do pozycji początkowej.")
        self.label6.grid(row=8, columnspan=4, column=0)




    def gluteBridge(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Glute bridge")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/10kg")
        self.seria2.set("10/10kg")
        self.seria3.set("10/10kg")
        self.seria4.set("extra seria")
        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/gluteBridge.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Kładziemy się na macie, sztanga lub hantel spoczywa na biodrach. Napinamy brzuch \n"
                                 "tak aby odcinek lędźwiowy przylegał do podłoża i uginamy nogi w kolanie. Stopy  \n"
                                 "rozstawione na szerokość bioder lub nieznacznie węziej. Wykonaj wdech i unieś  \n"
                                 "pośladki. Kąt w kolanach po uniesieniu bioder powinien wynosić 90stopni. Przytrzymaj\n"
                                 "sekundę pozycję w momencie maksymalnego napięcia i zacznij powolne opuszczanie\n"
                                 "sztangi do pozycji początkowej.")
        self.label6.grid(row=8, columnspan=4, column=0)



    def wyciskanieHantliNad(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wyciskanie hantli nad głowę siedząc")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("9/10kg")
        self.seria2.set("9/10kg")
        self.seria3.set("9/10kg")
        self.seria4.set("9/10kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  7-9     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wyciskanieHantliNad.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Ustaw ławeczkę i usiądź. Plecy powinny być dociśnięte do oparcia z zachowaniem  \n"
                                    "naturalnej krzywizny kręgosłupa. Stopy spoczywają stabilnie na podłożu. Unieś \n"
                                    "hantle na wysokości głowy. Utrzymując prawidłową pozycję wyciśnij hantle nad  \n"
                                    "głowę, unikaj przeprostu w stawie łokciowym oraz nie zderzaj hantli ze sobą.\n"
                                    "Przez cały ruch łokieć i nadgarstek powinny być w jednej lini. Ruch powolny\n"
                                    "kontrolowany.Następnie przejdź do opuszczania hantli dopozycji początkowej. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def odwodzenieNogi(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Odwodzenie nogi na wyciągu")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/10kg")
        self.seria2.set("10/10kg")
        self.seria3.set("10/10kg")
        self.seria4.set("10/10kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/odwodzenieNogi.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Pochyl się lekko w przód, ręce oprzyj o bramę. Nogę ,którą odwodzisz lekko ugnij \n"
                                 "w kolanie. Wydychając powietrze odwiedź nogę maksymalnie w tył i przytrzymaj przez\n"
                                 "sekundę i powoli wróć do pozycji wyjściowej. Pośladek w momencie maksymalnego \n"
                                 "odwodzenia powinien być napięty. Podczas wykonywania ćwiczenia staraj się aby\n"
                                 "nawet na chwile nie stracić napięcia mięśniowego.")
        self.label6.grid(row=8, columnspan=4, column=0)


    def wyciskanieSztangi(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wyciskanie sztangi leżąc")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("7/20kg")
        self.seria2.set("7/20kg")
        self.seria3.set("7/20kg")
        self.seria4.set("7/20kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  5-7     Przerwa: 2 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wyciskanie.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Połóż się na ławce płaskiej tak żeby sztanga była na wysokości oczu. Złap sztangę \n"
                                 "nieco szerzej niż szerokość barków. Ściągamy łopatki w dół i w tył (retrakcja,\n "
                                 "depresja), a następnie unieś sztangę ze stojaków, tak żeby ramiona były prostopadle\n"
                                 "do ziemi. Prowadząc łokcie pod kątem ok. 45st. Wzdłuż tułowia opuszczamy sztangę do\n"
                                 "klatki piersiowej. Następnie wyciskamy sztangę do pozycji wyjściowej. Utrzymuj\n"
                                 "napięty brzuch i stopy w tej samej pozycji. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def wioslowanie(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wiosłowanie końcem sztangi")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("8/10kg")
        self.seria2.set("8/10kg")
        self.seria3.set("8/10kg")
        self.seria4.set("8/10kg")
        self.label1 = Label(self.window1, text="Powtórzenia:  6-8     Przerwa: 2 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wioslowanie.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Pochylamy się (kąt ok.90stopni w biodrach) uginając lekko kolana. Chwytamy drążek \n"
                                 "i unosimy sztangę. Ściągnij łopatki, wypchnij klatkę piersiową, sztangę przyciągaj\n"
                                 "powoli w stronę brzucha maksymalnie ściągając łopatki. Sztanga powinna sunąć blisko\n"
                                 "ciała ,po nogach. Zacznij powolne opuszczanie sztangi- nie rób tego gwałtownie! ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def rdl(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("RDL")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("7/20kg")
        self.seria2.set("7/20kg")
        self.seria3.set("7/20kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  5-7     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/RDL.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Podejdź do sztangi, ustaw stopy na szerokość bioder, chwyć sztange nachwytem,\n"
                                 "napnij brzuch, ściągnij łopatki i podnieś sztange. Z tej pozycji zacznij powolne\n"
                                 "opuszczanie sztangi. Ruch ten powinen odbywac się poprzez cofanie bioder - utrzymuj\n"
                                 "przez cały ruch ściągnięte łopatki i napięte mięsnie brzucha aby utrzymać naturalną\n"
                                 "krzywiznę kręgosłupa. Sztangę opuszczaj do momentu gdy poczujesz, że nie jesteś już\n"
                                 "w stanie cofnąć bioder. Powróć do pozycji początkowej. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def uginanieNog(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Uginanie nóg na maszynie")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/20kg")
        self.seria2.set("10/20kg")
        self.seria3.set("10/20kg")
        self.seria4.set("extra seria")
        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/uginanieNog.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Zacznij od ustawienia maszyny dostosowując ją do swojego wzrostu- wałek powinien  \n"
                                 "znajdować się kilka cm poniżej łydek. Napnij pośladki. Przyciągnij wałek jak  \n"
                                 "najmocniej w stronę ud i przytrzymaj sekundę, następnie zacznij powolnie opuszczać\n"
                                 "ciężar (jednak nie odkładaj ciężaru całkowicie ,utrzymuj stałe napięcie mięśni).")
        self.label6.grid(row=8, columnspan=4, column=0)

    def odwrotneRozpietki(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Odwrotne Rozpiętki")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()


        self.seria1.set("10/10kg")
        self.seria2.set("10/10kg")
        self.seria3.set("10/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/odwrotneRozpietki.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text= "Ustaw ławkę pod kątem 45 stopni. Chwyć hantle i oprzyj się klatką o ławkę i ugnij\n"
                                  "łokcie. Hantle podnoś wolno do lini barków. Unikaj bujania tułowiem, szarpania,\n"
                                  "gwałtownych ruchów. Następnie zacznij powolne opuszczanie hantli do pozycji\n"
                                  "startowej, utrzymuj stałe napięcie mięśni, nie pozwalaj działać\n grawitacji. ")
        self.label6.grid(row=8, columnspan=4, column=0)



    def uginanieHantli(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Uginanie hantli na biceps")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12/10kg")
        self.seria2.set("12/10kg")
        self.seria3.set("12/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/uginanieHantli.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Stopy ustawiamy na szerokość bioder. Hantle trzymamy wzdłuż tułowia. Napinamy \n"
                                    "brzuch ściągamy łopatki. Uginając łokcie przyciągamy hantel w kierunku klatki\n"
                                    "piersiowej. ")
        self.label6.grid(row=8, columnspan=4, column=0)

    def wznosyHantli(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wznosy hantli w bok")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12/5kg")
        self.seria2.set("12/5kg")
        self.seria3.set("12/5kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wzosyHantli.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text= "Stopy ustawiamy na szerokość bioder. Hantle trzymamy wzdłuż tułowia. Napinamy\n"
                                    "brzuch, ściągamy łopatki. Lekko uginamy łokcie i wznosimy hantle do boku, do\n"
                                    "momentu kiedy łokieć będzie na linii z barkami. Łokcie powinny znajdować się\n"
                                    "w jednej linii z nadgarstkiem lub lekko ponad lini nadgarstka. Powoli opuszczaj\n"
                                    "hantle do pozycji "
                                    "startowej. ")
        self.label6.grid(row=8, columnspan=4, column=0)



    def allahy(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Allahy")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12/10kg")
        self.seria2.set("12/10kg")
        self.seria3.set("12/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/allahy.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Uklęknij, chwyć wyciąg obiema rękoma i przyciągnij za głowę do karku. Zawiń\n"
                                    "miednicę, napnij mięśnie brzucha. Powolnym ruchem, wydychając powietrze zbliżaj\n"
                                    "klatkę piersiową w kierunku kolan. W momencie maksymalnego spięcia przytrzymaj\n"
                                    "sekundę i przejdź do powrotu do pozycji początkowej - pamiętaj jednak aby nie\n"
                                    "tracić pozycji i nie rozluźniać mięśni. Biodra podczas wykonywania ćwiczenia \n"
                                    "powinny być nieruchome! Nie ciągnij ciężaru rękoma, one pozostają stale  tej\n"
                                    "samej pozycji służą nam tylko do utrzymania wyciągu. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def przyciaganieWyciagu(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Przyciąganie wyciągu dolnego do brzucha")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12/10kg")
        self.seria2.set("12/10kg")
        self.seria3.set("12/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/przyciaganieWyciagu.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Chwyć drążek neutralnym chwytem. Odchyl się nieznacznie do tyłu przez wypchnięcie \n"
                                 "klatki piersiowej, ściągnij łopatki. Przyciągnij drążek do klatki prowadząc wzdłuż\n"
                                 "tułowia. Następnie powolnym, kontrolowanym ruchem zacznij prostować ramiona\n"
                                 "opuszczając ciężar. Pamiętaj jednak aby nie odkładać ciężaru, utrzymuj\n"
                                    "stałe napięcie. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def wznosyNaBok(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wznosy na bok na wyciągu")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/10kg")
        self.seria2.set("10/10kg")
        self.seria3.set("10/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wznosyNaBok.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Stań stabilnie , napnij brzuch, ściągnij łopatki. Unieś ramię trzymając uchwyt \n"
                                    "wyciagu dolnego do lini barków. Następnie powolnym ruchem zacznij opuszczać ramię. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def przyciaganieKolan(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Przyciąganie kolan do klatki w podporze tyłem")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12")
        self.seria2.set("12")
        self.seria3.set("12")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/przyciaganieKolan.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Usiądź na twardym podłożu, stopy przylegają do siebie. Lekko odchyl się w tył \n"
                                    "i podeprzyj rękoma. Łopatki ściągnięte, brzuch stale napięty, unosimy zgięte\n"
                                    "nogi nie tracąc przy tym napięcia mięśni brzucha. Przyciągaj kolana w kierunku\n"
                                    "klatki piersiowej jednocześnie wypuszczając powoli powietrze .Nie powinno się\n"
                                    "odczuwać bólu i dyskomfortu w odcinku lędźwiowym. Nogi opuszczaj do momentu aż\n"
                                    "jesteś w stanie utrzymać napięcie mięśni brzucha bez obciążenia odcinka\n"
                                    "lędźwiowego. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def wyciskanieNog(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wyciskanie nóg na suwnicy")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/20kg")
        self.seria2.set("10/20kg")
        self.seria3.set("10/20kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wyciskanieNog.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Ustawiamy maszynę dostosowując do swojego wzrostu. Usadzamy (szeroki rozstaw\n"
                                 "stóp),stopy lekko zrotowane do zewnątrz , kolana lekko ugięte. Odsuwamy zabezpieczenie \n"
                                 "wypychamy powoli platformę. NIE WYKONUJEMY PRZEPROSTU W STAWIE KOLANOWYM-\n"
                                 " - kolana w końcowej fazie ruchu nadal powinny być lekko ugięte. Opuszczamy\n"
                                 "ciężar nie odkładając go do końca tak aby cały czas napięcie było zachowane")
        self.label6.grid(row=8, columnspan=4, column=0)


    def zabiHipThrust(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Żabi hip thrust")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("15/10kg")
        self.seria2.set("15/10kg")
        self.seria3.set("15/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  12-15     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/zabiHip.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Opieramy się tułowiem o ławeczkę pod kątem na wysokości łopatek, stopy łączymy. \n"
                                    "Podwiń miednicę, napnij mięśnie brzucha i unieś sztangę/hantel biodrami.\n"
                                    "W momencie gdy uniesiesz sztangę kąt w kolanie powinien wynosić 90st. Kolana\n"
                                    "powinny rozchodzić się na zewnątrz. W końcowej fazie ruchu maksymalnie napnij \n"
                                    "pośladki i przytrzymaj napięcie przez ok 2-3 sekundy.")
        self.label6.grid(row=8, columnspan=4, column=0)


    def zakroki(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Zakroki")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/10kg")
        self.seria2.set("10/10kg")
        self.seria3.set("10/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/zakroki.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text= "Stań w pozycji wyprostowanej, ustaw stopy na szerokość bioder, napnij brzuch \n"
                                    "i ściągnij łopatki. Przenosząc ciężar na jedną nogę wykonaj zakrok tak głęboki\n"
                                    "jak jesteś w stanie (nie uderzaj jednak kolanem o podłoże). Przez cały ruch\n"
                                    "utrzymuj stabilną pozycję. Wróć do pozycji startowej. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def zabki(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Żabki")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12")
        self.seria2.set("12")
        self.seria3.set("12")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/zabki.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Połóż się na ławce przodem, tak aby nogi swobodnie pozostawały poza ławką.\n"
                                    "Ugnij nogi w kolanach i maksymalnie napinając pośladki unieś stopy w kierunku \n"
                                    "sufitu.Przytrzymaj przez sekundę w fazie maksymalnego napięcia i rozpocznij\n"
                                    "opuszczanie nóg.")
        self.label6.grid(row=8, columnspan=4, column=0)



    def degreeCrunch(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("90 degree crunch")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("15")
        self.seria2.set("15")
        self.seria3.set("15")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  12-15     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/90degree.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Kładziemy się na macie. Napinamy brzuch tak aby odcinek lędźwiowy przylegał do\n"
                                    " podłoża.Unosimy zgięte nogi w kolanie tak aby kąt w biodrze wynosił 90 stopni. \n"
                                    "Dłonie umieszczamy za głową. Napinając mieście brzucha odrywamy łopatki od \n"
                                    "podłoża i przyciągamy klatkę w kierunku kolan. Następnie zaczynamy powolne\n"
                                    "opuszczanie tułowia do pozycji pozczątkowej.")
        self.label6.grid(row=8, columnspan=4, column=0)

    def wznosyKolan(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wznosy kolan do klatki w zwisie")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10")
        self.seria2.set("10")
        self.seria3.set("10")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wznosyKolan.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Chwytamy drążek, ściągamy łopatki i utrzymujemy je sztywno. Przyciągamy nogi\n"
                                    "w kierunku klatki "
                                    "piersiowej i powoli opuszczamy. ")
        self.label6.grid(row=8, columnspan=4, column=0)

    def prostowaniePrzedramion(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Prostowanie przedramion na wyciągu")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/10kg")
        self.seria2.set("10/10kg")
        self.seria3.set("10/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)

        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/prostowaniePrzedramion.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text= "Złap drążek wyciągu górnego na bramie nachwytem, na szerokość barków i pochyl\n"
                                    "się.Ściągnij łopatki, napnij mięśnie brzucha. Trzymając łokcie „przyklejone” do\n"
                                    "tułowia zacznij prostować przedramiona do pełnego wyprostu. Wróć do pozycji\n"
                                    "wyjściowej kontrolując ruch.")
        self.label6.grid(row=8, columnspan=4, column=0)




    def sciaganieDoKlatkiNach(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Ściąganie do klatki nachwytem")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("9/15kg")
        self.seria2.set("9/15kg")
        self.seria3.set("9/15kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  7-9     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/sciaganieDoKlatkiNach.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Drążek chwyć trochę szerzej niż linia barków nachwytem. Odchyl się nieznacznie do \n"
                                "tyłu przez wypchnięcie klatki piersiowej. Przyciągnij drążek do klatki opuszczając.\n"
                                 "łokcie wzdłuż tułowia. Następnie powolnym, kontrolowanym ruchem zacznij \n"
                                 "opuszczając ciężar. Pamiętaj jednak aby nie odkładać ciężaru gdyż może to \n"
                                 "spowodować utratę pozycji w trakcie wykonywania serii.")
        self.label6.grid(row=8, columnspan=4, column=0)


    def bstanceDeadlift(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("B-stance deadlift")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("9/10kg")
        self.seria2.set("9/10kg")
        self.seria3.set("9/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  7-9     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/bstance.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Ustaw stopy na szerokość bioder, jedną nogę cofnij tak aby zapewnić sobie\n"
                                 "równowagę- ciężar ciała jednak spoczywa na nodze wyprostowanej. Chwyć hantla,\n"
                                 "napnij brzuch, ściągnij łopatki i wyprostuj się. Z tej pozycji zacznij powolne\n"
                                 "opuszczanie hantla. Ruch ten powinen odbywać się poprzez cofanie bioder - utrzymuj\n"
                                 "przez ruch ściągnięte łopatki i napięte mięsnie brzucha aby utrzymać naturalną\n"
                                 "krzywiznę kręgosłupa. Tułów opuszczaj do momentu gdy poczujesz, że nie jesteś\n"
                                 "już w stanie cofnąć bioder. Powróć do pozycji początkowej.")
        self.label6.grid(row=8, columnspan=4, column=0)


    def pullThrough(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Pull through")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12/10kg")
        self.seria2.set("12/10kg")
        self.seria3.set("12/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/pullThrough.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Klękamy w takiej odległości od wyciągu aby możliwy był pełen ruch bez odstawienia \n"
                                    "ciężaru. Chwytamy liny i ustawiamy je na lini bioder opierając przedramiona\n"
                                    "o biodra. Ruch odbywa się poprzez wyprostowanie bioder : PAMIĘTAJ! Aby nie\n"
                                    "ciągnąć ciężaru rękoma, możliwie jak największy opór ma spoczywać na biodrach!\n"
                                    "Przedramiona nieruchomo podczas ruchu. ")
        self.label6.grid(row=8, columnspan=4, column=0)



    def lawkaRzymska(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Ławka rzymska")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10")
        self.seria2.set("10")
        self.seria3.set("10")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/ławkaRzymska.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Ustaw ławkę dostosowując jej wysokość do swojego wzrostu - tak abyś była\n"
                                    "w stanie w pełni zgiąć się do kąta ostrego w biodrze. „zawiń” tułów , napnij\n"
                                    "maksymalnie pośladki i zacznij powolne opuszczanie tułowia aż do rozciągnięcia \n"
                                    "mięśni pośladkowych, następnie zacznij prostować tułów używając jedynie siły \n"
                                    "swoich mięśni pośladkowych, nie prostuj tułowia! Unoś tułów jedynie do momentu\n"
                                    "maksymalnego spięcia pośladków. Nie wyginaj się w odcinku lędźwiowym. ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def odwodzenieNogiBok(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Odwodzenie nogi w bok w leżeniu z gumą")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("15")
        self.seria2.set("15")
        self.seria3.set("15")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  12-15     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/odwodzenieNogiBok.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Połóż się na ławce lub macie na ziemi. Gumę oporową umieść nad kolanami. Napnij\n"
                                    "brzuch, lekko ugnij kolana i unieś nogę w górę. Utrzymuj stabilnie pozycję.\n"
                                    "Nie podnoś nogi zbyt wysoko ! Jedynie do momentu kiedy poczujesz maksymalne\n"
                                    "napięcie pośladka.")
        self.label6.grid(row=8, columnspan=4, column=0)


    def sciaganieDoKlatki(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Ściąganie do klatki chwyt neutralny")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/15kg")
        self.seria2.set("10/15kg")
        self.seria3.set("10/15kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 2 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/sciaganieDoKlatki.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Chwyć drążek neutralnym chwytem. Odchyl się nieznacznie do tyłu przez\n"
                                    "wypchnięcie klatki piersiowej. Przyciągnij drążek do klatki opuszczając łokcie\n"
                                    "wzdłuż tułowia.Następnie powolnym, kontrolowanym ruchem zacznij prostować\n"
                                    "ramiona opuszczając ciężar. Pamiętaj jednak aby nie odkładać ciężaru gdyż może\n"
                                    "to spowodować utratę pozycji w trakcie wykonywania serii.")
        self.label6.grid(row=8, columnspan=4, column=0)


    def odwodzenieNog(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Odwodzenie nóg na maszynie")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12/20kg")
        self.seria2.set("12/20kg")
        self.seria3.set("12/20kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  12-15     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/odwodzenieNog.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Ustaw maszynę i usiądź opierając stopy o przeznaczone do tego uchwyty. Pochyl \n"
                                    "się w przód (możesz oprzeć się rękami o maszynę) i napnij brzuch. Odwiedź nogi\n"
                                    "maksymalnie na ile pozwala ci na to maszyna i twoja mobilność, w końcowej fazie\n"
                                    "ruchu przytrzymaj napięcie przez 1 sek. I zacznij powoli opuszczać ciężar - nie \n"
                                    "odkładaj go, utrzymuj stałe napięcie.")
        self.label6.grid(row=8, columnspan=4, column=0)

    def wiosloJednoracz(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Wiosło jednorącz w opadzie tłowia")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("8/10kg")
        self.seria2.set("8/10kg")
        self.seria3.set("8/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  6-8     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/wiosloHantlem.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Oprzyj rękę i nogę o ławeczkę tak aby zapewnić sobie stabilną pozycję. Plecy\n"
                                    "proste, klatka wypchnięta, łopatki ściągnięte. Przyciągnij hantel w kierunku\n"
                                    "biodra. Łokcie prowadź blisko ciała. Opuszczaj hantel powoli wydychając\n"
                                    "powietrze.")
        self.label6.grid(row=8, columnspan=4, column=0)


    def monsterWalk(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Monster walk")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("12")
        self.seria2.set("12")
        self.seria3.set("12")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  10-12     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/monsterWalk.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Gumę zakładamy nad kolana, wypychamy klatkę piersiową, ściągamy łopatki \n"
                                    "i napinamy brzuch. Schodzimy do półprzysiadu i w tej pozycji odwodząc nogę w bok\n"
                                    "pogłębiamy przysiad. Następnie przeciwną nogę dostawiamy wracając do \npółprzysiadu.")
        self.label6.grid(row=8, columnspan=4, column=0)

    def rozpietki(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Rozpiętki")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("10/10kg")
        self.seria2.set("10/10kg")
        self.seria3.set("10/10kg")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  8-10     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1, onvalue=1, offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2, onvalue=1, offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3, onvalue=1, offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var4, onvalue=1, offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/rozpietki.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Połóż się na ławce płaskiej. Ściągnij łopatki i unieś ramiona na szerokość\n"
                                    "barków prostopadle do tułowia. Rozpocznij opuszczanie ramion do momentu aż\n"
                                    "łokieć znajdował nie w lejnej linii z barkiem, następnie powróć do pozycji\n"
                                    "początkowej - nie zderzaj hantli ze sobą! ")
        self.label6.grid(row=8, columnspan=4, column=0)


    def deabBug(self):
        self.window1 = tk.Toplevel(self.parent)
        self.window1.title("Dead bug")
        self.window1.config(bg='light pink')
        self.width = 550
        self.weight = 570
        self.window1.resizable(0, 0)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.addBaseToWorkout()
        self.seria1 = tk.StringVar()
        self.seria2 = tk.StringVar()
        self.seria3 = tk.StringVar()
        self.seria4 = tk.StringVar()

        self.seria1.set("15")
        self.seria2.set("15")
        self.seria3.set("15")
        self.seria4.set("extra seria")

        self.label1 = Label(self.window1, text="Powtórzenia:  12-15     Przerwa: 1,5 min", font=(FONT, 12),
                            background='black',
                            fg="light pink")
        self.label1.grid(row=0, column=0, columnspan=4)
        self.checkbutton1 = tk.Checkbutton(self.window1, text="Seria 1", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var1 ,onvalue=1,offvalue=0)
        self.checkbutton1.grid(row=1, column=0, pady=10)
        self.entry_seria1 = tk.Entry(self.window1, textvariable=self.seria1, width=8, font=("Calibiri", 12), )
        self.entry_seria1.grid(column=1, row=1, pady=10)
        self.checkbutton2 = tk.Checkbutton(self.window1, text="Seria 2", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var2 ,onvalue=1,offvalue=0)
        self.checkbutton2.grid(row=1, column=2, pady=10)
        self.entry_seria2 = tk.Entry(self.window1, textvariable=self.seria2, width=8, font=("Calibiri", 12))
        self.entry_seria2.grid(column=3, row=1, pady=10)
        self.checkbutton3 = tk.Checkbutton(self.window1, text="Seria 3", background="light pink", fg="black",
                                           font=('Calibiri', 12), variable=self.var3 ,onvalue=1,offvalue=0)
        self.checkbutton3.grid(row=2, column=0, pady=10)
        self.entry_seria3 = tk.Entry(self.window1, textvariable=self.seria3, width=8, font=("Calibiri", 12))
        self.entry_seria3.grid(column=1, row=2, pady=10)
        self.checkbutton4 = tk.Checkbutton(self.window1, text="Seria 4*", background="light pink", fg="black",
                                           font=('Calibiri', 12),variable=self.var4 ,onvalue=1,offvalue=0)
        self.checkbutton4.grid(row=2, column=2, pady=10)
        self.entry_seria4 = tk.Entry(self.window1, textvariable=self.seria4, width=8, font=("Calibiri", 12))
        self.entry_seria4.grid(column=3, row=2, pady=10)
        self.img = tk.PhotoImage(file="Photo/deabBug.png")
        self.label5 = Label(self.window1, image=self.img)
        self.label5.grid(row=3, column=0, rowspan=5, columnspan=4, pady=10)
        self.label6 = Label(self.window1, width=72, height=8, background="light pink", font=('Calibiri', 10),
                            text="Połóż się na plecach na macie unieś nogi - kąt w biodrach i kolanie powinien\n"
                                 "wynosić 90 stopni. Ramiona unosimy prostopadle do podłoża. Napinamy brzuch,\n"
                                 "tak aby odcinek lędźwiowy przylegał do maty. Zaczynamy opuszczanie naprzemienne \n"
                                 "nogi i ręki. Przez cały ruch odcinek lędźwiowy powinien przylegać do podłoża!")
        self.label6.grid(row=8, columnspan=4, column=0)

#poniżej znajduja się klasy dla wszystkich zestawów trenigowych,
# w których znajdują się ramki z rozpisanymi po kolei ćwiczeniami, ilością powtórzeń, serii i czasu przerwy
class FullBody1(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Full body 1.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Full body 1.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Przysiady", font=(FONT, FONTSIZE), width=30,
                                   command=self.przysiad, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  5-7  Przerwy: 2 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="Ściąganie do klatki chwyt neutralny", font=(FONT, FONTSIZE), width=30,
                              command=self.sciaganieDoKlatki, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 2 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="Odwodzenie nogi w tył na wyciągu", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.odwodzenieNogi, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Rozpiętki", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.rozpietki, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Monster walk", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.monsterWalk, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Dead bug", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.deabBug, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  12-15   Przerwy: 1 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie pierwszego treningu
def startFullBody1(user):
    global username
    username = user
    root = tk.Tk()
    app = FullBody1(master=root)
    app.mainloop()
    pass



class FullBody2(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Full body 2.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Full body 2.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Hip thrust", font=(FONT, FONTSIZE), width=30,
                                   command=self.hipThrust, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  6-8 Przerwy: 2 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="Wyciskanie hantli skos dodatni 30 st.", font=(FONT, FONTSIZE), width=30,
                              command=self.wyciskanieHantli, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  5-7  Przerwy: 2 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="Wiosło jednorącz w opadzie tłowia", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.wiosloJednoracz, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  6-8  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Odwodzenie nóg na maszynie", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.odwodzenieNog, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  12-15  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Facepull", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.facepull, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="90 degree crunch", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.degreeCrunch, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia: 12-15  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)



#uruchomienie drugiego treningu
def startFullBody2(user):
    global username
    username = user
    root = tk.Tk()
    app = FullBody2(master=root)
    app.mainloop()
    pass




class FullBody3(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Full body 3.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Full body 3.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Martwy ciąg z hantlami", font=(FONT, FONTSIZE), width=30,
                                   command=self.martwyCiag, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  7-9  Przerwy: 2 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="Ściąganie do klatki nachwytem", font=(FONT, FONTSIZE), width=30,
                              command=self.sciaganieDoKlatkiNach, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  7-9  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="Glute bridge", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.gluteBridge, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Wyciskanie hantli nad głowę siedząc", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.wyciskanieHantliNad, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  7-9  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Wyciskanie nóg na suwnicy", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.wyciskanieNog, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Przyciąganie kolan do klatki", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.przyciaganieKolan, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12   Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie trzeciego treningu
def startFullBody3(user):
    global username
    username = user
    root = tk.Tk()
    app = FullBody3(master=root)
    app.mainloop()
    pass



class LowerBody1(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Lower body 1.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Lower body 1.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Hip thrust", font=(FONT, FONTSIZE), width=30,
                                   command=self.hipThrust, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 4  Powtórzenia: 6-8  Przerwy: 2 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="RDL", font=(FONT, FONTSIZE), width=30,
                              command=self.rdl, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  5-7  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="Odwodzenie nogi w tył na wyciągu", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.odwodzenieNogi, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Wyciskanie nóg na suwnicy", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.wyciskanieNog, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Uginanie nóg na maszynie", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.uginanieNog, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Allahy", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.allahy, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12   Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie czwartego treningu
def startLowerBody1(user):
    global username
    username = user
    root = tk.Tk()
    app = LowerBody1(master=root)
    app.mainloop()
    pass



class LowerBody2(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Lower body 2.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Lower body 2.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Przysiad", font=(FONT, FONTSIZE), width=30,
                                   command=self.przysiad, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 4  Powtórzenia: 5-7  Przerwy: 2 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="Glute bridge", font=(FONT, FONTSIZE), width=30,
                              command=self.gluteBridge, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  8-10  Przerwy: 2 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="B-stance deadlift", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.bstanceDeadlift, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  7-9  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Pull through", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.pullThrough, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Ławka rzymska", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.lawkaRzymska, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Odwodzenie nogi w bok", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.odwodzenieNogiBok, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  12-15  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie piątego treningu
def startLowerBody2(user):
    global username
    username = user
    root = tk.Tk()
    app = LowerBody2(master=root)
    app.mainloop()
    pass



class LowerBody3(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Lower body 3.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Lower body 3.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Przysiady", font=(FONT, FONTSIZE), width=30,
                                   command=self.przysiad, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 4  Powtórzenia: 5-7  Przerwy: 2 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="RDL", font=(FONT, FONTSIZE), width=30,
                              command=self.rdl, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  5-7  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="Żabi hip thrust", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.zabiHipThrust, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  12-15  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Zakroki", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.zakroki, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Uginanie nóg na maszynie", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.uginanieNog, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Żabki", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.zabki, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12   Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie szóstego treningu
def startLowerBody3(user):
    global username
    username = user
    root = tk.Tk()
    app = LowerBody3(master=root)
    app.mainloop()
    pass



class UpperBody1(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Upper body 1.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Upper body 1.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Wiosłowanie końcem sztangi", font=(FONT, FONTSIZE), width=30,
                                   command=self.wioslowanie, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 4  Powtórzenia: 6-8   Przerwy: 2 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="Wyciskanie sztangi leżąc", font=(FONT, FONTSIZE), width=30,
                              command=self.wyciskanieSztangi, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  5-7  Przerwy: 2 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="Wznosy hantli w bok", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.wznosyHantli, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Ściąganie drążka do klatki neutralnie", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.sciaganieDoKlatki, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 2 min min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Odwrotne rozpietki", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.odwrotneRozpietki, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Uginanie hantli na biceps", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.uginanieHantli, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12   Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie siódmego treningu
def startUpperBody1(user):
    global username
    username = user
    root = tk.Tk()
    app = UpperBody1(master=root)
    app.mainloop()
    pass


class UpperBody2(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Upper body 2.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Upper body 2.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Wyciskanie hantli nad głowę siedząc", font=(FONT, FONTSIZE), width=30,
                                   command=self.wyciskanieHantliNad, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 4  Powtórzenia: 7-9  Przerwy: 1,5 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="Ściąganie do klatki nachwytem", font=(FONT, FONTSIZE), width=30,
                              command=self.sciaganieDoKlatkiNach, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  7-9  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="Facepull", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.facepull, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Rozpiętki", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.rozpietki, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Przyciąganie wyciągu dolnego", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.przyciaganieWyciagu, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Wznosy w bok na wyciągu", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.wznosyNaBok, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10   Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie ósmego treningu
def startUpperBody2(user):
    global username
    username = user
    root = tk.Tk()
    app = UpperBody2(master=root)
    app.mainloop()
    pass


class UpperBody3(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)


    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Upper body 3.1")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Upper body 3.1", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Wiosło jednorącz w opadzie tłowia", font=(FONT, FONTSIZE), width=30,
                                   command=self.wiosloJednoracz, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 3  Powtórzenia: 6-8  Przerwy: 1,5 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="Ściąganie do klatki nachwytem", font=(FONT, FONTSIZE), width=30,
                              command=self.sciaganieDoKlatkiNach, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  7-9  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="Facepull", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.facepull, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 4  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Prostowanie przedramian na wyciągu", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.prostowaniePrzedramion, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Odwrotne rozpiętki", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.odwrotneRozpietki, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Wznosy kolan do klatki w zwisie", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.wznosyKolan, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10   Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie dziewiątego treningu
def startUpperBody3(user):
    global username
    username = user
    root = tk.Tk()
    app = UpperBody3(master=root)
    app.mainloop()
    pass


class FlatBelly(Training):
    def __init__(self, master=None):
        Training.__init__(self, master)
        

    def startFrame(self):
        self.robocze = tk.Frame(self.parent, background='light pink')
        self.robocze.pack(side=TOP, pady=10)
        self.parent.title("Flat belly")
        self.StartWindow = self.robocze
        self.label_start = tk.Label(self.StartWindow, text="Flat belly", font=('Calibiri', 20),
                                      background='light pink', fg="white")
        self.label_start.grid(row=0, column = 1, pady=15)
        self.button1 = Button(self.StartWindow, text="Powrót", font=(FONT, FONTSIZE), width=30,
                              command=self.toogleToBase, background='light pink', fg="black")
        self.button1.grid(row=15, column=1)
        self.button1 = Button(self.StartWindow, text="Dead bug", font=(FONT, FONTSIZE), width=30,
                                   command=self.deabBug, background='black', fg="pink")
        self.button1.grid(row=1, column =1)
        self.label1 = Label(self.StartWindow, text="Serie: 3  Powtórzenia: 12-15  Przerwy: 1 min\n", font=(FONT, 10), background='light pink',
                                    fg="black")
        self.label1.grid(row=2,column =1)
        self.button2 = Button(self.StartWindow, text="Przyciąganie kolan do klatki", font=(FONT, FONTSIZE), width=30,
                              command=self.przyciaganieKolan, background='black', fg="pink")
        self.button2.grid(row=3, column=1)
        self.label2 = Label(self.StartWindow, text="Serie: 3  Powtórzenia: 10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label2.grid(row=4, column=1)
        self.button3 = Button(self.StartWindow, text="90 degree crunch", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.degreeCrunch, background='black', fg="pink")
        self.button3.grid(row=5, column=1)
        self.label3 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label3.grid(row=6, column=1)
        self.button4 = Button(self.StartWindow, text="Allahy", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.allahy, background='black', fg="pink")
        self.button4.grid(row=7, column=1)
        self.label4 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label4.grid(row=8, column=1)
        self.button6 = Button(self.StartWindow, text="Przyciąganie kolan do klatki", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.przyciaganieKolan, background='black', fg="pink")
        self.button6.grid(row=10, column=1)
        self.label6 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  10-12  Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label6.grid(row=11, column=1)

        self.button7 = Button(self.StartWindow, text="Wznosy kolan do klatki w zwisie", font=(FONT, FONTSIZE),
                              width=30,
                              command=self.wznosyKolan, background='black', fg="pink")
        self.button7.grid(row=12, column=1)
        self.label7 = Label(self.StartWindow, text="Serie: 3  Powtórzenia:  8-10   Przerwy: 1,5 min\n", font=(FONT, 10),
                            background='light pink',
                            fg="black")
        self.label7.grid(row=13, column=1)

#uruchomienie dziesiątego treningu
def startFlatBelly(user):
    global username
    username = user
    root = tk.Tk()
    app = FlatBelly(master=root)
    app.mainloop()
    pass