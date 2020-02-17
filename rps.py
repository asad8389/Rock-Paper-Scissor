import random


p_win= 0
c_win= 0

while True:
    
    print("...Rock...")
    print("...Paper...")
    print("...Scissor...")

    #choice input
    choice1 = input("enter your choice: ").lower()
    #computer's random choice
    rand_no=random.randint(1,3)

    if rand_no==1:
        comp="rock"
    elif rand_no==2:
        comp="paper"
    else:
        comp="scissor"

    print("computer choose: " + comp)

    #check who win the round
    if choice1 and comp:
        
        if choice1==comp:
            print("its a tie")

        elif choice1=="rock":

            if comp=="paper":
                print("compter won")
                c_win+=1

            else:
                print("player won")
                p_win+=1

        elif choice1=="paper":

            if comp=="scissor":
                print("compter won")
                c_win+=1

            else:
                print("player won")
                p_win+=1

        elif choice1=="scissor":

            if comp=="rock":
                print("compter won")
                c_win+=1

            else:
                print("player won")
                p_win+=1

        else:
            print('wrong enter valid move')

        print("\n\n")
        
        #round winnings 
        print(f"Computer: {c_win}\nPalyer  : {p_win}")

        print("\n\n")

        #check who win 2 rounds first
        if p_win == 2 or c_win == 2:
            #check who win the game
            if p_win > c_win:
                print(" Congratulations player won")
            else:
                print(" Congratulations compter won")
            break
        
    
        






