from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations_dictionary = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number: "))
  for each_key in operations_dictionary:
    print(each_key)

  is_done = False

  while not is_done:
    math_operation = input("Which mathematical operation from the list above would you like to use?\nEnter your choice here: ")
    num2 = float(input("What's the second number: "))
    math_function = operations_dictionary[math_operation]
    first_answer = math_function(num1, num2)

    print(f"{num1} {math_operation} {num2} = {first_answer}")

    user_answer = input(f"Would you like to continue using {first_answer} type 'y' for yes or 'n' for no. If you would like to restart the calculator type 'r'.\n")

    if user_answer == "y":
      is_done = False
      num1 = first_answer
    elif user_answer == "n":
      is_done = True
    elif user_answer == "r":
      is_done = True
      calculator()
    else:
      print("That answer is not valid.")
      is_done = True

calculator()