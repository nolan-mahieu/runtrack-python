def chiffre_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''
    for lettre in message:
        if lettre.lower() in alphabet:
            lettre_chiffree = alphabet[(alphabet.index(lettre.lower()) + decalage) % 26]
            message_chiffre += lettre_chiffree.upper() if lettre.isupper() else lettre_chiffree
        else:
            message_chiffre += lettre
    return message_chiffre

message = "Bonjour tout le monde !"
decalage = 3
message_chiffre = chiffre_cesar(message, decalage)
print(message_chiffre)