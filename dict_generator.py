import re
from collections import defaultdict
rez = []

data = {}

n = int(input())

for i in range(n):
    new_dict = {}
    nume = input().split(': ')[1]
    limbaje = input().split(': ')[1]

    new_dict["nume"] = nume
    new_dict["limbaje"] = limbaje.split(', ')
    rez.append(new_dict)     
print(rez)


key_list = ["nume", "limbaje"]