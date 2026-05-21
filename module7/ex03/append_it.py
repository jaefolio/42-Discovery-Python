#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	print("none")
	sys.exit()
for word in sys.argv[1:]:
	if word.endswith("ism"):
		continue
	else:
		print(word + "ism")
	
