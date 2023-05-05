import random
TorF=False
def guessDigit(guess):
    guessNumber=input("enter the number: ")
    if guessNumber.isdigit() and guessNumber!="000":
        if guess==int(guessNumber):
            print("correct answer")
            checkinput()
        else:
            print("wrong answer")
            guessDigit(guess)
    elif guessNumber=="000":
        quit()
    else:
        guessDigit(guess)
def checkinput():
    manual = input( "Enter range 0 between Number: " )
    if manual.isdigit():
        if manual=="000":
            quit()
        elif ((int(manual) == 0) or (int(manual) == 1)):
            checkinput()
        else:
            return int(manual)
    else:
        print("invaild input you give, try again,press 1 to start again/ 0 exit")
        manual = input( "Enter range 0/1 between Number: " )
        if manual=="000":
            quit()
        elif manual.isdigit():
            if int(manual)==1:
                checkinput()
            elif int(manual)==0:
                quit()
        else:
            checkinput()

if __name__ == "__main__":
    while(1):
        obj=checkinput()
        guessRange=random.randint(0,obj)
        guessDigit(guessRange)






