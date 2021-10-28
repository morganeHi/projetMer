import csv  # importation de la librairie csv

# on propose un choix entre matériel et le nom de l'espece
choix = input("Souhaitez-vous choisir par matériel ou par nom ? \n")

# premiere condition si tu choisis par matériel
if choix == "matériel":
    # on imprime les différents matériel possible et on recupère son choix de matériel
    print("matériel disponible : couteau, pince, crochet, griffe, râteau, sel, gratoir, épuisette, haveneau, pelle, croc, burin, pique, couteau à palourde, aucun : ")

    materiel = input("quel matériel possédez-vous : ").strip().upper()

    # ouverture du fichier csv qui stocke nos données
    file = open("BDD-projet-mer.csv", "r")
    reader = csv.DictReader(file)
    # en fonction du choix de matériel, on imprime l'espèces, methode, comestible, reglementation en fonction de son choix
    for row in reader:
        if row["materiel"].strip().upper() == materiel or row["materiel2"].strip().upper() == materiel or row["materiel3"].strip().upper() == materiel or row["materiel4"].strip().upper() == materiel:
            print("Vous pouvez pêcher l'espèce suivante:", row["nom"])
            print("Quelques indications pour la pêcher :", row["methode de peche"])
            print("L'espèce est comestible :", row["comestible"])
            print("La taille minimale et la réglementation sont :", row["reglementation"])

# deuxieme condition si on choisit par le nom de l'espèce
if choix == "nom":
    # ouverture du fichier
    with open("BDD-projet-mer.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row["nom"])
    # on recupère le nom de l'espèce voulu et on l'assigne a la variable nom
    nom = input("nom : ").strip().upper()
    with open("BDD-projet-mer.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # si la varibale nom correspond a cette ligne dans la colonne nom alors on imprime la methode, le materiel, si c'est comestible et la reglementation
            if row["nom"].strip().upper() == nom:
                print("Voici quelques informations qui pourront vous aider pour votre pêche:", row["methode de peche"],)
                print("Vous pourrez utiliser comme matériel:", row["materiel"],
                      row["materiel2"], row["materiel3"], row["materiel4"])
                print("cette espece est-elle comestible :", row["comestible"])
                print("Quelques règles à respecter concernant cette espèce(au minimum", row["reglementation"])