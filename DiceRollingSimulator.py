import math
import random
import time

min = input("Enter minimum value for dice")
max = input("Enter maximum value for dice")

answer = "yes"

while (answer.lower() == "yes"):
    print("DICE is rolling..")
    time.sleep(2)
    print ("Outcome: ")
    print(random.randrange(int(min), int(max)))
    flag = 1
    while (flag == 1):
        answer = input("Would you like to roll the DICE again?(yes/no)")
        if(answer.lower() == "yes" or answer.lower() == "no"):
            flag = 0
        else:
            print("Please enter valid answer, yes/no..!!")
    
