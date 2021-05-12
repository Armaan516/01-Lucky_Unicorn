# functions go here
def statement_generator(statement, decoration):
  # stars that go at sides of statement
  sides = decoration * 3
  
  # putting the statement and stars in one line
  statement = "{} {} {}".format(sides, statement, sides)

  # stars that go at the top and bottom of statement
  top_bottom = decoration * len(statement)

  # putting the top/bottom 
  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""


# main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()
statement_generator("Congratulations you got a Unicorn", "!")

