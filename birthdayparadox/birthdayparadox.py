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

