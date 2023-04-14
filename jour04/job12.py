def trier(liste):
    r=[]
    while liste:
        mini=liste[0]
        for z in liste:
            if z < mini:
                mini=z 
        liste.remove(mini)
        r.append(mini)
    return r 

print(trier([41, 17, 3, 4, 17, 51]))
