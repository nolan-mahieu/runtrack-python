import re 
import hashlib
import json
import os
import os.path

while True:
    password = input("Choissisez un mot de passe :")
    if len(password) < 8:
        print("le mot de passe doit contenir au moins 8 caracteres") 
    elif not re.search("[a-z]", password):
        print("Erreur : le mot de passe doit contenir au moins une lettre minuscule")
    elif not re.search("[A-Z]", password):
        print("Erreur :  le mot de passe doit contenir au moins une lettre majuscule")
    elif not re.search("[0-9]", password):
        print("Erreur : le mot de passe doit contenir au moins un chiffre")
    elif not re.search("[!?@#$%*&^]", password):
        print("Erreur : le mot de passe doit contenir au moins un caracteres spécial")
    else:
        password_crypté = hashlib.sha256(password.encode()).hexdigest()
        print("le mot de passe est valide")
        print("le mot de passe crypté est:", password_crypté)
        break
password_bytes = password.encode('utf-8')
password_crypté = hashlib.sha256(password_bytes)
hash_hex = password_crypté.hexdigest()
rep = os.path.dirname((__file__))
chemin = os.path.join(rep,"passwords.json")

print("Le hachage SHA-256 du mot de passe est:", hash_hex, "\n"," le fichier est enregistré dans: ", chemin)


with open(chemin, "a+") as f:
    json.dump(hash_hex, f)
    f.write("\n")

with open ("C:\\Users\\geleb\\OneDrive\\Bureau\\Bachelor\\Runtrack_python\\exo_password\\password.json", "r") as f:
    data = json.load(f)
    print(data)
