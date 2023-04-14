import re 
import hashlib
import json
import os


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

if not os.path.exists(chemin):
    with open(chemin, "w") as file:
        start = {"users": [
            {"mdp": hash_hex} ]}
        json.dump(start, file)
else:
    with open(chemin, "r") as f:
        mdps = json.load(f)

    with open(chemin, "w") as f:
        if {"mdp": hash_hex} not in mdps["users"]:
            mdps["mdp"].append({"mdp": hash_hex})
            json.dump(mdps, f)

