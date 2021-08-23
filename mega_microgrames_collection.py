#! /usr/bin/python2

# Linux User & Developer presents: Mega Microgrames Collection

from Tkinter import *

import rock_paper_scissors2
import hangman
import poker_dice

root = Tk()
root.title ("Linux User & Developer's Mega Microgrames Collection")

mainframe = Frame(root, height = 200, width = 500)
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

intro = Label(mainframe, text = """Welcome to Linux User & Developers Mega Microgrames Collection. Please select one of the following games to play:
""")
intro.pack(side = TOP)

rps_button.pack()

hm_button = Button(mainframe, tet = "Rock, Paper, Scissors", command = rockpaperscissors.gui)
rps_button.pack()

