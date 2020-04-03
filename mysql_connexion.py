import MySQLdb as mdb


def init_db():
    DBNAME = "ipssi_card_game"
    DBHOST = "localhost"
    DBPASS = ""
    DBUSER = "root"

    try:
        db = mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
        print("Database Connected Successfully")

        cur = db.cursor()

        # Creer table Card
        sqlquery = """
        CREATE TABLE IF NOT EXISTS card (
        Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Name CHAR(100) NOT NULL,
        Ressource_type CHAR(10) NOT NULL,
        Cost INT NOT NULL,
        Effect CHAR(100) NOT NULL,
        Value INT NOT NULL,
        Target CHAR(100) NOT NULL,
        Rarity CHAR(100) NOT NULL,
        Description CHAR(255) NOT NULL
        )
        """
        cur.execute(sqlquery)
        print("Table card Created Successfully")

        # Creer table Deck
        sqlquery2 = """
        CREATE TABLE IF NOT EXISTS Deck (
        Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL
        )
        """
        cur.execute(sqlquery2)
        print("Table deck Created Successfully")

        # Creer table Deck_Cards
        sqlquery3 = """
        CREATE TABLE IF NOT EXISTS Deck_cards (
        Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Id_Deck INT  NOT NULL,
        Id_card INT  NOT NULL
        )
        """
        cur.execute(sqlquery3)
        print("Table deck_card Created Successfully")

        db.close()

    except mdb.Error as e:
        print("Connexion error")