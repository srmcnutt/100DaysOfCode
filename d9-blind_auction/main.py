from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bidders = {}
choice = ""

while choice != 'n':
  name = input("what is your name?\n")
  price = int(input("place a bid in whole numbers please:\n"))
  
  #TODO add name and price to dict
  bidders[name] = price
  
  choice = input("any other bidders? (y/n)\n")

  clear()

high_bid = 0
winner = ""
for bidder in bidders:
  if bidders[bidder] > high_bid:
    high_bid = bidders[bidder]
    winner = bidder
    

print(f"the winner is {winner} with a bid of {high_bid}.")