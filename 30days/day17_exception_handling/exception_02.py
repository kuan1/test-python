from datetime import datetime

try:
  name = input('Enter your name: ')
  year_born = input('Year you were born: ')
  age = datetime.now().year - int(year_born)
  print(f'You are {name}. And your age is {age}')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
    print('I usually run with the try block')
except Exception as e:
  print('Something is went wrong', e)