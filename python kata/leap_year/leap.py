year = int(input('Please put in your year?'))

def leap(year):
  if (year % 4) == 0 and (year % 100) == 0 and (year % 400) == 0:
    # year = True
    return True
    print(f'{year} entered is a leap year')
  else:
    # year = False
    return False
    print(f'{year} entered is not a leap year')

year2 = leap(year)

print(year2)