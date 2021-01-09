# 100 days of code day 8 - Steven McNutt 2021

from resources import logo, alphabet

print(logo)

#super awesome ceasar cipher function w00t!
def caesar(text="foo", shift=0, direction = "e"):
  transformed_text = ""
  cipher_direction = "encode"
  
  if direction[:1] == 'd':
      cipher_direction = "decode"
      shift *= -1
  
  for letter in text:
    if letter == " ":
      transformed_text += letter
    else:
      index = ((alphabet.index(letter)) + shift) % 26
      transformed_text += alphabet[index]

  print(f"The {cipher_direction}d text is: {transformed_text}")

# *** Game loop ***
play = ""

while play[:1] != "n":
  direction = input("Type '(e)ncode' to encrypt, type '(d)ecode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  
# prevent game from crashing on non-integer input
  try:
    shift = int(input("Type the shift number:\n"))
  except ValueError:
    print ("come on, dog, enter an integer\n")
  
# basic input validation and then call our function
  if text and (direction[0] in ['e', 'd']) :
    caesar(text, shift, direction)
  else:
      print("seems to be a problem")

  play = input("Run again? \n")
  print("\n")

print("end of line.")