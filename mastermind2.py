import random

#possible color array
colors = ["Y", "G", "B", "R", "W", "O"]

#intiate variables
num_to_generate = 4
guess_countdown = 3
guess_count = 0
computer_selected = []

#grab random colors
for i in range(0, num_to_generate):
    computer_selected.append(random.choice(colors))

#intro
print("Welcome to MasterMind!")
print("Guess the",num_to_generate,"colors from the possibilities: Y G B R W O")

#set successful completion to False
complete = False

#troubleshoot
#print("cpu:",computer_selected)

#loop guessing
while True:
    #break loop when completion is True
    if complete == True:
        break

    #ask for guesses
    user_guess = input("Enter your guess(space between): ").upper()
    user_guess_arr = list(user_guess.replace(" ", ""))

    #save correct and incorrect
    num_correct_pos = 0
    num_incorrect_pos = 0

    #increment guess count and countdown
    guess_count += 1 
    guess_countdown -= 1

    #if guess matches computer completion
    if user_guess_arr == computer_selected and guess_countdown > 0:
        print("You did it in",guess_count,"guesses!")
        print(computer_selected, "was the correct combination.")
        complete = True
    else:
    #if not complete and guesses left check guesses against computer
        if guess_countdown > 0:
            #loop through each color guess
            for idx, u_guess in enumerate(user_guess_arr):
                if u_guess in computer_selected:
                    if user_guess_arr[idx] == computer_selected[idx]:
                        num_correct_pos += 1
                    else:
                        num_incorrect_pos += 1
            #failure message
            print("Not correct.")
            print("Correct Position:",num_correct_pos,"Incorrect Position",num_incorrect_pos)
            print("You have",guess_countdown," guesses left.")
        else:
            #ran out of guesses
            print("Sorry!",computer_selected, "was the correct combination.")
            complete = True
                
