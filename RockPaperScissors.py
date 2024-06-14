import random
def conditions(char1,char2):
    if(char1=='R' and char2=='S'):
        return 1
    elif(char1=='R' and char2=='P'):
        return 0
    elif(char1=='R' and char2=='R'):
        return -1
    elif(char1=='S' and char2=='S'):
        return -1
    elif(char1=='P' and char2=='P'):
        return -1
    elif(char1=='S' and char2=='P'):
        return 1
    elif(char1=='S' and char2=='R'):
        return 0
    elif(char1=='P' and char2=='S'):
        return 0
    elif(char1=='P' and char2=='R'):
        return 1
    return 2

ROUNDS=int(input("ENTER THE NUMBER OF ROUNDS TO BE PLAYED WITH COMPUTER: "))
print("****************ROUND #",1,"****************")
score_player=0
score_computer=0
ties=0
flag=0
i=1
while i<=ROUNDS:
    RSP=''
    player=input("PICK YOUR THROW -> [R]ock, [P]aper, [S]cissors: ")
    if(player!='R' and player!='S' and player!='P'):
        print("INVALID CHOICE AS YOU CHOSE: ",player)
        print("ENTER YOUR CHOICE AGAIN!!")
        print()  
    else:
        computer=random.choice(['R','S','P'])
        result=conditions(player,computer)
        if(computer=='R'):
            RSP="'ROCK'"
        elif(computer=='P'):
            RSP="'PAPER'"
        else:
            RSP="'SCISSORS'"

        if(result==1):
            print("COMPUTER THREW ",RSP," YOU WIN!")
            score_player+=1
            print()
            print("YOUR SCORE: ",score_player)
            print("COMPUTER SCORE: ",score_computer)
            print("TIES: ",ties)
            print()
            if i<ROUNDS:
                print("****************ROUND #",i+1,"****************")
            i+=1
        elif(result==0):
            print("COMPUTER THREW ",RSP," YOU LOST!")
            score_computer+=1
            print()
            print("YOUR SCORE: ",score_player)
            print("COMPUTER SCORE: ",score_computer)
            print("TIES: ",ties)
            print()
            if i<ROUNDS:
                print("****************ROUND #",i+1,"****************")
            i+=1
        else:
            print("COMPUTER THREW ",RSP," There is a TIE!")
            ties+=1
            print("YOUR SCORE: ",score_player)
            print("COMPUTER SCORE: ",score_computer)
            print("TIES: ",ties)
            print()
            if i<ROUNDS:
                print("****************ROUND #",i+1,"****************")
            i+=1

print("The game of ",ROUNDS," matches is complete.The final scores are: ")
print("--------------------FINAL SCORE--------------------")
print("YOUR SCORE: ",score_player)
print("COMPUTER SCORE: ",score_computer)
print("TIES: ",ties)