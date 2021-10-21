# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:20:32 2021

@author: andre
"""
def int_to_bin(y):
    return

def int_to_rom(y):
    return

def bin_to_int(y):
    return

def rom_to_int(y):
    return

# Menu function is defined
def menu():
    try:
        # Ask user for input    
        from_sys = input('''Please choose your number system
                                 #1. Decimal
                                 #2. Binary
                                 #3. Roman
                                 --->:
                                     ''')
        user_number = input('''Please enter your number 
                                --->:
                                    ''')

        to_sys = input('''Please choose the numerical system you want to convert to
        #1. Decimal
        #2. Binary
        #3. Roman
        --->: 
            ''')
            
        # Convert number from system to system based on user input  
        if from_sys == '1' and to_sys == '2': # int to bin
            print(int_to_bin(int(user_number)))
        elif from_sys == '1' and to_sys == '3': # int to rom
            print(int_to_rom(int(user_number)))
        elif from_sys == '2' and to_sys == '3': # bin to rom
            bin_int = bin_to_int(user_number)
            print(int_to_rom(bin_int)) # rom to bin
        elif from_sys == '3' and to_sys == '2':
            rom_int = rom_to_int(user_number)
            print(int_to_bin(rom_int))
        # User tries to convert from and to the same numerical system
        elif from_sys == to_sys:
            print('You are trying to convert one numerical system to the same. Please try again')
            menu()
        else:
            print('Invalid input.')
            menu()
        
    except:    
            print('Invalid input')
            menu()
menu()