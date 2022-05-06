import random
def play():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    user_choice = input('''
    Pick one:
    Rock
    Paper
    Scissors\n\n''').lower()
    print (f'''
    \nComputer picked: {computer_choice} 
    You pick: {user_choice}''')
    if computer_choice == user_choice:
        print ( 'Its a draw')
    elif win(user_choice, computer_choice):
        print ('You win')

    else:
        print('You loose')
    answer = input("\n\nWould you like to continue playing? y/n\n").lower()
    play_again(answer)

def play_again(answer):
    
    if ("y" in answer):
        play()
    else:
        exit()

def win(player, opponent):
    if (player == 'rock' and opponent == 'scissors'\
        or player == 'paper' and opponent == 'rock' \
            or player =='scissors'and opponent == 'paper'):
        return True
play()