data_pwd = {
    "mdp": password_crypté
}
chemin = 'C:\\Users\\geleb\\OneDrive\\Bureau\\Bachelor\\Runtrack_python\\exo_password'
dossier = os.path.join(chemin, "data_pwd.json")

if not os.path.exists(dossier):
    with open(dossier, "a+") as write_file:
        json.dump([data_pwd], write_file)
        print("info inscrit dans .json file")

with open(dossier, "r+") as file:
    data = json.load(file)
    if data_pwd not in data:
        data.append(data_pwd)
        json.dump(data_pwd, file)
        print("le mdp est enregistré")

        print("le mote de passe existe deja")
