customer_name = input("Client : ")
initial_price = float(input("Prix : "))
discount_percent = int(input("Remise : "))
discount_amount = initial_price * discount_percent / 100
final_price = initial_price - discount_amount
amount_saved = initial_price - final_price

print(f"-------- FACTURE --------\n\n"
      f"Client : {customer_name}\n\n"
      f"Prix initial : {initial_price:.2f}$\n"
      f"Remise : {discount_percent} %\n"
      f"Montant de la remise : {discount_amount: .2f}$\n"
      f"Prix final : {final_price: .2f}$\n"
      f"Vous avez économisé : {discount_amount: .2f}$")

# cas tester :
# Prix	Remise	Résultat attendu
# 100	10	90.00
# 250	15	212.50
# 99.99	20	79.99
# 50	0	50.00