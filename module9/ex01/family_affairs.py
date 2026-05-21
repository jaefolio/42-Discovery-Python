#!/usr/bin/env python3


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

def find_the_redheads(family):
	#redheads = []
	#for p in family:
		#if family[p] == "red":
			#redheads.append(p)
	redheads = list(filter(lambda p: family[p] == "red", family))
	return redheads

print(find_the_redheads(dupont_family))
