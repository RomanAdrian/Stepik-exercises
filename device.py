class Device():
    cheapest = None

    def __init__(self,tip, firma, pret) -> None:
        self.tip = tip
        self.firma = firma
        self.pret = pret
        if Device.cheapest is None:
            Device.cheapest = pret
                   
        elif pret < Device.cheapest:
            Device.cheapest = pret

    def describe(self):
        print("Acesta este un {}, produs de {}, cu pretul de {} de lei.")

    def apply_discount(self, percentage):
        self.percentage = percentage
        result = (percentage * self.pret) / 100
        final_result = self.pret - result
        self.pret = round(final_result)
        return round(self.pret)

    @classmethod
    def get_lowest_price(cls):
         print("Cel mai mic pret este {}".format(Device.cheapest))


unu = Device("televizor", "panasonic", 4200)
doi = Device("telefon", "samsung", 2000)
trei = Device("monitor", "asus", 700)

unu.apply_discount(10)
doi.apply_discount(30)
trei.apply_discount(15)

print(unu.pret)
print(doi.pret)
print(trei.pret)