import random 
import pyperclip

length=int(input('enter the password length: '))
upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case='abcdefghijklmnopqrstuvwxyz'
number=123456789
special_characters='!@#$%^&*'
con=upper_case+lower_case+str(number)+special_characters

password = "".join (random.sample(con,length))
pyperclip.copy(password)

print('your passowrd is ',password)
print("your password is copied to your clipboard")
