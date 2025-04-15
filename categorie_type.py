from datetime import datetime
from GESTION_PRODUIT.saisieUtilisateur import saisi_produit
from GESTION_PRODUIT.generer import date_enregistrement, matricule_auto


TAILLE_MAX_STOCK = 10000
TAILLE_SEUIL = 30000
tail = 0

categories = { }
produits = [ ]


def verifierStock(quantite):
    global tail
    if tail + quantite == TAILLE_SEUIL - 2:
            print("Limite de stock dépassé")
            return False
    elif tail + quantite >= TAILLE_MAX_STOCK:
        print("Limite de stock atteinte")
        return  False
    else:
        tail += quantite
            #print(f"{quantite}produit ajoute avec succes. le stock actuel est de {tail}")
        return True


def saisir_date(date_peremption):
    while True:
        #date_peremption = input("saisir la date de peremption (jj/mm/aaaa) : ")
        try:
            date_obj = datetime.strptime(date_peremption, "%d/%m/%Y").date()
            return  date_obj
        except ValueError:
            print("Format invalide. utilisez un format comme 25/12/2002 : ")

def gerer_categorie():
    print("categorie existantes : ", list(categories.keys()))
    categorie = input("choisir ou creer une categorie : ")

    if categorie not in categories:
        categories[categorie] = []

    print(f"Types existants pour {categorie}: ", categories[categorie])
    typeProd = input("choisir ou creer un type: ")

    if typeProd not in categories[categorie]:
        categories[categorie].append(typeProd)
    return categorie, typeProd





def ajoutProd():
    produit = saisi_produit()
    if not verifierStock(produit['quantite']):
        print("ajout annulé probleme de stock")
        return None
    if not saisir_date(produit['date_peremption']):
        return

    categorie, typeProd = gerer_categorie()

    produit.update({
        'matricule': matricule_auto(),
        'date_ajout': date_enregistrement(),
        'categorie': categorie,
        'type': typeProd
    })
    produits.append(produit)
    return produit

def affichProd():
    if not produits:  # Si la liste est vide
        print("\nAucun produit à afficher.")
        return

    print("\n--- LISTE DES PRODUITS ---")
    for i, produit in enumerate(produits, 1):
        print(f"\nProduit {i}:")
        for cle, valeur in produit.items():
            print(f"  {cle.upper()}: {valeur}")

def updateProd():
    modifier = input("saisir le nom du produit à supprimer ou son matricule : ")
    for produit in produits:
        if produit["matricule"] == modifier or produit["nom"] == modifier:
            print(f"Produit trouvé {produit}")
            champ = input("quel champ voulez vous modifier ? nom, prix, quantite : ").lower()
            if champ in produit:
                nouvelle_valeur = input(f"nouveau {champ} : ")

                if champ in ["prix", "quantite"]:
                    try:
                        nouvelle_valeur = float(input(f"nouveau {champ} : "))
                    except ValueError:
                        print("erreur : entrez un nombre validez.")
                produit[champ] = nouvelle_valeur
                print("produit mis à jour")
            else:
                print("champ invalide")
            return
        print("produit non trouvé")


def deleteProd():
    supprimer = input("saisir le nom du produit ou son matricule : ")
    for produit in produits:
        if produit["matricule"] == supprimer or produit["nom"] == supprimer:
            print(f"Produit trouvé {produit}")
            confirmer = input("voulez vous supprime ce produit? cette action sera irreversible. (o/n): ").lower()

            if confirmer == 'o':
                produits.remove(produit)
                print("produit supprimé")
            return
        print("produit non trouvé")