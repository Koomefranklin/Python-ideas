#simple Rock,Paper Scissors game between user and computer with 5 rounds and implementing recursion
#By Koome Franklin
#github.com/Koomefranklin/Pyhton-ideas
import random
def play():
    score = {"user":0, "computer":0}#dictionary to keep score of rounds
    list = ['rock', 'paper', 'scissors']
    for i in range(5):#iterating through to play 5 times
        computer_choice = random.choice(list)
        user_choice = input(f'''
        You will play {5-i} more Rounds before the final score
        Pick one:
        Rock
        Paper
        Scissors\n\n''').lower()
        if user_choice in list:
            #display the choices and round winner if the input is correct
            print (f'''
            \nComputer picked: {computer_choice} 
            You pick: {user_choice}''')
            if computer_choice == user_choice:
                print ( 'Its a draw')
            elif win(user_choice, computer_choice):
                score['user'] +=1#add one to the user score when the user wins
                print ('You win')
            else:
                score['computer'] +=1 #add one to the computer score when the computer wins
                print('You loose')
        else:
            print('Please select a valid choice')
    winner(score)
    answer = input("\n\nWould you like to continue playing? y/N\n").lower()
    play_again(answer)

def winner(score):#print final score and winner
    user_score = score.get('user')
    computer_score = score.get('computer')
    if user_score > computer_score:
        higher = 'User'
    else:
        higher = 'Computer'
    print(f'The score is user: {user_score} wins\n\tComputer: {computer_score} wins\nThe winner is {higher}')

def play_again(answer):#function to replay the game again
    
    if ("y" in answer):
        play()
    else:
        exit()

def win(player, opponent):#function to determine the winner
    if (player == 'rock' and opponent == 'scissors'\
        or player == 'paper' and opponent == 'rock' \
            or player =='scissors'and opponent == 'paper'):
        return True
play()