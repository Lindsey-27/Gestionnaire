


def saisi_produit():
    produit = {
        'nom': input("Nom du produit: "),
        'prix': float(input("Prix: ")),
        'quantite': int(input("Quantité: ")),  # <-- Doit être présent
        'date_peremption': input("Date (JJ/MM/AAAA): ")
    }
    return produit
    #return {'nom' : nom, '\n' 'prix ': prix, '\n' 'quantite' : quantite, '\n' 'date_peremption' : date_peremption }

