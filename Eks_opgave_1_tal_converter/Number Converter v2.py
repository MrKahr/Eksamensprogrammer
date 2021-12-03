'''
Link til github: https://github.com/MrKahr/Eksamensprogrammer
Anden eksamens opgave i IPD: Number converter.
@authors: Mads Andersen, Eric van den Brand, Daniel Hansen, Thor Skatka og Andreas Hansen
Beskrivelse: Programmet converterer bruger defineret tal, blandt binære tal, romer tal og 10 tals systemet.
'''

rom_num = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


# ! integer formatting function
def FormatNumber(number):
    # Formates number with , for added readability
    # f. eks.: 1000000 --> 1,000,000
    ready_number = '{:,}'.format(number)
    
    return ready_number


# ! IntToBin to convert integer to binary
def IntToBin(x):
    # Create an empty string, then take the entered integer and modulus by 2
    a = ''
    
    # Add the modulus to the string, then use floor division to redefine the entered number
    # Perform until x == 0. 
    while x > 0:
        n = x % 2
        a += str(n)
        x = x // 2
    
    z = a[::-1]  # Reverse the string
    
    return z


# ! ParIntRom and IntToRom convert integers to roman numerals
def ParIntRom(x):
    i = 0
    rom_str = ''  # Creates en empty string
    
    # If x // integers[i] > 0, it adds the roman numeral to rom_str and subtracts integers[i] form x
    # When x // inegers[i] > 0  not anymore, then it repeats for integers[i+1], until end of integers
    while x > 0:
        while (x // integers[i]) > 0:
            rom_str += rom_num[i]
            x -= integers[i]
        
        i += 1
    
    return rom_str  # It then returns rom_str


def IntToRom(x):
    if x >= 4000:  # If x >= 4000, it splits x in two parts:
        big = x // 1000  # Big part, wich are the roman numerals that need to be multiplied by 1000
        tiny = x - big * 1000  # And tiny part, wich is whats left of x after big is subtracted
        
        # big_rom and tiny_rom are then made by ParIntRom
        big_rom = ParIntRom(big)
        tiny_rom = ParIntRom(tiny)
        
        roof = '_' * len(big_rom)  # roof is then made in length of big_rom
        print_ready_rom = f'{big_rom}{tiny_rom}'  # big_rom and tiny_rom are added together
        
        # And the roman numeral gets printed as one big multiline string
        print_it_all = f'''{roof}\n{print_ready_rom}'''
        
        return print_it_all
    
    else:  # If x < 4000 it just returns ParIntRom(x)
        return ParIntRom(x)


# ! BinToInt converts binary numbers to integers
def BinToInt(x):
    x = [int(x) for x in str(x)]  # Make a list of the digits.
    t = 0  # Make a 'total'
    
    # Multiply t by 2 and add digit for each digit in the list
    for num in x:
        t = 2 * t + num
    
    number = FormatNumber(t)
    
    return number


# ! ParIntRom and RomToInt convert roman numerals to integers
def ParRomInt(x):
    value = 0
    
    # Goes through rom_num list, if first part of x == rom_num[i]: value += integers[i]
    # Delete first part it found a value for, and repeats
    # When it doesnt find a match for rom_num[i], 
    # it goes to rom_num[i+1] and repeats until end of rom_num
    for i in range(len(rom_num)):
        while x[:len(rom_num[i])] == rom_num[i]:
            value += integers[i]
            
            x = x[len(rom_num[i]):]
    
    return value


def RomToInt(x):
    # Space means that the first part is multiplied by 1000
    if ' ' in x:
        # Splits string into big_rom and tiny_rom
        big_rom, tiny_rom = [str(i) for i in x.split(' ')]
        
        # Runs ParIntRom for big_rom and tiny_rom
        big_int = ParRomInt(big_rom)
        tiny_int = ParRomInt(tiny_rom)
        
        # Adds big_int * 1000 and tiny_int together
        number = (big_int * 1000) + tiny_int
        
        return FormatNumber(number)
    
    else:  # If x has no ' ', run ParIntRom and return result
        number = ParRomInt(x)
        return FormatNumber(number)


# ! Menu function is defined
def Menu():
    try:
        # Ask user for input
        from_sys = input('''Please choose your number system
        #1. Decimal
        #2. Binary
        #3. Roman
        #4. Terminate Program
        --->: ''')
        
        assert from_sys in ['1', '2', '3', '4']  # Checks if input is valid
        
        user_number = input('''Please enter your number (if its a roman numeral of 4000 
        and above, please type a space after the part that needs to be multiple by 1000): 
        --->: ''')
        
        if from_sys == '1':  # Sets from_sys to int, if decimal was chosen
            user_number = int(user_number)
        
        if from_sys == '2':
            # Creates set of all unique elements in user_number
            # Checks if user_number includes only 0 and 1
            assert set(user_number) == {'0', '1'}
        
        if from_sys == '3':  # Checks if roman numeral is invalid input
            list_u = list(user_number)
            
            for i in list_u:
                if i != ' ':
                    assert i in rom_num
        
        if from_sys == '4':  # Terminates program
            print('You terminated the program')
            
            return
        
        to_sys = input('''Please choose the numerical system you want to convert to
        #1. Decimal
        #2. Binary
        #3. Roman
        --->: ''')
        
        assert to_sys in ['1', '2', '3']  # Checks if input is valid
        
        # Convert number from system to system based on user input
        # User tries to convert from and to the same numerical system
        if from_sys == to_sys:
            print('You are trying to convert one numerical system to the same. Please try again')
            
            Menu()
        
        elif from_sys == '1':
            if to_sys == '2':  # int to bin
                print(IntToBin(user_number))
            
            elif to_sys == '3':  # int to rom
                print(IntToRom(user_number))
        
        elif from_sys == '2':
            if to_sys == '1':  # bin to int
                print(BinToInt(user_number))
            
            elif to_sys == '3':  # bin to rom
                bin_int = BinToInt(user_number)
                
                print(IntToRom(bin_int))  # int to rom
        
        elif from_sys == '3':
            if to_sys == '1':  # rom to int
                print(RomToInt(user_number))
            
            elif to_sys == '2':  # rom to bin
                rom_int = RomToInt(user_number)
                
                print(IntToBin(rom_int))  # int to bin
        
        else:  # Loops for invalid input
            print('Something unexpected went wrong')
            
            Menu()
    
    except:  # Loops for invalid input
        print('Invalid input')
        
        Menu()


Menu()
