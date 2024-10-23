quantity = float(input("donne la quantite : "))
unite = input("donne l'unite (kg / pounds ): ")
if unite == "kg" :
    print(f"the quantity you put equal in pound {quantity * 2.2}pound")
else:
    print(f"the quantity you put equal in kg {quantity / 2.2}kg")