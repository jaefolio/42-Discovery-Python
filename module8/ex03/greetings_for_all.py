#!/usr/bin/env python3

import sys

#give text default value to so if no argument is passed it uses ""
#isinstance allows you to call an integer directly as .isdigit() expect a string and will crash
def greetings(text=""):
	if isinstance(text, int):
		print("It was not a name.")
	elif not text: 
		print("Hello, noble stranger.")
	else:
		print(f"Hello, {text}")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
