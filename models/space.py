class Space:
    is_corner = False
    index = None
    name = ""


class PropertySpace(Space):
    name = "property"
    price = 0
    rent = 0
    index = None

    def __init__(self, name, price, rent, index=None):
        self.index = index
        self.name = name
        self.price = price
        self.rent = rent


class UtilitySpace(PropertySpace):
    name = "utility"
    price = 0
    rent = 0

    def __init__(self, name, price, rent):
        super().__init__(name, price, rent)


class StationSpace(PropertySpace):
    name = "station"
    price = 0
    rent = 0


class CornerSpace(Space):
    name = "corner"
    is_corner = True
    is_jail = False
    is_go_to_jail = False
    is_free_parking = False
    is_go = False


class ChanceSpace(Space):
    is_corner = False
    name = "chance"


class CommunityChestSpace(Space):
    is_corner = False
    name = "community_chest"


class TaxSpace(Space):
    is_corner = False
    name = "tax"
