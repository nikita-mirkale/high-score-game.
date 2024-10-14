'''
The game() function in a program let's a user play a game and returns the score as an integer. You need to read a file "highscore.txt" which is either blank or contains the previous highscore. You need to write a program to update the highscore wherever the game() function breaks the highscore.

'''



import random

def game():
    print("You are playing the game...")
    score = random.randint(1,100)

    #fetch the highscore

    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore !=""):
            highscore = int(highscore)
        else:
            highscore = 0


    print(f"Your score: {score}")
    if(score>highscore):
        #write this highscore to the file
        with open("highscore.txt","w") as f:
            f.write(str(score))

    return score


print(game())