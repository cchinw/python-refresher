# --- Exercise 1 ---

children = ["Chidera", "Imole", "Layo", "Chance"]

def greet_child(name, age):
  if name == "Chidera":
    return "My beating heart" + " " + name + ", you are " + str(age) + " years old"
  elif name == "Imole":
    return "My bright light" + " " + name + ", you are " + str(age) + " years old"
  elif name == "Layo":
    return "My joy bringer" + " " + name + ", you are " + str(age) + " years old"
  else:
    return "My bundle of joy" + " " + name + ", you are " + str(age) + " years old"
  
print(greet_child(children[0], 3))
print(greet_child("Imole", 2))
print(greet_child("Layo", 1))
print(greet_child("Chance", 0))