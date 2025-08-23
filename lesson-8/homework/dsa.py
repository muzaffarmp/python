
# Exception Handling Exercises
# 1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def calc(n):
  try:
    return 1/n
  except ZeroDivisionError:
    return 'Noldan boshqa son kirit!'
print(calc(2))

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer
def calc(n):
  try:
    return 1/int(n)
  except ValueError:
    return 'Raqam kirit!'

print(calc(input('Son kiriting '))) 

# 3 Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def calc(n):
  try:
    with open(n,'r') as f:
        return f.read()
  except FileNotFoundError:
    return 'Fayl topilmadi!'
print(calc(input('Fayl nomi va joylashgan joyini kiriting ')))  

# 4 Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def calc(w1,w2):
  try:
      for i in (w1,w2):
          if i not in ('0123456789'):
              1+i
      else:
          print('ok')
  except TypeError:
    return 'Raqam kiritilmagan!'
w1=input('Raqam kirit ')
w2=input('Yana raqam kirit ')
print(calc(w1,w2)) 

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
def calc(tx):
  try:
      with open (tx,'w') as f:
          f.write('tttaaaa')
      return 'OK'
  except PermissionError:
    return 'Fayl ochiq!'
print(calc(input('Faylni ko`rsat '))) 

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def calc(t):
    try:
        a=[1,2,3,4]
        return a[t]
    except IndexError:
        return 'Noto`g`ri raqam!'
print(calc(int(input('Raqam kirit '))))  

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    a=input('Raqam kirit! ')
    print(a)
except KeyboardInterrupt:
    print('Toxtatma')

# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    10/0
except ArithmeticError:
    print('Xato')
# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
