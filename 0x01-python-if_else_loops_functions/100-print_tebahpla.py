#!/usr/bin/python3
for i, j in zip(range(122, 96, -1), range(89, 64, -1)):
	print(f"{chr(i)}{chr(j)}", end="")
