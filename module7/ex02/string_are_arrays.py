#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
	sys.exit()

text = sys.argv[1]
if "z" not in text:
	print("none")
else:
	for char in text:
		if char == "z":
			print("z", end="")
