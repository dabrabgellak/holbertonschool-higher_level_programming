#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absnumber = abs(number) % 10
if number % 10 < 6 and number % 10 != 0:
    print('Last digit of {:d}'.format(number),
          'is {:d} is less than 6 and not 0'.format(absnumber * -1))
elif number % 10 > 5:
    print('Last diigt of {:d}'.format(number),
          'is {:d} and is greater than 5'.format(absnumber))
elif number % 10 == 0:
    print('Last digit of {:d}'.format(number),
          'is {:d} and is 0'.format(absnumber))
