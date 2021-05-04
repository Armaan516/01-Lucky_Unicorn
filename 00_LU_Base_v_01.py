# Function goes here
def yes_no(question):
  valid = False
  while not valid: 
    response = input(question).lower()

    # If they say yes, output 'program continues'
    if response == "yes" or response == "y":
      response == "yes"
      return response

    # If they say no, output 'display instructions'
    elif response == "no" or response == "n":
      response == "no"
      return response

    # If response is anything else, output 'error'
    else: 
      print("Please answer yes / no")

def instructions():
  print("**** How to Play ****")
  print()
  print("The rules of the game go here")
  print()
  return ""

# Main routine goes here
played_before = yes_no("Have you played the game before?")


if played_before == "no":
  instructions()

print("Program continues")