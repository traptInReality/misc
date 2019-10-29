#! /usr/bin/env python

# Colt Adkison
# 28 OCT 2019
# Caesar Cipher Cracker

test = 'OCA'
boundaries = { 'lower': [ord('a'),ord('z')], 'upper': [ord('A'),ord('Z')] }

def rotate(source, offset):
    dest = ord(source) + offset
    if source in range(*boundaries['lower']):
        print('lower')
    elif source in range(*boundaries['upper']):
        print('upper')

for each in test:
    rotate(each,1)
