
#100daysofcode day 10: calculator. 2021 Steven McNutt
#calling dictionaries from functions
#recursion

def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def mult(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div
}

def calculator():
  print("\n******** Calculator ********\n\n")
  num1 = float(input("what is the first number?: "))
  num2 = float(input("what is the second number?: "))
  
  for symbol in operations:
    print(symbol)
  
  operation_symbol = input("\npick an operation from the list above: ")
  
  if operation_symbol in operations:
    result1 = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result1}\n")
  
  else:
    print("invalid input")
  
  run_program = True
  
  while run_program:
    choice = input(f"Type 'y' to continue calculating with {result1}, 'n' to exit: ")
    
    if choice == 'n':
      run_program = False
      calculator()
    
    else:
      for symbol in operations:
        print(symbol)
  
      operation_symbol = input("pick another operation: ")
      num3 = float(input("What's the next number?: "))
      
      if operation_symbol in operations:
        result2 = operations[operation_symbol](result1, num3)
        print(f"{result1} {operation_symbol} {num3} = {result2}")
      
      else:
        print("invalid input")
    
calculator()