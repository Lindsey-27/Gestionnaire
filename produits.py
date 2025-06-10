import sqlite3

def ajouter_produit(nom, date_peremption = None, description = None, categorie_id = None, prix=None, quantite=None):
    conn = sqlite3.connect("inventaire.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nom FROM categories WHERE id=? ",(categorie_id,))
    categorie = cursor.fetchone()
    if not categorie:
        print(f"aucune categorie avec Id {categorie_id}")
        conn.close()
        return
    try:
        cursor.execute('''INSERT INTO categories (nom, prix, quantite, date_peremption, description, categorie_id)
        VALUES (?, ?, ?, ?, ?, ?)''', (nom, description, prix, quantite, date_peremption, categorie_id))
        conn.commit()
        print(f"Produit '{nom}' ajoutée dans la categorie {categorie[0]}")
    except sqlite3.Error as e:
        print(f"Erreur, lors de l'ajout du produit ", e)
    conn.close()