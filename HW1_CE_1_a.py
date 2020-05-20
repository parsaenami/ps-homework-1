import random

number_of_experiment = [10, 100, 1000, 10000]
exp1_n = 0
exp1_f = 0
a = b = index = None

for x in number_of_experiment:
    index = x
    while x != 0:
        a = random.randrange(0, 2)
        b = random.randrange(0, 2)
        if a == 1:
            x -= 1
            exp1_n += 1
            if b == 1:
                exp1_f += 1

    print(f'for {index} experiments the answer is : {exp1_f / exp1_n}')