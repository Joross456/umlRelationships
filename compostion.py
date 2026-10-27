class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self):
        self.rooms = [
            Room("Bedroom"),
            Room("Kitchen")
        ]


house = House()

for room in house.rooms:
    print(room.name)