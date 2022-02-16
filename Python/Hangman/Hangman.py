import random
from Words import words
import string
from hangman_visual import lives_visual_dict

print('Click enter to begin')
def get_valid_word(words):
    word = random.choice(words) #randomly cooses word from list file
    while '-' in word or ' ' in word:
        word= random.choice(words)

    return word.upper()

def hangman():
    
    word= get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user guessed

    #getting user input
    user_letter= input('Guess a letter: ').upper()

    lives = 7
    
    while len(word_letters)>0 and lives > 0:
        print('You have',lives,'lives. You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print(user_letter, 'is not in word')
        elif user_letter in used_letters:
            print('You have already used that character, please guess again')

        else:
            print('That is not a valid letter')
    if lives==0:
        print(lives_visual_dict[lives])
        print('Sorry you died! The word was', word)
    else:
        print('You guessed the word!')

hangman()
