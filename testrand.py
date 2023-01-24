import os
import time
import random

def main():
    count16 = 0
    count14 = 0

    for i in range(0, 1000000000000, 1):
            
        x = random.randrange(1, 17)
        if (x == 16):
            count16 += 1
        else:
            if (x == 14):
                count14 += 1

        if (count16 == 1000000 or count14 == 1000000):
            break
            
    print( " 16:", count16)
    print('\n',"14:", count14)


if __name__ == "__main__":
    main()