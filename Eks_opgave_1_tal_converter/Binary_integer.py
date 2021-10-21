# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:43:21 2021

@author: Daniel
"""

# Function to convert integer to binary
# Create an empty list, then take the entered integer and modulus by 2
# Add the modulus to the list, then use floor division to redefine the entered number
# Perform until i < 0. Reverse the list, print the list

def int_to_bin(i):
    a=[]
    while i > 0:
        n = i % 2
        a.append(n)
        i = i//2
    a.reverse()
    print("The number in binary is: ")
    for i in a:
        print(i,end="")



# To convert from binary to integer, take current total, mulitpy by 2,
# add current digit. Repeat for every digit.

def bin_to_int(b):
    # Make a list of the digits.
    b = [int(x) for x in str(b)]
    # Make a "total"
    t = 0
    # Multiply t by 2 and add digit for each digit in the list
    for num in b: 
        t = 2*t+num
    print(t) 


bin_to_int(1100)