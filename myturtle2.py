#! /usr/bin/python3

from turtle import *
shape('turtle')
speed(0)

def triangle(num,sidelength):
    for i in range(num):
        for i in range(3):
            forward(sidelength)
            left(120)
        left(5)
        
def square(num,sidelength):
    for i in range(num):
        for i in range(4):
            forward(sidelength)
            left(90)
        left(5)

def star(num,sidelength):
    for i in range(num):
        for i in range(5):
            forward(sidelength)
            right(144)
        right(5)

        
