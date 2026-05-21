#!/usr/bin/env python3

import sys

if len(sys.argv) == 1 or len(sys.argv) > 2:
	print("none")
else:
	text = sys.argv[1]
	print(text.lower())
