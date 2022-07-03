d = {
    "1": {
        "comment": "1) Is formula 1 2022 game worth buying?",
        "reply": [
            "2",
            "6"
        ]
    },
    "2": {
        "comment": "2) I assure you it makes up for the price.",
        "reply": [
            "3"
        ]
    },
    "3": {
        "comment": "3) Idk what to say, seems a little bit expensive, but a lot of fun nonetheless.",
        "reply": [
            "4",
            "5"
        ]
    },
    "4": {
        "comment": "4) This is not expensive",
        "reply": []
    },
    "5": {
        "comment": "5) You get 20% off if you own the 2021 game, not expensive",
        "reply": []
    },
    "6": {
        "comment": "6) If you have the money, buy it.",
        "reply": []
    }
}

tabs = 0
spatiu = '\t'
def parcurgere(tabs, id):
    if id in d:
        for k,v in d[id].items():
            if isinstance(v, list):
                for x in v:
                    parcurgere(tabs, x)
            else:
                print(tabs * spatiu + v + '\n')
                tabs = tabs + 1
parcurgere(0, "1")