customer_name = input("Nom du client : ")
product_name = input("Produit : ")
unit_price = float(input("Prix Unitaire : "))
quantity = int(input("Quantité: "))
subtotal = unit_price * quantity
vat = subtotal * 0.2
total = subtotal + vat

print(f"----------- FACTURE -----------\n\n"
      f"Client : {customer_name}\n"
      f"Produit : {product_name}\n\n"
      f"Quantité : {quantity}\n"
      f"Prix Unitaire : {unit_price:.2f}$\n\n"
      f"Sous total : {subtotal:.2f}$\n"
      f"TVA(20%) : {vat:.2f}$\n"
      f"Total TTC : {total:.2f}$\n\n"
      f"Merci pour votre achat !")