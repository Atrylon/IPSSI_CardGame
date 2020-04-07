class Player:
    def __init__(self, index, name):
        # Joueur 1 ou Joueur 2
        self.player_index = index
        self.name = name
        self.hp = 100
        self.shield = 30
        # Tableau qui contient la main du joueur - 7 cartes max
        self.hand = []
        self.gold_generation = 1
        self.gold_stock = 0
        self.mana_generation = 1
        self.mana_stock = 0
        self.action_generation = 1
        self.action_stock = 0

    def changeHP(self, hp_change):
        self.hp = self.hp - hp_change
        print("Vous avez actuellement " + self.hp + " pvs !")

    def changeShield(self, shield_change):
        self.shield = self.shield - shield_change
        print("Vous avez actuellement " + self.shield + " points de bouclier !")

    def get_player_index(self):
        return self.player_index

    def get_player_hand(self):
        return self.hand

