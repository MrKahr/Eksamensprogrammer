
"""
Created on Wed Oct 20 13:20:32 2021
@author: @authors: Mads Andersen, Eric van den Brand, Daniel Hansen, Thor Skatka og Andreas Hansen
"""


def format_number(number):
    ready_number = '{:,}'.format(number)
    return ready_number


# ! int_to_bin to convert integer to binary
# Create an empty list, then take the entered integer and modulus by 2
# Add the modulus to the list, then use floor division to redefine the entered number
# Perform until i < 0. Reverse the list, print the list
def int_to_bin(x):
    a = ""
    while x > 0:
        n = x % 2
        a += str(n)
        x = x // 2
    z = a[::-1] #Reverse the string
    return z
        

# ! par_int_rom and int_to_rom convert integers to roman numerals
def par_int_rom(x):
        rom_num = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" ,"IV", "I" ]
        integers = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
        
        i = 0
        rom_str = ""
        
        while x > 0:
            while (x // integers[i]) > 0:
                rom_str += rom_num[i]
                x -= integers[i]
            i+=1
        
        return rom_str


def int_to_rom(x):
    if x >= 4000:
        big = x // 1000
        big_roman = par_int_rom(big)
        
        tiny = x - big * 1000
        tiny_roman = par_int_rom(tiny)
        
        roof = '_' * len(big_roman)
        print_ready_roman = f"{big_roman}{tiny_roman}"
        
        print_it_all = f'''{roof}\n{print_ready_roman}'''
        
        return print_it_all
        
    else:
        return par_int_rom(x)
    

# ! bin_to_int converts binary numbers to integers
def bin_to_int(x):
    x = [int(x) for x in str(x)] # Make a list of the digits.
    t = 0 # Make a "total"
    
    # Multiply t by 2 and add digit for each digit in the list
    for num in x: 
        t = 2 * t + num
    number = format_number(t)
    
    return number


# ! par_rom_int and rom_to_int convert roman numerals to integers
def par_rom_int(x):
    rom_num = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" ,"IV", "I" ]
    integers = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    value = 0
    
    for i in range(len(rom_num)):
        while x[:len(rom_num[i])] ==  rom_num[i]:
            value += integers[i]
            x = x[len(rom_num[i]):]

    return value


def rom_to_int(x):
    if ' ' in x:
        big_rom,tiny_rom = [str(i) for i in x.split(' ')]
        
        big_int = par_rom_int(big_rom)
        tiny_int = par_rom_int(tiny_rom)
        
        number = (big_int * 1000) + tiny_int
        
        return format_number(number)
    
    else:
        number = par_rom_int(x)
        return format_number(number)


# Menu function is defined
def menu():
    try:
        # Ask user for input
        from_sys = input('''Please choose your number system
        #1. Decimal
        #2. Binary
        #3. Roman
        --->: ''')
        
        user_number = input('''Please enter your number (if its a roman numeral of 4000 
        and above, please type a space after the part that needs to be multiple by 1000): 
        --->: ''')

        to_sys = input('''Please choose the numerical system you want to convert to
        #1. Decimal
        #2. Binary
        #3. Roman
        --->: ''')
            
        # Convert number from system to system based on user input  
        if from_sys == '1' and to_sys == '2': # int to bin
            print(int_to_bin(int(user_number)))
            
        elif from_sys == '1' and to_sys == '3': # int to rom
            print(int_to_rom(int(user_number)))
            
        elif from_sys == '2' and to_sys == '1': #bin to int
            print(bin_to_int(user_number))
            
        elif from_sys == '3' and to_sys == '1': #rom to int
            print(rom_to_int(user_number))
            
        elif from_sys == '2' and to_sys == '3': # bin to rom
            bin_int = bin_to_int(user_number)
            print(int_to_rom(bin_int)) # rom to bin
            
        elif from_sys == '3' and to_sys == '2':
            rom_int = rom_to_int(user_number)
            print(int_to_bin(int(rom_int)))
            
        # User tries to convert from and to the same numerical system
        elif from_sys == to_sys:
            print('You are trying to convert one numerical system to the same. Please try again')
            return
            #menu()
            
        else:
            print('Invalid input.')
            return 
            #menu()
        
    except:    
            print('Invalid input')
            return
            #menu()
            
menu()