# Ask the user if they have played before
show_instructions = ""
while show_instructions != "xxx":

  show_instructions = input("Have you played this game before?").lower()

  # If they say yes, output 'program continues'
  if show_instructions == "yes" :
    print("Program continues")
  
  elif show_instructions == "y":
    print("Program continues")

  # If they say no, output 'display instructions'
  elif show_instructions == "no":
    print("Display instructions")

  elif show_instructions == "n":
    print("Display instructions")

  # If response is anything else, output 'error'
  else: 
    print("Please answer yes / no")

  print("You chose {}".format(show_instructions))