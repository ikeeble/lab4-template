#!/usr/bin/env python3
# Author ID: ikeeble

#Created on: 09/02/2024
#Author: Iain Keeble

def is_digits(sobj):
    for char in sobj:
        if not char.isdigit():
            return False
    return True
    # place code here - loop through each character in sobj 

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
