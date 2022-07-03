class Device():
    cheapest = None
    def __init__(self,tip, firma, pret) -> None:
        self.tip = tip
        self.firma = firma
        self.pret = pret
        if Device.cheapest is None:
            Device.cheapest = pret
        if pret < Device.cheapest:
            Device.cheapest = pret

    def describe(self):
        print("Acesta este un {}, produs de {}, cu pretul de {} de lei.")

    @classmethod
    def get_lowest_price(cls):
         print("Cel mai mic pret este {}".format(Device.cheapest))


unu = Device("televizor", "panasonic", 4200)
doi = Device("telefon", "samsung", 2000)
trei = Device("monitor", "asus", 700)
describes = [unu, doi, trei]
print(Device.get_lowest_price())
print(unu.describe())
print(unu.firma)