# Function goes here
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
how_much = num_check("How much money would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
