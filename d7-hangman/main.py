from art import stages
from word_list import word_list

import logging
logging.basicConfig(
  level = "WARNING"
)
#Step 1 


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random
chosen_word = random.choice(word_list)

hint_list = []
for letter in chosen_word:
  hint_list += '_'

logging.info(f'chosen_word is: {chosen_word}')
logging.info(f'hint list is: {hint_list}')

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = ""
lives = 6

#Introduction
print(
  "welcome to hangman. You have 6 lives to complete the word. Good luck!\n"
  )

# initialize game loop and set conditions
while "_" in hint_list and lives > 0:
  
  index = 0 
  hint_string = ""
  for letter in hint_list:
    hint_string += hint_list[index] + " "
    index += 1
  
  print(f"{hint_string}\n")
  
  # make sure we have a single character input
  while len(guess) != 1:
    guess = input("guess a letter\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

  index = 0
  for letter in chosen_word:
    if letter == guess:
      hint_list[index] = chosen_word[index]
    index += 1

  if guess in chosen_word:
    print("good job!\n")
  
  else:
    print("lost a life, try again.\n")
    lives -= 1
    logging.info(f"lives remaining: {lives}")
  
  
  # reset guess field before rerunning loop
  guess = ""

  # print stages
  print(f"{stages[lives]}\n")

# figure out if we've won or lost after exiting game loop.
if lives > 0:
  print(f"The word is {chosen_word}\n")
  print("******** You won!  great job ********")
else:
  print ("you lose.  Game over.")
  
