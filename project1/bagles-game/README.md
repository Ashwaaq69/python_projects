# Bagles Game

## Overview
Bagles is a deductive logic game where players try to guess a secret number that consists of both digits and letters. The game provides clues based on the player's guesses, helping them to deduce the correct answer.

## Game Rules
- The secret number is a combination of unique digits (0-9) and letters (A-F).
- Players have a limited number of guesses to find the secret number.
- After each guess, players receive feedback in the form of clues:
  - **Fermi**: A correct digit/letter is in the correct position.
  - **Pico**: A correct digit/letter is in the wrong position.
  - **Bagels**: No digit/letter is correct.

## How to Play
1. Run the game by executing the `bagles.py` script in the `src` directory.
2. Follow the prompts to enter your guesses.
3. Use the clues provided after each guess to refine your next guess.
4. Continue guessing until you either find the secret number or run out of guesses.

## Features
- The game supports a customizable number of digits and letters in the secret number.
- Clues are provided in alphabetical order to prevent players from deducing the position of correct digits/letters based on clue order.

## Setup
To run the game, ensure you have Python installed on your machine. Navigate to the `src` directory and execute the following command:

```
python bagles.py
```

Enjoy playing Bagles!