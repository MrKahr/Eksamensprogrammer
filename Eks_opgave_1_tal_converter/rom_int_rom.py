
def partial_int_rom(x):
        roman_numerals = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" ,"IV", "I" ]
        integers = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
        i = 0
        roman_string = ""
        
        while x > 0:
            while (x // integers[i]) > 0:
                roman_string += roman_numerals[i]
                x -= integers[i]
            i+=1
        
        return roman_string


def integer_to_roman(x):
    if x >= 4000:
        big = x // 1000
        
        big_roman = partial_int_rom(big)
        
        tiny = x  - big * 1000
        
        tiny_roman = partial_int_rom(tiny)
        
        
        print('_'*len(big_roman))
        print(f"{big_roman}{tiny_roman}")
    

integer_to_roman(3888888)


def partial_rom_int(x):
    roman_numerals = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" ,"IV", "I" ]
    integers = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    value = 0
    for i in range(len(roman_numerals)):
        while x[:len(roman_numerals[i])] ==  roman_numerals[i]:
            value += integers[i]
            x = x[len(roman_numerals[i]):]
    return value


def roman_to_int(x):
    if ' ' in x:
        a,b = [str(i) for i in x.split(' ')]
        
        big_int = partial_rom_int(a)
        tiny_int = partial_rom_int(b)
        
        print((big_int * 1000) + tiny_int)
    
    else:
        print(partial_rom_int(x))    

g = 'MMMDCCCLXXXVIII DCCCLXXXVIII'

roman_to_int(g)