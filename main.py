import random    #libraries

def get_choices():           #function
    player_choice = input("enter a choice (rock, paper, scissors: )")         # user input
    options = ["rock", "paper", "scissors"]      #list
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}    # dictionary (key value pair)
    return choices



def check_win(player, computer):       #function arguments
    print(f"you chose  {player}, computer chose  {computer}")     #Concatenating Strings  fstrings
    if player == computer:               # if statement                
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you win!"
        else:
            return "paper covers rock! you lose."
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! you win!"
        else:
            return "scissors cuts paper! you lose."
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! you win!"
        else:
            return "Rock smashes scissors! you lose."



choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)