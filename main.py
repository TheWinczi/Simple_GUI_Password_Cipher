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

""" Other methods

    window = Tk()
    
    window.geometry("420x420")
    window.title("This is title")

    icon = PhotoImage(file = 'imgs/icon.png')
    window.iconphoto(True, icon)
    window.config(background = '#db6e00')

    label = Label(window,
                  text="Pierwszy label",
                  fg = "red",
                  bg = 'black',
                  font=('Arial', 35, 'bold'),
                  relief = RAISED,
                  bd = 10,
                  padx = 20,
                  pady = 20,
                  image = icon,
                  compound = 'right')
    label.pack()
    # label.place(x=0, y=0)
    
    # main loop of window
    window.mainloop()
"""
