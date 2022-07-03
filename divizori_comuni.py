def divizori_comuni(unu, doi):
    lista_divizori1 = []
    lista_divizori2 = []
    for i in range(1, unu + 1):
        if(unu % i == 0):
                lista_divizori1.append(i)
    for j in range(1, doi + 1):
        if (doi % j == 0):
            lista_divizori2.append(j)
            
    rez = [i for i in lista_divizori1 if i in lista_divizori2]
    return rez           
    

print(divizori_comuni(20, 60))