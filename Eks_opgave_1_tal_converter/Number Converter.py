
'''
Link til github:
https://github.com/MrKahr/Eksamensprogrammer

Anden eksamens opgave i IPD: Number converter.

@authors: Mads Andersen, Eric van den Brand, Daniel Hansen, Thor Skatka og Andreas Hansen

Beskrivelse: Programmet converterer bruger defineret tal, 
blandt binære tal, romer tal og 10 tals systemet.

P.S.: Navn ved afsnit indikerer afsnittetes hovedforfatter.
'''


# ! integer formatting function (Eric)
def format_number(number):
    # Formates number with , for added readability
    # f. eks.: 1000000 --> 1,000,000
    ready_number = '{:,}'.format(number)
    
    return ready_number


# ! int_to_bin to convert integer to binary (Daniel)
def int_to_bin(x):
    # Create an empty string, then take the entered integer and modulus by 2
    a = ''
    
    # Add the modulus to the string, then use floor division to redefine the entered number
    # Perform until x == 0. 
    while x > 0:
        n = x % 2
        a += str(n)
        x = x // 2
    
    z = a[::-1] # Reverse the string
    
    return z
        

# ! par_int_rom and int_to_rom convert integers to roman numerals (Andreas, Eric og Thor)
def par_int_rom(x):
    rom_num = ['M' , 'CM' , 'D' , 'CD' , 'C' , 'XC' , 'L' , 'XL' , 'X' , 'IX' , 'V' ,'IV', 'I' ]
    integers = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    
    i = 0
    rom_str = '' # Creates en empty string
    
    # If x // integers[i] > 0, it adds the roman numeral to rom_str and subtracts integers[i] form x
    # When x // inegers[i] > 0  not anymore, then it repeats for integers[i+1], until end of integers
    while x > 0:
        while (x // integers[i]) > 0:
            rom_str += rom_num[i]
            x -= integers[i]
            
        i+=1
    
    return rom_str # It then returns rom_str

 
def int_to_rom(x):
    if x >= 4000: # If x >= 4000, it splits x in two parts:
        big = x // 1000 # Big part, wich are the roman numerals that need to be multiplied by 1000
        tiny = x - big * 1000 # And tiny part, wich is whats left of x after big is subtracted
        
        # big_rom and tiny_rom are then made by par_int_rom
        big_rom = par_int_rom(big)
        tiny_rom = par_int_rom(tiny)
        
        roof = '_' * len(big_rom) # roof is then made in length of big_rom
        print_ready_rom = f'{big_rom}{tiny_rom}' # big_rom and tiny_rom are added together
        
        # And the roman numeral gets printed as one big multiline string
        print_it_all = f'''{roof}\n{print_ready_rom}'''
        
        return print_it_all
        
    else: # If x < 4000 it just returns par_int_rom(x)
        return par_int_rom(x)
    

# ! bin_to_int converts binary numbers to integers (Daniel)
def bin_to_int(x):
    x = [int(x) for x in str(x)] # Make a list of the digits.
    t = 0 # Make a 'total'
    
    # Multiply t by 2 and add digit for each digit in the list
    for num in x: 
        t = 2 * t + num
        
    number = format_number(t)
    
    return number


# ! par_rom_int and rom_to_int convert roman numerals to integers (Eric og Thor)
def par_rom_int(x):
    rom_num = ['M' , 'CM' , 'D' , 'CD' , 'C' , 'XC' , 'L' , 'XL' , 'X' , 'IX' , 'V' ,'IV', 'I' ]
    integers = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    
    value = 0
    
    # Goes through rom_num list, if first part of x == rom_num[i]: value += integers[i]
    # Delete first part it found a value for, and repeats
    # When it doesnt find a match for rom_num[i], 
    # it goes to rom_num[i+1] and repeats until end of rom_num
    for i in range(len(rom_num)):
        while x[:len(rom_num[i])] ==  rom_num[i]:
            value += integers[i]
            
            x = x[len(rom_num[i]):]

    return value


def rom_to_int(x):
    if ' ' in x:
        # Splits string into big_rom and tiny_rom
        big_rom,tiny_rom = [str(i) for i in x.split(' ')]
        
        # Runs par_rom_int for big_rom and tiny_rom
        big_int = par_rom_int(big_rom)
        tiny_int = par_rom_int(tiny_rom)
        
        # Adds big_int * 1000 and tiny_int together
        number = (big_int * 1000) + tiny_int
        
        return format_number(number)
    
    else: # If x has no ' ', run par_rom_int and return result
        number = par_rom_int(x)
        return format_number(number)


# ! Menu function is defined (Andreas og Mads)
def menu():
    try:
        # Ask user for input
        from_sys = input('''Please choose your number system
        #1. Decimal
        #2. Binary
        #3. Roman
        #4. Terminate Program
        --->: ''')
        
        if from_sys == '4': # Terminates program
            print('You terminated the program')
            
            return
        
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
            
        elif from_sys == '2' and to_sys == '1': # bin to int
            print(bin_to_int(user_number))
            
        elif from_sys == '3' and to_sys == '1': # rom to int
            print(rom_to_int(user_number))
            
        elif from_sys == '2' and to_sys == '3': # bin to rom
            bin_int = bin_to_int(user_number)
            
            print(int_to_rom(bin_int)) # int to rom
            
        elif from_sys == '3' and to_sys == '2': # rom to bin
            rom_int = rom_to_int(user_number)
            
            print(int_to_bin(int(rom_int))) # int to bin
            
        # User tries to convert from and to the same numerical system
        elif from_sys == to_sys:
            print('You are trying to convert one numerical system to the same. Please try again')
            
            menu()
            
        else: # Loops for invalid input
            print('Invalid input: from_sys or to_sys error')
            
            menu()
        
    except: # Loops for invalid input
            print('Invalid input: user_number error')
            
            menu()


menu()