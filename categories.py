import sqlite3
from datetime import datetime

from generer import date_enregistrement
from produits import ajouter_produit

TAILLE_MAX_STOCK = 10000
TAILLE_SEUIL = 30000
tail = 0

def verifier_stock(quantite):
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
            return  True
        except ValueError:
            #print("Format invalide. utilisez un format comme 25/12/2002 : ")
            return False


def ajouter_categorie(nom, description=None):
    conn = sqlite3.connect('inventaire.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO categories (nom, description) VALUES (?, ?)
        ''', (nom, description))
        conn.commit()
        print(f"Categorie '{nom}' ajoutée")
    except sqlite3.IntegrityError:
        print(f"Erreur, la categorie '{nom}' existe déjà")
    finally:
        conn.close()

def ajouter_sous_categorie(nom, description = None, parent_id = None):
    conn = sqlite3.connect('inventaire.db')
    cursor = conn.cursor()

    # Verifier que la categorie parente existe
    cursor.execute("SELECT * FROM categories WHERE id = ?", (parent_id,))
    parent = cursor.fetchone()
    if not parent:
        print(f"Aucune categorie trouvée avec ID {parent_id}")
    else:
        try:
            cursor.execute('''INSERT INTO categories (nom, description, parent_id) VALUES (?, ?, ?)''',
                           (nom, description, parent_id))
            conn.commit()
            print(f"Sous categorie '{nom}' ajoutée à {parent[1]} avec succes")
        except sqlite3.IntegrityError:
            print(f"Erreur: la sous categorie {nom} existe deja")
    conn.close()

def afficher_categorie(categorie_id, date_peremption=None):
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, description FROM categories WHERE id = ? AND  parent_id IS NULL", (categorie_id,))
    categorie = cursor.fetchone()
    if not categorie:
        print(f"Aucune categorie avec Id {categorie_id}")
        conn.close()
        return
    print(f"\nCategorie : {categorie[1]} (ID {categorie[0]}")
    if categorie[2]:
        print(f"description {categorie[2]}")
    cursor.execute("SELECT id, nom FROM categories WHERE parent_id = ?",(categorie_id,))
    sous_categorie = cursor.fetchall()
    if sous_categorie:
        print(f"Sous categorie: ")
        for scategorie in sous_categorie:
            print(f" - {scategorie[1]} (ID{scategorie[0]})")
            cursor.execute("SELECT id,nom, prix, quantite, date_peremption, date_enregistrement, description"
                           " FROM produits WHERE categorie_id = ?",(scategorie[0],))
            produits = cursor.fetchall()
            if produits:
                print(" produits : ")
                for produit in produits:
                    produit_id = produit[0],
                    produit_nom = produit[1]
                    produit_prix = produit[2]
                    produit_quantite = produit[3]
                    produit_date_peremption = produit[4]
                    produit_date_enregistrement = produit[5]
                    produit_description = produit[6]
                    if date_peremption:
                        print(f"{produit_nom}; (Id {produit_id}) ;{produit_description}; {produit_prix};"
                              f"{produit_date_peremption}; {produit_date_enregistrement}; {produit_quantite}")
                    else:
                        print(f"{produit_nom}; (Id {produit_id}) ;{produit_description}; {produit_prix};"
                              f"pas de date de peremption; {produit_date_enregistrement}; {produit_quantite}")
                else:
                    print("aucun produit")


if __name__ == "__main__":
    print("1. ajouter une nouvelle categorie")
    print("2. ajouter une nouvelle sous categorie")
    print("3. afficher une  categorie")
    print("4. ajouter un  produit")
    choix = input("ton choix: ").strip()

    nom = input("nom categorie: ").strip()
    description = input("description facultative = ").strip() or None
    if choix == "1":
        ajouter_categorie(nom, description)
    elif choix == "2":
        parent_id = input("Id de la categorie parente : ").strip()
        if parent_id.isdigit():
            ajouter_sous_categorie(nom, description, int(parent_id))
        else:
            print("id parent invalide")
    elif choix == "3":
        id_categorie = input("entrez l'id de la categorie : ").strip()
        if id_categorie.isdigit():
            afficher_categorie(int(id_categorie))
    elif choix == "4":
        nomProd = input(" nom produit ").strip()
        descriptionProd = input(" description ").strip() or None
        prix = input("Prix produit ").strip()
        prixProd = float(prix)
        quantite = input("quantite de produit ").strip()
        date_peremption = input("date peremprion ")
        if saisir_date(date_peremption):
            print()
        else:
            print("date invalide")
        categorie_id = input("ID de la categorie ou sous categorie ").strip()
        if not categorie_id.isdigit():
            print("Id de la categorie invalide")
            exit()
        ajouter_produit(nom, description, prix, quantite, date_peremption, date_enregistrement, int(categorie_id))

    else:
        print("choix inconnu")