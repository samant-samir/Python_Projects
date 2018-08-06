import random

words = ['apple','book','cat','dog','elephant']
wordSelected = words[random.randint(0,4)]
print("Welcome to Hangman game..!!\nStart guessing the word, guess it correctly before your Man is hunged..")
count = 0
flag = 0
while count < 7:
    guessAlphabet = input("Enter your guess (one alphabet at a time):")
    if guessAlphabet.isalpha() == 0:
        print("Please enter only alphabets (one alphabet at a time)")
        continue
    if len(guessAlphabet) > 1:
        print("Please enter only one alphabet at a time..!!")
        continue
    posList = [pos for pos, char in enumerate(wordSelected) if char == guessAlphabet]
    if not posList:
        count += 1
        print("Wrong guess..!! Remaining lives : " + str(7-count))
        continue
    outPut = "*"
    outPut = outPut.ljust(len(wordSelected), "*")
    outPutList = list(outPut)
    inPutList = list(wordSelected)
    for i in posList:
        outPutList[int(i)] = inPutList[int(i)]

    astrList = [pos for pos, char in enumerate(str(outPutList)) if char == '*']
    if not astrList:
        flag = 1
        break
    print("Correct..!! The word is : " + str(outPutList) + "\nKeep Guessing..")

if flag == 1:
    print("Congratulations..!! You've won..")
else:
    print("Sorry you couldn't save the man..")
