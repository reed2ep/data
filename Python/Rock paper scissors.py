import random

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n ")
    computer= random.choice(['r','p','s'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return "You win"

    return 'You lost!'

def is_win(player, opponent):
    #return true if player wins
    if(player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's'):
        return True

print(play())
