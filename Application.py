from tkinter import *
from math import ceil
import string
import random


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttnClicks = 0
        self.createWidgets()

    def createWidgets(self):

        self.bigLogo = PhotoImage( file = "img/duzeLogo.png" )
        self.logoLbl = Label(self)
        self.logoLbl["image"] = self.bigLogo
        self.logoLbl["padx"] = 10
        self.logoLbl["pady"] = 10
        self.logoLbl.grid( row = 0, column = 0, columnspan = 5, sticky = W+E+N+S )

        self.textLbl = Label(self)
        self.textLbl["text"] = "Wprowadz nazwę strony, do której chcesz stworzyć hasło"
        self.textLbl["pady"] = 10
        self.textLbl["font"] = ('Arial', 10, 'bold')
        self.textLbl.grid( row = 1, column = 0, columnspan = 5, sticky = W+E+N+S )

        self.dlugoscHasla = StringVar()
        self.dlugoscHasla.set(None)

        dostepneDlugosci = ["krótkie", "średnie", "długie"]
        column = 1
        for dlugosc in dostepneDlugosci:
            Radiobutton(self,
                        text = dlugosc,
                        variable = self.dlugoscHasla,
                        value = column * 5
                        ).grid(row = 2, column = column, sticky = N+E+S+W, pady = 10 )
            column += 1
        self.dlugoscHasla.set(len(dostepneDlugosci)*5)

        self.pwEnt = Entry(self)
        self.pwEnt["borderwidth"] = 10
        self.pwEnt["relief"] = FLAT
        self.pwEnt.grid( row = 3, column = 1, columnspan = 3, sticky = W+E+N+S )

        self.hashBttn = Button(self)
        self.hashBttn["text"] = "szyfruj"
        self.hashBttn["pady"] = 10
        self.hashBttn["padx"] = 30
        self.hashBttn["bg"] = "#0066FF"
        self.hashBttn["font"] = ('Arial', 10, 'bold')
        self.hashBttn.grid( row = 4, column = 2, columnspan = 1, sticky = W+E+N+S, padx = 10, pady = 10 )
        self.hashBttn["command"] = self.encryptPassword

        self.hashPwdLbl = Label(self)
        self.hashPwdLbl["text"] = "Oto twoje zaszyfrowane hasło"
        self.hashPwdLbl["font"] = ('Arial', 10, 'bold')
        self.hashPwdLbl.grid(row = 5, column = 1, columnspan = 3, sticky = W+E+N+S )

        self.hashPwdTxt = Text(self, width = 35, height = 2, wrap = WORD)
        self.hashPwdTxt.insert(0.0, "Tu pojawi się zaszyfrowane hasło")
        self.hashPwdTxt.tag_configure("center", justify='center')
        self.hashPwdTxt.tag_add("center", 1.0, "end")
        self.hashPwdTxt.grid( row = 6, column = 1, columnspan = 3, sticky = W+E+N+S, pady = 10)

    def encryptPassword(self):
        password = (str(self.pwEnt.get())).lower()
        message = ""

        if len(password) <= 0:
            message = "Nie podales strony intenetowej!"
        else:
            random.seed(password)
            wybranaDlugoscHasla = int(self.dlugoscHasla.get())
            letters = ''.join(random.choice(string.ascii_letters) for i in range(wybranaDlugoscHasla))
            digits = ''.join(random.choice(string.digits) for i in range(wybranaDlugoscHasla))

            for i in range(ceil(wybranaDlugoscHasla/2)):
                message += random.choice(letters)
                message += random.choice(digits)

            message = ''.join(random.sample(message,len(message)))
            message = message[:len(message)-1]

        self.hashPwdTxt.delete(0.0, END)
        self.hashPwdTxt.insert(0.0, message)
        self.hashPwdTxt.tag_add("center", 1.0, "end")
