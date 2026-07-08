first_name = input("Prénom: ")
hours_worked = float(input("Heures travaillées: "))
hourly_rate = float(input("Salaire horraire: "))

gross_salary = hours_worked * hourly_rate

print(f"Bonjour {first_name}!\n"
      f"Tu as travaillé {hours_worked}.\n"
      f"Ton salaire brute est  {gross_salary: .2f} £.")