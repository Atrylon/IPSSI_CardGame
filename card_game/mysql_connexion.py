import MySQLdb as mdb

DBNAME = "ipssi_card_game"
DBHOST = "localhost"
DBPASS = ""
DBUSER = "root"


def init_db():

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
        Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Name CHAR(100) NOT NULL
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

        # Creer table Player
        sqlquery4 = """
        CREATE TABLE IF NOT EXISTS Player (
        Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Player_index INT NOT NULL,
        Name CHAR(100) NOT NULL,
        HP INT NOT NULL,
        Shield INT NOT NULL,
        Gold_generation INT NOT NULL,
        Gold_stock INT NOT NULL,
        Mana_generation INT NOT NULL,
        Mana_stock INT NOT NULL,
        Action_generation INT NOT NULL,
        Action_stock INT NOT NULL
        )
        """
        cur.execute(sqlquery4)
        print("Table Player Created Successfully")

        # Creer table Player_Hand
        sqlquery5 = """
        CREATE TABLE IF NOT EXISTS Player_hand (
        Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Id_Player INT  NOT NULL,
        Id_card INT  NOT NULL
        )
        """
        cur.execute(sqlquery5)
        print("Table Player_hand Created Successfully")

        db.close()

    except mdb.Error as e:
        print("Connexion error")


def readCards():

    final_result = []

    try:
        connection = mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)

        query = "SELECT * FROM card"

        cursor = connection.cursor()
        cursor.execute(query)

        result = cursor.fetchall()

        final_result = [list(i) for i in result]
        # print(final_result)

    except mdb.Error as e:
        print("Connexion error")

    return final_result