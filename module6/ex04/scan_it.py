#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
	print("none")
	sys.exit()
word = sys.argv[1]
string = sys.argv[2]
if string.count(word) == 0:
	print("none")
else:
	print(string.count(word))

