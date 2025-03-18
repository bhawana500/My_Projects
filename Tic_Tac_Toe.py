def game():
    zero= "❌" if xState[0]=="X" else "⭕" if zState[0]=="O" else " 0"
    one=  "❌" if xState[1]=="X" else "⭕" if zState[1]=="O" else " 1"
    two= "❌" if xState[2]=="X" else "⭕" if zState[2]=="O" else " 2"
    three= "❌" if xState[3]=="X" else "⭕" if zState[3]=="O" else " 3"
    four= "❌" if xState[4]=="X" else "⭕" if zState[4]=="O" else " 4"
    five= "❌" if xState[5]=="X" else "⭕" if zState[5]=="O" else " 5"
    six= "❌" if xState[6]=="X" else "⭕" if zState[6]=="O" else " 6"
    seven= "❌" if xState[7]=="X" else "⭕" if zState[7]=="O" else " 7"
    eight= "❌" if xState[8]=="X" else "⭕" if zState[8]=="O" else " 8"
    print(f"| {zero} | {one} | {two} |")
    print("|----|----|----|")
    print(f"| {three} | {four} | {five} |")
    print("|----|----|----|")
    print(f"| {six} | {seven} | {eight} |")
    return ""
def win(xState,zState):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for chance in win:
        xcount=0
        ocount=0
        for i in chance:
            if xState[i]=="X":
                xcount+=1
            if zState[i]=="O":
                ocount+=1
        if xcount==3:
            return "X"
        elif ocount==3:
            return "O"
    return ""
if __name__=="__main__":
    choice=int(input(''' <<WELOCOME_TO_TIC_TAC_TOE>>
1. GAME START
2. EXIT
'''))
    xState=["","","","","","","","",""]
    zState=["","","","","","","","",""]
    turn=1
if choice==1:
    print("~~~Game Started~~~")
    place=[]
    print(game())
    while len(place)<10:
        try:
            if turn==1:
                print("[X's Chance]")
                value=int(input("Enter the number at which place you're placing:"))
                if value not in place and value>=0 and value<9:
                    place.append(value)
                    xState[value]="X"
                else:
                    print("The Place has Already been Taken!!")
            elif turn==0:
                print("[O's Chance]")
                value=int(input("Enter a number at which place you're placing:"))
                if value not in place and value>=0 and value<9:
                    place.append(value)
                    zState[value]="O"
                else:
                    print("The Place has Already been Taken!!")
            turn=1-turn
        except IndexError:
            print("Please Enter Valid Place Number(0-8)!!")
        print(game())
        print()
        if win(xState,zState)=="X":
            print("Congrats!!, X WINS")
            break
        if win(xState,zState)=="O":
            print("Congrats!!, O WINS")
            break
        if len(place)==9:
            print("MATCH DRAW")
            break
else:
    print("You Exit the Game")
