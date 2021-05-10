import random

# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play... ").lower()
while play_again == "":

  # increase no. of rounds played
  rounds_played += 1

  # print round number
  print()
  print("*** Round #{} ***".format(rounds_played))

  chosen_num = random.randint(1,100)

  # Adjust balance 
  # if the random no. is between 1 and 5, user gets a unicorn (add $4 to the balance)
  if 1 <= chosen_num <= 5:
    chosen = "unicorn"
    balance += 4 

  # if the random no. is between 6 and 36, user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    balance -= 1
  
  
  # the token is either a horse or a zebra, in either case subtract $0.50 from balance
  else:
    # if the number is even, set the chosen item to a horse
    if chosen_num % 2 == 0:
      chosen = "horse"
    
    # otherwise set it to a zebra
    else:
      chosen = "zebra"
    balance -= 0.5
  
  print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

  if balance < 1:
    play_again = "xxx"
    print("Sorry you have run out of money")
  else: 
    play_again = input("Press Enter to play again or 'xxx' to quit ")


print()
print("Final Balance", balance)
print("Thanks for playing")