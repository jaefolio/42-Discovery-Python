#!/usr/bin/env python3

import sys

def shrink(text):
	return(text[:8])

def enlarge(text):
	length = len(text)
	while length < 8:
		text = text + "Z"
		length += 1
	return(text)

for arg in sys.argv[1:]:
	if len(arg) > 8:
		print(shrink(arg))
	elif len(arg) < 8:
		print(enlarge(arg))
	else:
		print(arg)
		
		




