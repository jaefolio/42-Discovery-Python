#!/usr/bin/env python3

table = 0
number = 0
while table <= 10:
	print(f"Table of {table}: ", end=" ")
	i = 0	
	while i <= 10:
		res = number * i
		print(f"{res}", end=" ")
		i += 1
	print("")
	number += 1
	table += 1
 
