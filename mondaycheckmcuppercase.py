# mondaycheckmcuppercase.py

schedule = input('Enter schedule here:')

Monday = 'Monday'

if Monday.find(schedule) != -1:
    print('Monday is present.')

else:
    print('Monday is not present.')

x = schedule.upper()

print('')

print('Your schedule in uppercase:')

print(x)
