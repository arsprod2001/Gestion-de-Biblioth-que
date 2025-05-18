from app.bibliotheque import *

fichier = "data/gestion.json"

while True:
    print("\n=== MENU BIBLIOTHÈQUE ===")
    print("1. Ajouter un livre")
    print("2. Afficher tous les livres")
    print("3. Supprimer un livre")
    print("4. Rechercher un livre")
    print("5. Marquer un livre comme lu")
    print("6. Afficher par état (lus / non lus)")
    print("7. Trier les livres")
    print("8. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        livre = saisieLivre()
        ajoutLivre(livre, fichier)
    elif choix == "2":
        afficherLivres(fichier)
    elif choix == "3":
        supprimerLivre(fichier)
    elif choix == "4":
        rechercherLivre(fichier)
    elif choix == "5":
        marquerCommeLu(fichier)
    elif choix == "6":
        afficherParEtat(fichier)
    elif choix == "7":
        trierLivres(fichier)
    elif choix == "8":
        print("Fin du programme")
        break
    else:
        print("Choix invalide")
