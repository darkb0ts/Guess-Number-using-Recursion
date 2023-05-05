import random
Point=5
checkNumber = [ ]
checkNumberTF=True
Question = ["In which decade was the Internet first implemented"," Where are the contents of your computer's hard drive indexed ", "Main circuit board in a computer is:" ,"ISP stands for", "Internet Explorer is a"]

print("Welcome to my computer quiz!")

playing=input("Do you want play [Yes/NO] : ")

if playing!=("Y"):
    print("Quiting")
    quit()
print("Okey Let's play")

while checkNumberTF:
    numberRad = random.randint( 0 , 4 )
    if (Point <=-1 or Point == 0 or len(checkNumber)==len(Question)):
        checkNumberTF=False
        continue
    elif numberRad not in checkNumber:
        checkNumber.append( numberRad )
        if numberRad == 0 :
            print( Question [numberRad] )
            answer = input( "enter the answer: " )
            if answer == "1960" :
                print( "Correct Answer" )
                continue
            else :
                print( "Wrong Answer" )
                Point -= 1
        elif numberRad == 1 :
            print( Question [numberRad] )
            answer = input( "enter the answer: " )
            if answer == "Google" :
                print( "Correct Answer" )
                continue
            else :
                print( "Wrong Answer" )
                Point -= 1
        elif numberRad == 2 :
            print( Question [numberRad] )
            answer = input( "enter the answer: " )
            if answer == "Decoder" :
                print( "Correct Answer" )
                continue
            else :
                print( "Wrong Answer" )
                Point -= 1
        elif numberRad == 3 :
            print( Question [numberRad] )
            answer = input( "enter the answer: " )
            if answer == "Internet Survey Period" :
                print( "Correct Answer" )
                continue
            else :
                print( "Wrong Answer" )
                Point -= 1
        elif numberRad == 4 :
            print( Question [numberRad] )
            answer = input( "enter the answer: " )
            if answer == "Web Browser" :
                print( "Correct Answer" )
                continue
            else :
                print( "Wrong Answer" )
                Point -= 1
    else:
        continue
if Point>=3:
    print("your score is good",Point)
else:
    print("sorry try again",Point)

# 1940,Google,Decoder,Internet Survey Period,Web Browser