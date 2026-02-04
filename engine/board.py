import json
from models.space import (
    ChanceSpace,
    CommunityChestSpace,
    PropertySpace,
    TaxSpace,
    StationSpace,
    CornerSpace,
    UtilitySpace,
)


class SpaceFactory:
    @staticmethod
    def create_space(data):
        stype = data.get("type")

        if stype == "property":
            return PropertySpace(
                name=data["name"],
                index=data["index"],
                price=data["price"],
                rent_list=data["rent"],
                house_cost=data["house_cost"],
            )
        elif stype == "tax":
            return TaxSpace(
                name=data["name"], index=data["index"], amount=data["amount"]
            )
        elif stype == "station":
            return StationSpace(
                name=data["name"], index=data["index"], price=data["price"]
            )
        elif stype == "corner":
            return CornerSpace(name=data["name"], index=data["index"])
        elif stype == "utility":
            return UtilitySpace(name=data["name"], index=data["index"])
        elif stype == "chance":
            return ChanceSpace(name=data["name"], index=data["index"])
        elif stype == "community_chest":
            return CommunityChestSpace(name=data["name"], index=data["index"])
        return None


class Board:
    def __init__(self):
        self.spaces = self._load_board()

    def _load_board(self):
        with open("data/properties.json", "r") as f:
            data = json.load(f)
            # This is where the magic happens: list comprehension using the factory
            return [SpaceFactory.create_space(item) for item in data]
