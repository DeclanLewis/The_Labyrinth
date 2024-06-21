# The author of this file is Declan Lewis. Made 30th of May 2024.
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license this is why I will be using a GNU
# This was testing out the random library for random occurrences in the game e.g loud ambience sounds.

import random

chance = 0.0000001
run = True
trapped = False
trapped2 = 6
day = 1

while run:
    if random.random() <= chance:
        print("yes")
        trapped2 = trapped2 + 50
        trapped = True
    else:
        trapped = False

    while trapped:
        while trapped2 >10:
            print("trapped")
            day = day + 1
            if day == 7:
                trapped2 = trapped2 -100

    print("done")









