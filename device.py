class Device():
    _cheapest = None

    def __init__(self, tip, firma, pret) -> None:
        self._tip = tip
        self._firma = firma
        self._pret = pret
        if Device._cheapest is None:
            Device._cheapest = pret
                   
        elif pret < Device._cheapest:
            Device._cheapest = pret

    def describe(self):
        print("Acesta este un {}, produs de {}, cu pretul de {} de lei.")

    def apply_discount(self, percentage):
        self._percentage = percentage
        result = (percentage * self._pret) / 100
        final_result = self._pret - result
        self._pret = round(final_result)
        return round(self._pret)

    @classmethod
    def get_lowest_price(cls):
         print("Cel mai mic pret este {}".format(Device._cheapest))

    @property
    def pret(self):
        return self._pret

    @pret.setter
    def pret(self, value):
        self.value = value
        
        try:
            self._pret = int(value)
            print("Pretul a fost actualizat cu succes!")
            
        except:
            print("Aceasta valoare nu poate fi transformata in int!")


unu = Device("televizor", "panasonic", 4200)
doi = Device("telefon", "samsung", 2000)
trei = Device("monitor", "asus", 700)

trei.pret = "500"

doi.pret = "20a"

unu.apply_discount(10)
doi.apply_discount(30)
trei.apply_discount(15)

print(unu.pret)
print(doi.pret)
print(trei.pret)