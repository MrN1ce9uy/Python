#! /usr/bin/python3

import random

while True:
	print(''' 1. roll the dice		2. exit		''')
	user = int(input("what do you want to do?\n"))
	if user==1:
		number1 = random.randint(1,6)
		number2 = random.randint(1,6)
		print(number1,number2)
	else:
		break
