class Car():
    def __init__(self, maker, model, hp):
        self._maker = maker
        self._model = model
        self._hp = hp

    def __str__(self):
        x = self._maker, self._model, self._hp
        return str(x)

    def __repr__(self):
        return self.__str__().replace("'", '')

    def __lt__(self, other):
        return self._hp < other._hp
     
unu = Car("Mercedes", "Amg", 650)
doi = Car("Redbull", "F1", 1000)
trei = Car("Ford", "Mustang", 400)
patru = Car("Ferrari", "Enzo", 700)

l = [unu, doi, trei, patru]
l.sort()
print(l)