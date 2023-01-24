import os

def _cal( n):
    temp = 1
    sum = 0

    for i in range (1, n + 1, 1):
        temp *= i
        sum += temp

    print (sum)

def _ex4(x, n):
    temp = 1
    sum = 1
    next_operator = False

    if (n == 1):
        return 1    

    for i in range (2, n + 1, 2):
        temp *= i - 1
        temp *= i

        if (next_operator == False): 
            sum -= pow(x, i)/ temp
            next_operator = True
        else: 
            sum += pow(x, i)/ temp
            next_operator = False

    return sum


def main():


    print (_ex4(3, 4))
    
if __name__ == "__main__":
    main()