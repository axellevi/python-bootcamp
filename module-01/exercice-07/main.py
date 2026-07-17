first_name = input("Prénom : ")
weight = float(input("Poids : "))
height = float(input("Taille : "))
bmi = weight / (height ** 2)

print(f"------ IMC ------\n\n"
      f"Bonjour {first_name}!\n"
      f"Poids {weight} kg\n"
      f"Taille: {height} m\n\n"
      f"Votre IMC est de {bmi:.2f}")
