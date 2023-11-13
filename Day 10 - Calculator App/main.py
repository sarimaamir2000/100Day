import art
print(art.logo)


#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2

#Divide
def divide(n1,n2):
  return n1 / n2

#Create a dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = float(input("What's the first number?: "))
  go_again = "y"

  for operator in operations:
    print(operator)
  
  while go_again == "y":
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
    function = operations[operation_symbol]
    answer = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    go_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if go_again == 'y':
      num1 = answer
    else:
      calculator()

calculator()