L = [8, 24, 48, 2, 16]
print("Afficher a l'endroit :", (L))
long = len(L)
def liste():
    temp = L[0]
    L[0] = L[-1]
    L[-1] = temp
    print("Afficher a l'envers :", (L))
liste()

