customer_name = input("Client : ")
initial_price = float(input("Prix : "))
quantity = int(input("Quantité : "))
discount_percent = int(input("Remise : "))

discount_amount = initial_price * discount_percent / 100
final_price = initial_price - discount_amount
more_than = initial_price >= 100
discount = discount_amount == 0
has_changed = final_price != initial_price
print(f"-------- ANALYSE --------\n\n"
      f"Client : {customer_name}\n\n"
      f"Prix final : {final_price:.2f}$\n\n"
      f"plus de 5 articles ? {more_than}\n"
      f"Aucune remise ? {discount}\n"
      f"Le prix a changé ? {has_changed}")

# Cas testés : 
# Teste au minimum :

# Prix	Quantité	Remise
# 150	8	      10
# 50	2	      0
# 100	5	      20
# 99.99	6	      0