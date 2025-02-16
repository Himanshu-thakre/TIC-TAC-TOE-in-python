
import os
import random

bn = ["0","1","2","3","4","5","6","7","8","9"]

def board ():
    #board function for game board
    os.system("clear")
    print(">>TIC<•>TAC<•>TOE<<\n")
    print("     |     |    ")
    print(f"  {bn[1]}  |  {bn[2]}  |  {bn[3]}   ")
    print("_____|_____|_____")
    print("     |     |    ")
    print(f"  {bn[4]}  |  {bn[5]}  |  {bn[6]} ")
    print("_____|_____|_____")
    print("     |     |    ")
    print(f"  {bn[7]}  |  {bn[8]}  |  {bn[9]}  ")
    print("     |     |    ")

def win ():
    #win function for checking winning conditions
    if (bn[1]==bn[2] and bn[2]==bn[3]):
        return 1
    elif (bn[4]==bn[5] and bn[5]==bn[6]):
        return 1
    elif(bn[7]==bn[8] and bn[8]==bn[9]):
        return 1
    elif(bn[1]==bn[5] and bn[5]==bn[9]):
        return 1
    elif(bn[3]==bn[5] and bn[5]==bn[7]):
        return 1
    elif(bn[1]==bn[4] and bn[4]==bn[7]):
        return 1
    elif(bn[2]==bn[5] and bn[5]==bn[8]):
        return 1
    elif(bn[3]==bn[6] and bn[6]==bn[9]):
        return 1

    count=0
    for i in range(1,10,1):
        if (bn[i]=='X' or bn[i]=='O'):
            count=count+1
        
    if (count==9):
        return 2



board()
for i in range(5): #This loop will runs 5(max inputs) times 
        
    #taking inputs from user
    a = int(input("\nPlease Enter Any Number>>>")) 
    while (a<1 or a>9 or bn[a]=='X' or bn[a]=='O'):
        print ("×××INVALID INPUT×××")
        a = int(input("Please Enter Any Number>>>"))
    bn[a]='X'
    board()

    #checking winning condition
    win1 = win ()
    if (win1==1):
        print("\n•••YOU WON•••\n\n")
        break
    elif (win1==2):
        print("\n•••DRAW•••\n\n")
        break

    #generates random number between 1 and 9
    b=random.randint(1,9)
    while (bn[b]=='X' or bn[b]=='O' or b<1 or b>9):
        b=random.randint(1,9)
    bn[b]='O'
    board()
        
    #checking winning condition again
    win2 = win ()
    if (win2==1):
        print("\n•••BOT WON•••\n\n")
        break









