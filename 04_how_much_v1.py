# Function goes here


# Main routine goes here

error = "Please enter a whole number between 1 and 10\n"

valid = False 
while not valid:
  try:
    #ask the question 
    response = int(input("How much money would you like to play for? "))

    #if the amount is too low / too high give
    if 0 < response  <= 10:
      print("You have asked to play with ${} ".format(response))

    #output an error
    else:
      print(error)
  
  #if there is an error, in this case strings or floats, this code will play
  except ValueError:
    print(error)