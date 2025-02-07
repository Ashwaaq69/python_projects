# filepath: /bagles-game/bagles-game/src/bagles.py
import random
import string

Num_Digits_Letters = 4
Max_Guesses = 5

def main():
    print('''Bagles, a deductive logic game.
I am thinking of a {}-character number with no repeated characters.
  Try to guess what it is. Here are some clues:
  When I say:    That means:
    Pico         One character is correct but in the wrong position.
    Fermi        One character is correct and in the right position.
    Bagels       No character is correct.
  For example, if the secret number was 2A4B and your guess was B4A2, the clues would be Fermi Pico.'''.format(Num_Digits_Letters))
    
    while True:  # main game loop
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(Max_Guesses))
        
        numGuesses = 1
        while numGuesses <= Max_Guesses:
            guess = ''
            while len(guess) != Num_Digits_Letters or not isValidGuess(guess):
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break  # They're correct, so break out of this loop.
            if numGuesses > Max_Guesses:
                print('You ran out of guesses. The answer was {}.'.format(secretNum))
        
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Returns a string of unique random digits and letters that is Num_Digits_Letters long."""
    characters = list(string.ascii_uppercase + string.digits)
    random.shuffle(characters)
    secretNum = ''.join(characters[:Num_Digits_Letters])
    return secretNum

def isValidGuess(guess):
    """Checks if the guess is valid (correct length and contains unique characters)."""
    return len(guess) == len(set(guess)) and all(c in string.ascii_uppercase + string.digits for c in guess)

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct character is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct character is in the wrong place.
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    
    # Sort the clues into alphabetical order so their original order
    # doesn't give information away.
    clues.sort()
    # Make a single string from the list of string clues.
    return ', '.join(clues)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()