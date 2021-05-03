# Ask the user if they have played before
show_instructions = input("Have you played this game before?").lower()

# If they say yes, output 'program continues'
if show_instructions == "yes" :
  print("Program continues")

# If they say no, output 'display instructions'
elif show_instructions == "no":
  print("Display instructions")

# If response is anything else, output 'error'
else: 
  print("Please answer yes / no")

for letter in show_instructions:
  print(letter)