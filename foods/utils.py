

import random

def generate_random_id():    
    chars= '1234567890'
    randomstr1 = ''.join((random.choice(chars)) for x in range(10))
    randomstr2 = ''.join((random.choice(chars)) for x in range(8))
    absolute_id = randomstr1 + "_" + randomstr2
    return absolute_id