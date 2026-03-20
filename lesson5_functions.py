# --- Exercise 1 ---

children = ["Chidera", "Imole", "Layo", "Chance"]

def greet_child(name, age):
  if name == "Chidera":
    return f"My beating heart {name}, you are {age} years old"
  elif name == "Imole":
    return f"My bright light {name}, you are {age} years old"
  elif name == "Layo":
    return f"My joy bringer {name}, you are {age} years old"
  else:
    return f"My bundle of joy {name}, you are {age} years old"

print(greet_child(children[0], 3))
print(greet_child("Imole", 2))
print(greet_child("Layo", 1))
print(greet_child("Chance", 0))

# # --- Exercise 2 ---

# salaries = [115000,200000,280000,393000,550000]

# def check_salary(salary):
