import random
rock   ='👊🏽'
paper  ='✋'
scissor='🖖🏼'
game_images =[rock,paper                   ,scissor]
print(game_images)
print("you are playing (0)ROCK (1)PAPER (2)SCISSORS game with computer")
user_input = int(input("enter your input:-"))
computer_input = random.randint(0,2)
if user_input>0 and user_input<3:
    print(game_images[user_input],"user input")
    print(game_images[computer_input],"computer input")
    #print(f"{user_input} is user input and {computer_input} is computer input")
    if user_input==computer_input:
        print("Game is tiee")
    elif user_input==2 and computer_input==0:
        print("computer win")
    elif user_input==0 and computer_input==2:
        print("user  winn")
    elif user_input > computer_input:
        print("user winns")
    elif user_input < computer_input:
        print("computer winns")

else:
    print("please enter valid number")