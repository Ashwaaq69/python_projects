import sys

bitmap = """
  ***  
 *   * 
*     *
*     *
 *   * 
  ***  
"""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap')

message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        # If the character is a space, print a space:
        if bit == ' ':
            print(' ', end='')
        # Otherwise, print the message character:
        else:
            print(message[i % len(message)], end='')
    # Print a new line at the end of each line:
    print()