# # --- Exercise 1 ---

# children = ["Chidera", "Imole", "Layo", "Chance"]

# def greet_child(name, age):
#   if name == "Chidera":
#     return f"My beating heart {name}, you are {age} years old"
#   elif name == "Imole":
#     return f"My bright light {name}, you are {age} years old"
#   elif name == "Layo":
#     return f"My joy bringer {name}, you are {age} years old"
#   else:
#     return f"My bundle of joy {name}, you are {age} years old"

# print(greet_child(children[0], 3))
# print(greet_child("Imole", 2))
# print(greet_child("Layo", 1))
# print(greet_child("Chance", 0))

# # --- Exercise 2 ---

salaries = [115000,200000, 205,000, 210000, 220000, 250000, 280000,393000,550000]

# def check_salary(salary):
#   if salary >= 550000:
#     return f"Your salary of ${salary:,} is for Anthropic band."
#   elif salary >= 393000:
#     return f"Your salary of ${salary:,} is for Netflix band."
#   elif salary >= 280000:
#     return f"Your salary of ${salary:,} is for Google band."
#   elif salary >= 200000:
#     return f"Your salary of ${salary:,} is for Microsoft band."
#   else:
#     return f"Your salary of ${salary:,} is grossly under market and needs improvement."

# for salary in salaries:
#   print(check_salary(salary))

# --- Exercise 3 ---

home_price = 1499950
down_payment = 0.20 * home_price
interest_rate = 6.8
years = 30

def mortgage_payment(home_price, down_payment, interest_rate, years):

  monthly_rate = interest_rate/100/12
  months = years * 12
  loan = home_price - down_payment

  payment = loan * (monthly_rate * (1 + monthly_rate) ** months) / ((1+ monthly_rate) ** months -1)
    
  return round(payment, 2)

payment = mortgage_payment(home_price, down_payment, interest_rate, years)

for salary in salaries:
  monthly_income = salary/12
  if payment > monthly_income * 0.43:
    print(f"With a salary of ${salary:,}, the monthly mortgage payment of ${payment:,} is not affordable.")
  else:
    print(f"With a salary of ${salary:,}, the monthly income of ${monthly_income:,.2f} can cover the mortgage payment of ${payment:,}.")

