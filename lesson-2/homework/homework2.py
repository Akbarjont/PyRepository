task 1
from datetime import datetime
Name = input('Please enter your name: ')
Year_of_birth = int(input('Please enter your year of birth: '))
age = (datetime.now().year - Year_of_birth)
print('The age of {} is {}'.format(Name, age))

task 2
txt = 'LMaasleitbtui'
txt[0::2], txt[1::2]

task 3 
txt = 'MsaatmiazD'
txt[0::2], txt[::-2]

task 4
txt = "I'am John. I am from London"
t1 = txt.split()
t1[5]

task 5 
UserString = input('Please enter your string: ')
ReverseString = UserString[::-1]
print(ReverseString)

task 6
sentence = input('Enter a string:')
vowels = 'A,a,E,e,I,i,O,o,U,u'
Count = 0
for harf in sentence:
    if harf in vowels:
        Count += 1 
if Count == 1: print('There is 1 vowel in the string: {}'.format(sentence))
if Count == 0: print('There is no vowel in the string: {}')
if Count > 1: print('There are {} vowels in the string: {}'.format(Count, sentence))

task 7 
import math
TheNumber = input('Please, type your number:')
print(max(TheNumber))

task 8 
TheWord = input('Please write a word to check if it is a palindrome')
RevWord = TheWord[::-1]
if RevWord == TheWord: print('Your word is a palindrome')
else: print('Your word is not a palindrome')

task 9 
TheEmail = input('Please type your email')
try:
    itvachcha = TheEmail.split('@')
    if len(itvachcha) != 2 or not itvachcha[1]:
        raise ValueError
    domainiz = itvachcha[1]
    print('Your domain is {}'.format(domainiz))
except:
    print('The email is invalid')

task 10 
import secrets
import string
password = secrets.token_hex(6)
characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}"
Generated = secrets.choice(characters)+password
print(Generated)
