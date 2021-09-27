import os
import time
def tables():
    number = int(input("Introduce a number: "))
    while number != 0:
        for x in range(11):
            print(number," x ",x," = ",number*x)
        number = int(input("Introduce a number: "))
        os.system('clear')
tables()
