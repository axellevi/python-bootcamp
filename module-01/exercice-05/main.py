firstName = input("Prénom: ")
product = input("Produit: ")
unitPrice = float(input("Prix unitaire: "))
amount = float(input("Quantité: "))
total = unitPrice * amount

print(f"Bonjour {firstName} !\n\n"
      f"Récapitulatif de votre achat :\n"
      f"- Produit : {product}\n"
      f"- Quantité : {amount}\n"
      f"- Prix unitaire : {unitPrice}\n"
      f"- Total : {total:.2f}$")