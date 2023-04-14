import hashlib, json, os

password = input("Veuillez saisir un mot de passe:")

if len(password) < 8:
    print("Le mot de passe doit avoir une longueur minimale de 8 caractères")
elif not any(mot.isupper() for mot in password):
    print("Le mot de passe doit contenir au moins une lettre majuscule")
elif not any(mot.islower() for mot in password):
    print("Le mot de passe doit contenir au moins une lettre minuscule")
elif not any(mot.isdigit() for mot in password):
    print("Le mot de passe doit contenir au moins un chiffre")
elif not any(mot in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '.'] for mot in password):
    print("Le mot de passe doit contenir au moins un caractère spécial")
else:
    print("Le mot de passe est sécurisé !")

password_bytes = password.encode('utf-8')
hash_object = hashlib.sha256(password_bytes)
hash_hex = hash_object.hexdigest()
rep = os.path.dirname((__file__))
chemin = os.path.join(rep,"passwords.json")

print("Le hachage SHA-256 du mot de passe est:", hash_hex, "\n"," le fichier est enregistré dans: ", rep)

with open(chemin, "a") as f:
    json.dump([hash_hex], f)
    f.write("\n")