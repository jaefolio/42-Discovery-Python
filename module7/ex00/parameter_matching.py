#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
	sys.exit()
user_input = input("What was the perimeter? ")
if user_input != sys.argv[1]:
	print("Nope, sorry...")
else:
	print("Good job!")
