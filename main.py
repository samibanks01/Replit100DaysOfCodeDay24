print("Infinity Dice 🎲")

print()

def rollDice(sides):
  import random
  while True:
    roll = random.randint(1, sides)
    print("You rolled", roll)
    print()
    again = input("Roll again? ")
    if again == "yes":
      continue
    else:
      break

sides = int(input("How many sides? "))
rollDice(sides)
