# Gestionnaire
gestion de produit


dans ce projet qui consiste à organiser et gerer un inventaire de produit(tout genre) j'ai
creer plusieurs fichiers: 
main.py qui est le fichier principal
database.py qui contient la base de donnée inventaire.db qui elle contient deux tables :
*table categories qui geres à la fois les categories de produit et les sous categories 
par le biais d'une colonne parent_id qui permet de lier categorie à sous categorie
*table produits qui stocke tous les produits qui sont enregistré et c'est liée à categories
categories.py qui contient plusieurs fonctions essentielles :
* verifier_stock : verifie que l'utilisateur ne dépasse pas les limites de quantite max
* saisir_date : permettre à l'user de saisir une date de peremption pour certains produit
et verifie que la date saisie est correcte( cette partie est optionnelle selon choix de
l'utilisateur)
* ajouter_categorie : 
