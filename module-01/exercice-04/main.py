first_name = input("Prénom: ")
celsuis = float(input("Température: "))

fahrenheit = float((celsuis * 9 / 5) + 32)

print(f"Bonjour {first_name}!\n\n"
      f"{celsuis} °C correspondent à {fahrenheit} °F.")