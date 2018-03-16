class Shore():

    def __init__(self, side):
        self.side = side
        self.animal_count = {"wilderbeast": 0, "lion": 0}



class Animal():

    def __init__(self):
        self.side = "right"
        self.species = None

    def board(self, raft):
        raft = raft.load(self)
        return raft


class Raft():

    def __init__(self):
        self.spot1 = {"slot": "empty", "species": "empty"}
        self.spot2 = {"slot": "empty", "species": "empty"}
        self.side = "right"
        self.capacity = [0, 0]

    def cross(self):
        if self.side == "right":
            self.side = "left"
        else:
            self.side = "right"

    def load(self, animal):
        if self.capacity[0] == 0:
            self.capacity[0] = 1
            self.spot1 = {"slot": "full", "species": animal.species}
            print("loaded")
        elif self.capacity[1] == 0:
            self.capacity[1] = 1
            self.spot2 = {"slot": "full", "species": animal.species}
            print("loaded")
        else:
            print("Fully loaded")

    def unload(self):
        unloaded_animal = input("Which animal to unload: \n")
        unloaded_animal = unloaded_animal.lower()
        if self.spot1["species"].lower() == unloaded_animal:
            self.capacity[0] = 0
            self.spot1 = {"slot": "empty", "species": "empty"}
            print("unloaded")
        elif self.spot2["species"].lower() == unloaded_animal:
            self.capacity[1] = 0
            self.spot2 = {"slot": "empty", "species": "empty"}
            print("unloaded")
        else:
            print("Empty")


class Wilderbeast(Animal):

    def __init__(self):
        self.species = "Wilderbeast"


class Lion(Animal):

    def __init__(self):
        self.species = "Lion"


traft = Raft()
jane = Wilderbeast()
jane.board(traft)
print(traft.spot1["species"])