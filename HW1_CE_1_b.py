import math
import random
import numpy as np
import pandas as pd

number_of_experiment = [10, 100, 1000, 10000]
exp2_n = 0
exp2_f = 0
a = b = a_prime = b_prime = index = None

for x in number_of_experiment:
    index = x
    while x != 0:
        a = random.randrange(0, 2)
        b = random.randrange(0, 2)
        if random.randrange(0, 2):
            a_prime, b_prime = a, b
        else:
            a_prime, b_prime = b, a
        if a_prime == 1:
            x -= 1
            exp2_n += 1
            if b_prime == 1:
                exp2_f += 1

    print(f'for {index} experiments the answer is : {exp2_f / exp2_n}')