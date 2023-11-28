#!/usr/bin/python3
def remove_char_at(str, n):
	copy = ""
	for i, c in enumerate(str):
		if i != n:
			copy += c
	return copy
