import random
print("|| WELCOME TO THE GAME OF ROCK PAPER SCISSORS || ")
p_1=input ("enter your name player_1 : ")
p_2=input ("enter your name player_2 : ")
print("|| welcome ",p_1, "and ",p_2,'||')
a=["rock","paper","scissors"]

player_1 = random.choice(a)
player_2 = random.choice(a)

if (player_1!=player_2):
    if(player_1=="rock" and player_2=="scissors"):
        if (True):
            print(p_1," WIN")
    elif(player_1=="rock" and player_2=="paper"):
        if (True):
            print(p_2 ," WIN")
    elif(player_1=="paper" and player_2=="rock"):
        if (True):
            print(p_1 ," WIN")
    elif(player_1=="paper" and player_2=="scissors"):
        if (True):
            print(p_2 ," WIN")
    elif(player_1=="scissors" and player_2=="rock"):
        if (True):
            print(p_2 ," WIN")
    elif(player_1=="scissors" and player_2=="paper"):
        if (True):
            print(p_1 ," WIN")
if(player_1==player_2):
    print("IT'S A DRAW")
print("outcome of ",p_1,"is",player_1)
print("outcome of ",p_2,"is",player_2)
