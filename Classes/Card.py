class Card:
    def __init__(self, name, ressource_type, cost, effect, value, target, rarity, description):
        self.name = name
        self.ressource_type = ressource_type
        self.cost = cost
        self.effect = effect
        self.value = value
        self.target = target
        self.rarity = rarity
        self.description = description

    def _get_name(self):
        return self.name

    def _set_name(self, new_name):
        self.name = new_name

    def _get_ressource_type(self):
        return self.ressource_type

    def _set_ressource_type(self, new_ressource_type):
        self.ressource_type = new_ressource_type

    def _get_cost(self):
        return self.cost

    def _set_cost(self, new_cost):
        self.cost = new_cost

    def _get_effect(self):
        return self.effect

    def _set_effect(self, new_effect):
        self.effect = new_effect

    def _get_value(self):
        return self.value

    def _set_value(self, new_value):
        self.value = new_value

    def _get_target(self):
        return self.target

    def _set_target(self, new_target):
        self.target = new_target

    def _get_rarity(self):
        return self.rarity

    def _set_rarity(self, new_rarity):
        self.rarity = new_rarity

    def _get_description(self):
        return self.description

    def _set_description(self, new_description):
        self.description = new_description
