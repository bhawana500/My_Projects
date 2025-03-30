import random                  # Importing the random module
l=['rock','paper','scissors']
uc=int(input("""~~~WELCOME TO THE GAME~~~
1> Play                                          
2> Exit
"""))
while True:  # Taking users choice if wants to play or not
    ccount=0   # using ucount and ccount to count the scores
    ucount=0 
    if uc==1:
        for i in range(1,6):                  # There will be total 5 round
            print(f"\nRound {i}-->")            # helps to know which round it is 
            uchoice=int(input(""" Select your Choice: 
    1. Rock
    2. Paper
    3. Scissor
"""))                                                # taking user choice
            if uchoice>3:                            # if user enters invalid choice the giving another chance to choose correct 
                print("Please Enter Valid Choice!!")
                uchoice=int(input(""" Select your Choice:
    1. Rock
    2. Paper
    3. Scissor
"""))
            uchoice=l[uchoice-1]                 
            cchoice=random.choice(l)           # with help of the random module taking computer's choice
            print(f"Your choice is '{uchoice}'")
            print(f"Computer's choice is '{cchoice}'\n")
            if (uchoice=='rock' and cchoice=='scissors') or (uchoice=='scissors' and cchoice=='paper') or (uchoice=='paper' and cchoice=='rock'):  # if any of these conditions came user will win a point
                ucount+=1
                print(f"##You win in round {i}##\n")
            elif uchoice==cchoice:   # if the choice is equal both will gets a point
                print(f"##Draw in round {i}##\n")
                ucount+=1
                ccount+=1
            else:                   # computer will get one point
                print(f"##Computer wins in round {i}##\n")
                ccount+=1
        if ucount>ccount and uc!=2:                                        # counting the final Results
            print(f"<<<Congratulations!, You Win with {ucount} points>>>")
        elif ucount<ccount and uc!=2:
            print(f"<<<Computer wins with {ccount} points>>>")
        elif ucount==ccount and uc!=2:
            print(f"<<<Draw with {ccount} points>>>")
        c=input("\nDo you want to Play Again(y/n):")  # checks if user wanted to play again or not
        if c=='y':
            continue
        else:
            print("Your Exit the Game.")
    elif uc==2:    # if user don't wanted to play, can exit the game. 
        print("You Exit the Game.")
        break
    break
