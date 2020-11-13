# Based on the Algorithm, Cannot be implemented with hardware. Only Software implementations.
# To run a data set turn the input into any data structure

import random
Vk1 = int(input("Vk1:"))
Ik1 = int(input("Ik1:"))
Pk1 = Vk1 * Ik1


Vk2 = int(input("Vk2:"))
Ik2 = int(input("Ik2:"))
Pk2 = Vk2 * Ik2


Vref = random.randint(250, 550)
print(f"Initial Vref: {Vref}")

if Pk2 - Pk1 == 0:
    print(Vref)
else:
    if Pk2 - Pk1 > 0:
        if Vk2 - Vk1 > 0:
            Vref = Vref + random.randint(1, 10)
            print(Vref)
        else:
            Vref = Vref - random.randint(1, 10)
            print(Vref)
    else:
        if Vk2 - Vk1 > 0:
            Vref = Vref - random.randint(1, 10)
            print(Vref)
        else:
            Vref = Vref + random.randint(1, 10)
            print(Vref)
