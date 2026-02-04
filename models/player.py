class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = 0
        self.money = 1500  # Starting money
        self.properties = []  # List of owned properties
        self.in_jail = False
