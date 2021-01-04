#Password Generator Project - Day 5 hundred days of Code. Steven McNutt 2020
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def list_picker(list, num_items):
  list_length = len(list)
  picked_items = ""
  
  #randomly select items from list and build string
  for letter in range(num_items + 1):
    selector = random.randint(1, list_length) - 1
    picked_items += list[selector]
  
  return picked_items

def shuffle_string(string):
  shuffled_string = ""
  my_list = list(string)
  random.shuffle(my_list)

  for item in my_list:
    shuffled_string += item
  
  return shuffled_string
  
letter_list = list_picker(letters, nr_letters)
number_list = list_picker(numbers, nr_numbers)
symbol_list = list_picker(symbols, nr_symbols)
unshuffled_string = letter_list + number_list + symbol_list
generated_password = shuffle_string(unshuffled_string)

print(f"Your password is: {generated_password}")
