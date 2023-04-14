L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

min_elem = L[0]
max_elem = L[0]

for i in L:
    if i < min_elem:
        min_elem = i
    if i > max_elem:
        max_elem = i 

print("Afficher l'element minimum", min_elem)
print("Afficher l'elment maximum" , max_elem)

