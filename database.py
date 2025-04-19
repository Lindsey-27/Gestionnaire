import sqlite3
def creer_base():
    conn = sqlite3.connect('inventaire.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories
    ( id INTEGER PRIMARY KEY AUTOINCREMENT,
      nom TEXT NOT NULL,
      parent_id INTEGER,
      FOREIGN KEY (parent_id) REFERENCES categories(id)
    );
    ''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS produits
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        description TEXT,
        prix REAL NOT NULL,
        quantite INTEGER DEFAULT 0,
        date_peremption DATE,
        date_enregistrement DATETIME DEFAULT CURRENT_TIMESTAMP,
        categorie_id INTEGER,
        FOREIGN KEY (categorie_id) REFERENCES categogies(id)
    );
    ''')
    conn.commit()
    conn.close()
    print("base de données créées avec succes")
creer_base()