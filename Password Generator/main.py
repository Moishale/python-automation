import random
import string

numbers = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
special_chars = "!@#$%^&*()_-[]"

upper, lower,  nums, symbols = True, True, True, False

all = ""

if upper == True:
    all += uppercase_letters
if lower == True:
    all += lowercase_letters
if nums == True:
    all += numbers
if symbols == True:
    all += special_chars


amount = 3
length = 20

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
