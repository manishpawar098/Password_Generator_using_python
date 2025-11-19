'''
PASSWORD GENERATOR 

'''

import random
char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%^&*_-/\|~"
length = int(input("Enter the length of password : "))
password = ""

for i in range(length):
    password+=random.choice(char)
print(password)