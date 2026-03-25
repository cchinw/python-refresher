# Lesson 3 - Making decisions with if/elif/else
# Chinwendu Ukoha - Python Refresher

# ---Exercise 1: Am I an adult?---
age = 35

if age >= 18:
  print("Adult")
else:
  print("Minor")

# ---Exercise 2: Restaurant Rewards---
order_total = 75

if order_total > 100:
  print("VIP order! Free drink + 10% off")
elif order_total > 50:
  print("Thanks! Here's a free dessert")
elif order_total > 25:
  print("Thanks for your order!")
else:
  print("Every order matters. Thank you!")

#---Exercise 3: House affordability ---
annual_salary = 500000

if annual_salary >+ 400000:
  print("You can comfortably afford a $2.5M+ home")
elif annual_salary >= 280000:
  print("You can comfortably afford a $1.8M home - Google/Netflix territory")
elif annual_salary >= 200000:
  print("You can afford a $1.2M home - this is your current target")
else:
  print("Keep building. The offer is coming")
  