import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91

# char = ''.join(random.choices(letters, k=nr_letters))
# sym = ''.join(random.choices(symbols, k=nr_symbols))
# num = ''.join(random.choices(numbers, k=nr_numbers))
#
# passwd = char + sym + num
#
# print(f"Your password is: {passwd}")
#
# # Hard Level - Order of characters randomised:
# # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# char = ''.join(random.choices(letters, k=nr_letters))
# sym = ''.join(random.choices(symbols, k=nr_symbols))
# num = ''.join(random.choices(numbers, k=nr_numbers))
#
# passwd = char + sym + num
# passwd_list = list(passwd)
# random.shuffle(passwd_list)
# shuffled_passwd = ''.join(passwd_list)
#
# print(f"Your password is: {shuffled_passwd}")


password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
password = list(password)
random.shuffle(password)
# password = ''.join(password)
new_pass = ""
for i in password:
    new_pass += i
print(f"Your password is: {new_pass}")
