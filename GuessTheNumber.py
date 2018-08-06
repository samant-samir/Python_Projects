import math
import random
import time

choice1 = "yes"
choice2 = "yes"
while(choice1.lower() == "yes"):
    print("Generating random number....")
    randomNumber = random.randint(0,9)
    time.sleep(2)
    print("Random number generated..!!")
    choice2 = "yes"
    while(choice2.lower() == "yes"):
        print("Guess the number: ")
        answer = input()
        if(answer.isnumeric()):
            difference = randomNumber - int(answer)
            if(difference == 0):
                print("Great..!! you've guessed the number correctly..!!")
                flag = 1
                while (flag == 1):
                    print("Would you like to play again?(yes/no)")
                    choice1 = input()
                    if(choice1.lower() == "yes" or choice1.lower() == "no"):
                        flag = 0
                        choice2 = "no"
                    else:
                        print("Please enter valid answer, yes/no..!!")

            elif(difference > 0):
                print("Ooops.. The number you guessed is smaller than the generated number..!!")
                flag = 1
                while(flag == 1):
                    print("Would you like to guess again?(yes/no)")
                    choice2 = input()
                    if(choice2.lower() == "yes"):
                        flag = 0
                    elif(choice2.lower() == "no"):
                        flag2 = 1
                        while (flag2 == 1):
                            print("Would you like to play again?(yes/no)")
                            choice1 = input()
                            if(choice1.lower() == "yes" or choice1.lower() == "no"):
                                flag2 = 0
                                flag = 0
                            else:
                                print("Please enter valid answer, yes/no..!!")
                    else:
                        print("Please enter valid answer, yes/no..!!")
            else:
                print("Ooops.. The number you guessed is greater than the generated number..!!")
                flag = 1
                while(flag == 1):
                    print("Would you like to guess again?(yes/no)")
                    choice2 = input()
                    if(choice2.lower() == "yes"):
                        flag = 0
                    elif(choice2.lower() == "no"):
                        flag2 = 1
                        while (flag2 == 1):
                            print("Would you like to play again?(yes/no)")
                            choice1 = input()
                            if(choice1.lower() == "yes" or choice1.lower() == "no"):
                                flag2 = 0
                                flag = 0
                            else:
                                print("Please enter valid answer, yes/no..!!")
                    else:
                        print("Please enter valid answer, yes/no..!!")    
            
