# 100 days of code day 14 - Steven McNutt 2021

#import resources
import os
import logging
from random import randint
from art import logo, vs
from game_data import data

#set up logging
logger = logging.getLogger("Game")
logging.basicConfig(
  level = "INFO"
)

def clear_screen():
  # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


# TODO main game loop
def game():
  score = 0
  play_game = True

  while play_game:
    # Display logo
    print(logo)

    # display score if not first round
    if score > 0:
      print(f"You're right! Current score: {score}.")

    # pick two people at random
    # make sure we don't pick the same person twicee
    a = 0
    b = 0
    while a == b:
      data_range = len(data) - 1
      a = randint(0, data_range)
      b = randint(0, data_range)

    celeb_a = data[a]
    celeb_b = data[b]

    logger.debug(f"celeb a: {celeb_a}.  celeb_b: {celeb_b}")

    print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}.")
    
    print(vs+ "\n")
    
    print(f"Against B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}.")

    # ask the user which person has more followers
    # TODO handle the case where the user just presses enter (currently crashes game)
    
    choice = ""
    while choice != 'a' and choice != 'b':
       choice = input("Who has more followers?  Type 'a' or 'b': ")[0]
       
       if choice == "a":
         picked = celeb_a
       elif choice == "b":
         picked = celeb_b
       else:
         print("invalid choice. select 'a' or 'b', please.")
         
       logger.debug(f"user entered: {choice}.")
       

    
    # compare follower counts
    not_picked = [celeb_a, celeb_b]
    not_picked.remove(picked)
    not_picked = not_picked[0]

    logger.debug(f"picked = {picked}")
    logger.debug(f"not picked = {not_picked}")

    # if user is wrong: clear screen, display score, end game
    if int(picked["follower_count"]) < int(not_picked["follower_count"]):
      clear_screen()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      play_game = False
    

    # if user is correct, increment score, clear screen, go back to top of game loop.
    else:
      score += 1
      clear_screen()
     
    
    

    
    
    
    

clear_screen()
game()