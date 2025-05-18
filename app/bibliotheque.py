import json

def genererID(bibliotheque):
    if len(bibliotheque) == 0:
        return 1
    plusGrandID = 0
    for livre in bibliotheque:
        if livre["ID"] > plusGrandID:
            plusGrandID = livre["ID"]
    return plusGrandID + 1


def ajoutLivre(livre, fichier):
    with open(fichier, "r") as f:
        bibliotheque = json.load(f)

    livre["ID"] = genererID(bibliotheque)
    livre["Lu"] = False
    livre["Note"] = None
    livre["Commentaire"] = ""

    bibliotheque.append(livre)

    with open(fichier, "w") as f:
        json.dump(bibliotheque, f, indent=4)


def saisieLivre():
    titre = input("Saisir le titre : ")
    auteur = input("Saisir l'auteur : ")
    annee = int(input("Saisir l'année : "))

    livre = {
        "Titre": titre,
        "Auteur": auteur,
        "Annee": annee
    }
    return livre


def afficherLivres(fichier):
    with open(fichier, "r") as f:
        bibliotheque = json.load(f)

    if len(bibliotheque) == 0:
        print("Aucun livre enregistré ")
        return

    print("\nListe des livres enregistrés :\n")

    i = 1
    for livre in bibliotheque:
        print("Livre", i, ":")
        print("ID          :", livre["ID"])
        print("Titre       :", livre["Titre"])
        print("Auteur      :", livre["Auteur"])
        print("Année       :", livre["Annee"])
        print("Lu          :", "Oui" if livre["Lu"] else "Non")
        note = livre["Note"] if livre["Note"] is not None else "Aucune"
        print(" Note        :", note)
        commentaire = livre.get("Commentaire", "Aucun")
        print("Commentaire :", commentaire)
        print("\n")
        i += 1


def supprimerLivre(fichier):
    with open(fichier, "r") as f:
        bibliotheque = json.load(f)

    if len(bibliotheque) == 0:
        print("La bibliothèque est vide")
        return

    print("\nListe des livres :")
    i = 1
    for livre in bibliotheque:
        print(f"{i}. {livre['Titre']} - {livre['Auteur']} ({livre['Annee']})")
        i += 1

    identifiant = int(input("Entrez le numéro du livre à supprimer : "))

    livre = bibliotheque[identifiant - 1]
    confirmation = input("Voulez-vous vraiment supprimer '" + livre['Titre'] + "' ? (o/n) : ").lower()
    if confirmation == "o":
        del bibliotheque[identifiant - 1]
        with open(fichier, "w") as f:
            json.dump(bibliotheque, f, indent=4)
        print("Livre supprimé avec succés")
    else:
        print("Suppression annulée")


def rechercherLivre(fichier):
    with open(fichier, "r") as f:
        bibliotheque = json.load(f)
    mot_cle = input("Entrez un mot-clé titre ou auteur : ").lower()

    resultats = []
    for livre in bibliotheque:
        titre = livre["Titre"].lower()
        auteur = livre["Auteur"].lower()
        if mot_cle in titre or mot_cle in auteur:
            resultats.append(livre)

    if len(resultats) == 0:
        print("Aucun livre trouvé")
    else:
        print("\nRésultats trouvés :\n")
        i = 1
        for livre in resultats:
            print(str(i) + ". " + livre["Titre"] + " - " + livre["Auteur"] + " (" + str(livre["Annee"]) + ")")


def marquerCommeLu(fichier):
    with open(fichier, "r") as f:
        bibliotheque = json.load(f)

    if bibliotheque == []:
        print("La bibliotheque est vide")
        return

    print("\nListe des livres :")
    i = 1
    for livre in bibliotheque:
        lu = "Lu" if livre["Lu"] else "Non lu"
        print(str(i) + ". " + livre["Titre"] + " - " +
              livre["Auteur"] + " (" + str(livre["Annee"]) + ") - " + lu)
        i += 1

    identifiant = int(input("Entrez le numéro du livre à marquer comme lu : "))
    livre = bibliotheque[identifiant - 1]

    if livre["Lu"]:
        print("Ce livre est deja marqué comme lu.")
        return

    note = int(input("Entrez une note sur 10 : "))
    commentaire = input("Entrez un commentaire (optionnel) : ")

    livre["Lu"] = True
    livre["Note"] = note
    livre["Commentaire"] = commentaire

    with open(fichier, "w") as f:
        json.dump(bibliotheque, f, indent=4)

    print("Le livre a été marqué comme lu.")


def afficherParEtat(fichier):
    with open(fichier, "r") as f:
        bibliotheque = json.load(f)

    if bibliotheque == []:
        print("La bibliothéque est vide.")
        return

    print("\n1. Afficher les livres LUS")
    print("2. Afficher les livres NON LUS")
    choix = input("Votre choix : ")

    if choix == "1":
        livres = []
        for l in bibliotheque:
            if l["Lu"]==True:
                livres.append(l)
        titre_filtre = "Livres LUS"
    elif choix == "2":
        livres = []
        for l in bibliotheque:
            if l["Lu"] == False:
                livres.append(l)
        titre_filtre = "Livres NON LUS"
    else:
        print("Choix invalide.")
        return

    if livres == []:
        print(titre_filtre + " : Aucun livre trouvé")
        return

    print("\n" + titre_filtre + " :\n")
    i = 1
    for livre in livres:
        print("Livre " + str(i) + " :")
        print("Titre       : " + livre["Titre"])
        print("Auteur      : " + livre["Auteur"])
        print("Année       : " + str(livre["Annee"]))
        if livre["Note"] != None:
            print("Note        : " + str(livre["Note"]))
        else:
            print("Note        : Aucune")
        if "Commentaire" in livre:
            print("Commentaire : " + livre["Commentaire"])
        else:
            print("Commentaire : Aucun")
        i += 1


def trierLivres(fichier):
    with open(fichier, "r") as f:
        bibliotheque = json.load(f)

    if bibliotheque == []:
        print("La bibliothèque est vide.")
        return

    print("\n=== Trier les livres ===")
    print("1. Par année")
    print("2. Par auteur (ordre alphabétique)")
    print("3. Par note décroissante")
    choix = input("Votre choix : ")

    if choix == "1":
        for i in range(len(bibliotheque)):
            for j in range(i + 1, len(bibliotheque)):
                if bibliotheque[i]["Annee"] > bibliotheque[j]["Annee"]:
                    bibliotheque[i], bibliotheque[j] = bibliotheque[j], bibliotheque[i]
        critere = "année"

    elif choix == "2":
        for i in range(len(bibliotheque)):
            for j in range(i + 1, len(bibliotheque)):
                if bibliotheque[i]["Auteur"].lower() > bibliotheque[j]["Auteur"].lower():
                    bibliotheque[i], bibliotheque[j] = bibliotheque[j], bibliotheque[i]
        critere = "auteur"

    elif choix == "3":
        for i in range(len(bibliotheque)):
            for j in range(i + 1, len(bibliotheque)):
                if bibliotheque[i]["Note"] is not None:
                    note_i = bibliotheque[i]["Note"]
                else:
                    note_i = -1

                if bibliotheque[j]["Note"] is not None:
                    note_j = bibliotheque[j]["Note"]
                else:
                    note_j = -1

                if note_i < note_j:
                    temp = bibliotheque[i]
                    bibliotheque[i] = bibliotheque[j]
                    bibliotheque[j] = temp
        critere = "note"

    else:
        print("Choix invalide.")
        return

    print("\nLivres triés par " + critere + " :\n")
    i = 1
    for livre in bibliotheque:
        print("Livre " + str(i) + " :")
        print("Titre : " + livre["Titre"])
        print("Auteur : " + livre["Auteur"])
        print("Année : " + str(livre["Annee"]))
        if livre["Note"] is not None:
            print("  Note : " + str(livre["Note"]))
        else:
            print("Note : Aucune")
        print("Lu : " + ("Oui" if livre["Lu"] else "Non"))
        i += 1
