
# 100 days of code day 11 - Blackjack

import random
import logging
logging.basicConfig(
  level = "DEBUG"
)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  card = ""
  card = random.choice(cards)
  logging.debug(f"dealt a {card}")

  return card

def calculate_score(hand):
  score = 0
  
  # return 0 if blackjack
  if len(hand) == 2 and sum(hand) == 21:
    return 0
  # replace 11 with a 1 if ace puts us over 21
  if 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
  
  score = sum(hand)

  return score

def compare_scores(user_score, computer_score):
  if user_score == computer_score and user_score < 21:
    return "Tie game!"
  elif computer_score == 0:
    return "Computer had blackjack. computer wins!"
  elif user_score == 0:
    return "User had blackjack.  User wins!"
  elif user_score > 21:
    return "User went over 21.  Computer wins!"
  elif computer_score > 21:
    return "Computer went over 21.  User wins!"
  elif user_score > computer_score:
    return "User wins!"
  elif computer_score > user_score:
    return "Computer wins!"
  else:
    return "no condition match; there's a bug"


def blackjack():
  user_cards = []
  computer_cards = []
  inital_hand = 2
  
  #deal inital hand 
  for count in range(inital_hand):
    card = deal_card()
    user_cards.append(card)
  
  for count in range(inital_hand):
    card = deal_card()
    computer_cards.append(card)
  
  logging.debug(f"initial hands:  user: {user_cards}. computer:   {computer_cards}.")
  
  # calculate scores
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  
  logging.debug(f"initial scores: Computer: {computer_score}. User: {user_score}.")
  
  game_continue = True
  # main game loop
  while game_continue:
    if user_score == 0 or computer_score == 0:
      game_continue = False
    
    deal_continue = True
    while user_score < 22 and deal_continue: 
      choice = ""
      choice = input("Do you want to draw another card? Type 'y' or 'n':")
      if choice == "y":
        card = deal_card()
        user_cards.append(card)
        user_score = calculate_score(user_cards)
      
      elif choice == "n":
        deal_continue = False
      
      elif user_score > 21:
        game_continue == False
        
      logging.debug(f"user score is: {user_score}.")
  
    while computer_score < 17:
      card = deal_card()
      computer_cards.append(card)
      computer_score = calculate_score(computer_cards)
  
      logging.debug(f"computer score is: {computer_score}.")
  
    if computer_score >= 17:
      game_continue = False
  
  
  logging.debug("exited main loop")
  
  winner = compare_scores(user_score, computer_score)
  print(f"user: {user_score}. Computer: {computer_score}. {winner}\n")

  choice = input("would you like to play again? (y/n) ")
  if choice == 'y':
    blackjack()

blackjack()
  



