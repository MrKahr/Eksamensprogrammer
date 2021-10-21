
def format_number(number):
    ready_number = '{:,}'.format(number)
    return ready_number


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
        
        tiny = x  - big * 1000
        
        tiny_roman = par_int_rom(tiny)
        
        
        print('_'*len(big_roman))
        print(f"{big_roman}{tiny_roman}")
        
    else:
        print(par_int_rom(x))
    

int_to_rom(3888888)
int_to_rom(3888)


def par_rom_int(x):
    rom_num = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" ,"IV", "I" ]
    integers = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    value = 0
    
    for i in range(len(rom_num)):
        while x[:len(rom_num[i])] ==  rom_num[i]:
            value += integers[i]
            x = x[len(rom_num[i]):]

    return value


def roman_to_int(x):
    if ' ' in x:
        a,b = [str(i) for i in x.split(' ')]
        
        big_int = par_rom_int(a)
        tiny_int = par_rom_int(b)
        
        number = (big_int * 1000) + tiny_int
        
        print(format_number(number))
    
    else:
        number = par_rom_int(x)
        print(format_number(number))

g = 'MMMDCCCLXXXVIII DCCCLXXXVIII'
q = 'MMMDCCCLXXXVIII'

roman_to_int(g)
roman_to_int(q)
