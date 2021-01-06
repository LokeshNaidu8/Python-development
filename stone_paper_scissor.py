import random

print("\n('--') Rock paper and scissor Game welcomes you ('_') \n")


playonemoretime="y"
while(playonemoretime =="y" or playonemoretime=="Y"):
    yourpoints = 0
    opponentpoints = 0
    total_game=int(input("\nHow many games you want to play : "))

    for i in range(total_game):
        dict={1:"stone",2:"paper",3:"scissor"}
        a=random.choice(list(dict.keys()))
        opponentchoice=dict[a]
        yourchoice=input("\nenter your choice\n"
                         "1.Stone\n"
                         "2.Paper\n"
                         "3.Scissor : ")
        def points():
            print(f"Opponent points : {opponentpoints}\n"
                  f"Your points : {yourpoints}\n")
        def won():
            print(f"\nYou won {i+1} game because opponent chosen {opponentchoice}\n")
            points()
        def draw():
            print(f"\nGame {i+1} ended equally because opponent chosen {opponentchoice}\n")
            points()
        def lose():
            print(f"\nYou lost {i+1} game because opponent chosen {opponentchoice}\n")
            points()

        if yourchoice=="1":
            if a==1:
                draw()
            elif a==2:
                opponentpoints+=1
                lose()
            else:
                yourpoints+=1
                won()
        if yourchoice=="2":
            if a == 1:
                yourpoints+=1
                won()
            elif a == 2:
                draw()
            else:
                opponentpoints += 1
                lose()
        if yourchoice=="3":
            if a == 1:
                opponentpoints+=1
                lose()
            elif a == 2:
                yourpoints+=1
                won()
            else:
                draw()

    if(yourpoints>opponentpoints):
        print("You won the game 😃 \n")
    elif(yourpoints==opponentpoints):
        print("Match has ended in draw\n")
    else:
        print("You lose the game 😔 \n ")

    playonemoretime=input("Do you want to play one more time \n say y/n : ")

print("\n('-_-') Thanks for playing")

