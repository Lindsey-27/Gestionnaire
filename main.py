#from GESTION_PRODUIT.categorie_type import ajoutProd
from categorie_type import ajoutProd, affichProd, deleteProd, updateProd

while True:
    print("\n--- MENU ---")
    print("1. Ajouter un produit")
    print("2. Afficher les produits")
    print("3. Modifier un produit")
    print("4. Supprimer un produit")
    print("5. Quitter")
    choix = input("Choix: ")

    if choix == '1':
        ajoutProd()
    if choix == '2':
        affichProd()
    if choix == '3':
        updateProd()
    if choix == '4':
        deleteProd()
    elif choix == '5':
        break



