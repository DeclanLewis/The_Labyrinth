# The author of this file is Declan Lewis. Made 30th of May 2024.

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









