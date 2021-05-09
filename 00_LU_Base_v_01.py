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

def num_check(question, low, high):
  error = "Please enter a whole number between 1 and 10\n"

  valid = False 
  while not valid:
    try:
      #ask the question 
      response = int(input(question))

      # valid response
      if low < response  <= high:
        return response

      # if the amount is too low / too high output an error
      else:
        print(error)
    
    #if there is an error, in this case strings or floats, this code will play
    except ValueError:
      print(error)


# Main routine goes here
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
  instructions()

print("Program continues")

# Ask user how much they want to play with... 
how_much = num_check("How much money would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))