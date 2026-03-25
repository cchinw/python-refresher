# -- Exercise 1 --

my_children = ["Chidera", "Imole", "Layo", "Chance"]

for child in my_children:
  if child == "Chidera":
    print("My beating heart" + " " +child)
  elif child == "Imole":
    print("My bright light" + " " + child)
  elif child == "Layo":
    print("My joy bringer" + " " + child)
  else:    print("My bundle of joy" + " " + child)

# -- Exercise 2 --

for i in range(1, 11):
  print(i)

for i in range(1, 11):
  if i%2 == 0:
    print(i)

# -- Exercise 3 --

salaries = [115000,200000,280000,393000,550000]

for salary in salaries: 
  if salary >= 400000:
    print("You can comfortably afford a $2.5M+ home. This is your primary target")
  elif salary >= 280000:
    print("You can comfortably afford a $1.8M home")
  elif salary >= 200000:
    print("You can afford a $1.2M home")
  else:
    print("Keep building. The offer is coming")