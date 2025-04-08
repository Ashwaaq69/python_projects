# How It Works
# Running 100,000 simulations can take a while, which is why lines 95 and 96 report that another 10,000 simulations have finished. This feedback can assure the user that the program hasn’t frozen. Notice that some of the integers, like 10_000 on line 95 and 100_000 on lines 93 and 103, have underscores. These underscores have no special meaning, but Python allows them so that programmers can make integer values easier to read. In other words, it’s easier to read “one hundred thousand” from 100_000 than from 100000.


import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is set to 2001 so that the birthdays are all in the same year.
        # This makes it easier to compare dates.
        startOfYear = datetime.date(2002, 8, 19)
        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once
      in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None.
    #compare each birthdate to every other birthday
    for a, birthdayA in enumerate(birthdays):
          for b, birthdayB in enumerate(birthdays[a + 1 :]):
              if birthdayA == birthdayB:
                  return birthdayA  # Return the matching birthday.
#Display the intro:

print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
 40. 
 The birthday paradox shows us that in a group of N people, the odds
 that two of them have matching birthdays is surprisingly large.
 This program does a Monte Carlo simulation (that is, repeated random
 simulations) to explore this concept.
  
 (It's not actually a paradox, it's just a surprising result.)
  ''')

# Set up a tuple of month names in order:

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
         numBDays = int(response)
         break  # User has entered a valid amount.
print()

#Generate and display the birthdays:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
matchingBirthday = getMatch(birthdays)
#display the result
print('In this simulation, ', end='')
if matchingBirthday != None:
    monthName = MONTHS[matchingBirthday.month - 1]
    dateText = f'{monthName} {matchingBirthday.day}'
    print('multiple people have a birthday on', dateText)
else:
    print('everyone has different birthdays')
print()

#Run the simulation 100,000 times to see how often matching birthdays occur:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')    

print('Let\'s run another 100,000 simulations.')
siMatch = 0
for i in range(100_000):
    # Display the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, 'simulations finished...')
    # Create a list of random birthdays:
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        siMatch += 1 # Two birthdays match.
print('100,000 simulations run.') 
  
  
  # Display simulation results:
probability = round(siMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', siMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')     
