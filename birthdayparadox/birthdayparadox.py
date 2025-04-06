# How It Works
# Running 100,000 simulations can take a while, which is why lines 95 and 96 report that another 10,000 simulations have finished. This feedback can assure the user that the program hasn’t frozen. Notice that some of the integers, like 10_000 on line 95 and 100_000 on lines 93 and 103, have underscores. These underscores have no special meaning, but Python allows them so that programmers can make integer values easier to read. In other words, it’s easier to read “one hundred thousand” from 100_000 than from 100000.


import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is set to 2001 so that the birthdays are all in the same year.
        # This makes it easier to compare dates.
        startOfYear = datetime.date(2001, 1, 1)
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
