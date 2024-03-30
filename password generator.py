# Program that generates password
import random
import string

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '!@#$%^&*+_-``~?'
all_char = lower + upper + numbers + symbols
length = 9

password_list = random.sample(all_char, length)  # Sample randomly without replacement
password = ''.join(password_list)  # Join the sampled characters into a string

print(f'Generated password is {password}')


