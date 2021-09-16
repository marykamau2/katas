def years():
      years = int(input('How old are you? \n'))

if years > 0:
    years_in_days = years * 365
    print(f'You are { years_in_days } days old.')
else:
    print('Please input a valid age above 0')