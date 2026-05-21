#!/usr/bin/env python3

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
#p[1] is the nested dictionary
def famous_births(scientists):
	year = sorted(scientists.items(), key= lambda p: p[1]["date_of_birth"])
	name_year = []
	for p in year:
		print(f"{p[1]["name"]} is a great scientist born in {p[1]["date_of_birth"]}.")

famous_births(women_scientists)
