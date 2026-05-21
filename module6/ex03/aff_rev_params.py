#!/usr/bin/env python3

import sys
length = len(sys.argv)
if len(sys.argv) < 3:
	print("none")
	sys.exit()
i = length - 1
while i > 0:
	print(sys.argv[i])
	i -= 1	
