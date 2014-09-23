#! /usr/bin/env python

import os

from_string = raw_input("Seed string: ")

letters = {}

out_string = ''

for each in from_string:
	if letters.has_key(each):
		letters[each] = letters[each] + 1
	else:
		letters[each] = 1

print letters

for each in from_string:
	if letters.has_key(each):
		upper_count = 0
		lower_count = 0
		if each >= 'A' and each <= 'Z':
			upper_count = letters[each]
			try:
				lower_count=letters[chr(ord(each) + 32)]
				del letters[chr(ord(each) + 32)]
			except:
				pass
		elif each >= 'a' and each <= 'z':
			lower_count = letters[each]
			try:
				upper_count = letters[chr(ord(each) - 32)]
				del letters[chr(ord(each) - 32)]
			except:
				pass
		else:
			continue
		del letters[each]
		total = upper_count + lower_count
		if total > 1:
			out_string = out_string + str(total)
		if upper_count and each > 'Z':
			out_string = out_string + chr(ord(each) - 32)
		else:
			out_string = out_string + each
	else:
		continue
	
print out_string
	
