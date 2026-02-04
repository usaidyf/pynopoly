class Space:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.type = "<undefined>"

    def on_land(self, player):
        """Override this in subclasses to define what happens"""
        print(f"{player.name} landed on {self.name}")


class PropertySpace(Space):
    def __init__(self, name, index, price, rent_values):
        super().__init__(name, index)
        self.price = price # Cost to purchase the property
        self.rent_values = rent_values  # A list or dict of rent levels
        self.owner = None # Instance of a Player or None
        self.type = "property"

    def on_land(self, player):
        super().on_land(player)
        if self.owner is None:
            # Logic for offering purchase
            pass
        elif self.owner != player:
            # Logic for paying rent
            pass


class UtilitySpace(PropertySpace):
    type = "utility"
    price = 0
    rent = 0

    def __init__(self, type, price, rent):
        super().__init__(type, price, rent)


class StationSpace(PropertySpace):
    type = "station"
    price = 0
    rent = 0


class CornerSpace(Space):
    type = "corner"
    is_corner = True
    is_jail = False
    is_go_to_jail = False
    is_free_parking = False
    is_go = False


class ChanceSpace(Space):
    is_corner = False
    type = "chance"


class CommunityChestSpace(Space):
    is_corner = False
    type = "community_chest"


class TaxSpace(Space):
    is_corner = False
    type = "tax"
