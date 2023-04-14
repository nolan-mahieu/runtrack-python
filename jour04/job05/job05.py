
L = [2, 4, 6, 8, 10]

print("La valeur de L[1] est :", L[1])

def remplacer(L):
    L[3] = L[2] + L[4]
    print(L[3])
    print(L)
    

remplacer(L)

print("La valeur du dernier terme de la liste est :", L[-1])

