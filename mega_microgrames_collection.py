#! /usr/bin/python2

# Linux User & Developer presents: Mega Microgrames Collection

from Tkinter import *

import rockpaperscissors
import hangman
import pokerdice

root = Tk()
root.title ("Linux User & Developer's Mega Microgrames Collection")

mainframe = Frame(root, height = 200, width = 500)
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

intro = Label(mainframe, text = """Welcome to Linux User & Developers Mega Microgrames Collection.
Please select one of the following games to play:
""")
intro.pack(side = TOP)

rps_button = Button(mainframe, tet = "Rock, Paper, Scissors", command = rockpaperscissors.gui)
rps_button.pack()

rps_button = Button(mainframe, text = "Hangman", command = hangman.start)
hm_button.pack()

pd_button = Button(mainframe, text = "Poker Dice", command = pookerdice.start)
pd_button.pack()

exit_button = Button(mainframe, text = "quit", command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()
