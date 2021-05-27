import Application
from tkinter import *


def main():
    """ main function on the program """

    # defain main window
    root = Tk()

    root.title("Szyfrator haseł")
    root.geometry("480x480")
    root.resizable( width=False, height=False )

    logo = PhotoImage(file="img/maleLogo.png")
    root.iconphoto(True, logo)

    app = Application.Application(root)

    # main function of the window
    root.mainloop()


# Check is it main
if __name__ == '__main__':
    main()
