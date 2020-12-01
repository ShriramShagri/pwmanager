import random 

def generator(passlen):
    SYMBOLS = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '~!@#$%^&*()_+=-\\][|}{;:/,?><']
    COMBINED_LIST = list(SYMBOLS[0]) + list(SYMBOLS[1]) + list(SYMBOLS[2]) + list(SYMBOLS[3]) 
    
    rand_digit = random.choice(list(SYMBOLS[0])) 
    rand_upper = random.choice(list(SYMBOLS[2])) 
    rand_lower = random.choice(list(SYMBOLS[1])) 
    rand_symbol = random.choice(list(SYMBOLS[3])) 

    password = rand_digit + rand_upper + rand_lower + rand_symbol 
    
    for x in range(passlen - 4): 
        password = password + random.choice(COMBINED_LIST) 
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

    return password