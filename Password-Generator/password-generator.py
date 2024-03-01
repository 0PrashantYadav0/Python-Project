import random
import string

def generate_password(min_Length, numbers = True, special_characters=True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation
  
  characters = letters
  if numbers:
    characters += digits
  if special_characters:
    characters += special

  pwd = ""
  check = False
  has_number = False
  has_special = False

  while not check or len(pwd) < min_Length:
    new_char = random.choice(characters)
    pwd += new_char

    if new_char in digits:
      has_number = True
    if new_char in special:
      has_special = True

    check = True
    if numbers:
      check = has_number
    if special_characters:
      check = check and has_special

  return pwd


num = int(input("Enter the length of password : "))
has_number = input("Do you want to have numbers. (y/n) : ").lower() == "y"
has_special = input("Do you want to have special characters. (y/n) : ").lower() == "y"

pwd = generate_password(num, has_number, has_special)
print(pwd)
