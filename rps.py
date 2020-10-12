#program of rock paper and scissor game between computer and the user. 

import random
#moves for Computer
moves = ["r","p", "s"]
Keep_playing = "true"

#while loop
while Keep_playing == "true":
    cmove = random.choice(moves)
    pmove = input("Enter your choice: r, p or s?")

    print("the computer choice : ", cmove)

    if cmove == pmove:
        print("Tie")
    elif pmove == "r" and cmove == "p":
        print("Computer won the game")
    elif pmove == "r" and cmove == "s":
        print("Player won the game")
    elif pmove == "p" and cmove == "r":
        print("Player won the game")
    elif pmove == "s" and cmove == "p":
        print("Player won the game")
    elif pmove == "s" and cmove == "r":
        print("Player won the game")
    elif pmove == "p" and cmove == "s":
        print("Player won the game")    
        
    else:
        print("Please enter the valid inputs ['r','p','s']")

        print("\n")
        continue_input = input("Want to play again? (Y/N): ").casefold()
        print("\n")

        if(continue_input == 'y') or (continue_input == 'yes'):
            continue
        else:
            print("see you again. Bye")
            break
  

        
        

