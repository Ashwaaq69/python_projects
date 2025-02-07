import random
import string

Num_Chars = 2  # Number of characters in the secret code
Max_Guesses = 5


def main():
    print(f'''Bagels, a deductive logic game.
I am thinking of a {Num_Chars}-character code using digits (0-9) and letters (A-Z) with no repeats.
Try to guess what it is. Here are some clues:
  When I say:    That means:
    Pico         One character is correct but in the wrong position.
    Fermi        One character is correct and in the right position.
    Bagels       No character is correct.
    ''')
    
    while True:
        secretCode = getSecretCode()
        print('I have thought up a code.')
        print(f'You have {Max_Guesses} guesses to get it.')
        
        numGuesses = 1
        while numGuesses <= Max_Guesses:
            guess = ''
            while len(guess) != Num_Chars or not all(c in string.digits + string.ascii_uppercase for c in guess):
                print(f'Guess #{numGuesses}: ')
                guess = input('> ').upper()
            
            clues = getClues(guess, secretCode)
            print(clues)
            numGuesses += 1
            
            if guess == secretCode:
                break
            if numGuesses > Max_Guesses:
                print(f'You ran out of guesses. The answer was {secretCode}.')
        
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretCode():
    """Returns a string of unique random characters (digits and letters)."""
    chars = list(string.digits + string.ascii_uppercase)
    random.shuffle(chars)
    return ''.join(chars[:Num_Chars])


def getClues(guess, secretCode):
    """Returns clues based on the player's guess."""
    if guess == secretCode:
        return 'You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretCode[i]:
            clues.append('Fermi')
        elif guess[i] in secretCode:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    
    clues.sort()
    return ', '.join(clues)


if __name__ == '__main__':
    main()
