#Rock Paper Scissors
import random as r

def playing():
    try:
        user_move=str(input("Pick Your Choice: R P S"))
    except TypeError,ValueError:
        print("Enter a valid move.\n")
    else:
        return user_move

def mvt(x):
    if x=="r":
        return("Rock.")
    elif x=="p":
        return("Paper.")
    elif x=="s":
        return("Scissors.")
    elif x=="q":
        return("to quit.\n")
    else:
        return("an invalid move.\n")

moves=("r","p","s")
pscore=0
cscore=0

#Starting a game
getgame=str(input("Enter B to start playing, Q to quit."))
getgame=getgame.casefold()
while getgame=="b":
    user_move=playing()
    user_move.casefold()

#Quit Game
    if user_move=="q":
        getgame="q"

#Gameplay
    print("You have chosen "+mvt(user_move))
    if user_move in moves:
        bot_move=r.choice(moves)
        print("The computer picked "+mvt(bot_move))
        if user_move==bot_move:
            print("Tie.\n")
        elif user_move=="r" and bot_move=="s" or user_move=="p" and bot_move=="r" or user_move=="s" and bot_move=="p":
            pscore+=1
            print("You scored a point!\n")
        else:
            cscore+=1
            print("Computer scores a point!\n")       

#Game Over
else:
    print("Game Over!\n\tSCOREBOARD:")
    print(f"Player: {pscore}, Computer: {cscore}")
    if pscore>cscore:
        print("You won!")
    elif cscore>pscore:
        print("Computer won!")
    else:
        print("No result.")