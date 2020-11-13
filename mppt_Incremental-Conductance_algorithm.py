# Based on the Algorithm, Cannot be implemented with hardware. Only Software implementations.
# To run a data set turn the input into any data structure

import random
Vk1 = int(input("Vk1:"))
Ik1 = int(input("Ik1:"))
Pk1 = Vk1 * Ik1


Vk2 = int(input("Vk2:"))
Ik2 = int(input("Ik2:"))
Pk2 = Vk2 * Ik2

delV = Vk2 - Vk1
delI = Ik2 - Ik1
delP = Pk2 - Pk1

Vref = random.randint(250, 550)
print(f"Initial Vref: {Vref}")

if delV == 0:
    if delI == 0:
        print(Vref)
    else:
        if delI > 0:
            Vref = Vref + random.randint(1, 10)
            print(Vref)
        else:
            Vref = Vref - random.randint(1, 10)
            print(Vref)
else:
    if delP/delV == 0:
        print(Vref)
    else:
        if delP/delV > 0:
            Vref = Vref + random.randint(1, 10)
            print(Vref)
        else:
            Vref = Vref - random.randint(1, 10)
            print(Vref)
