import random 
import pyperclip
sl=int(input('enter the password length: '))
x='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s='abcdefghijklmnopqrstuvwxyz'
t=123456789
w='!@#$%^&*'
p=x+s+str(t)+w

password = "".join (random.sample(p,sl))
pyperclip.copy(password)

print('your passowrd is ',password)
print("your password is copied to your clipboard")