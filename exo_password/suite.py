import random
import string

minu = string.ascii_lowercase
maj = string.ascii_lowercase
nombre = string.digits
spéciaux = string.punctuation

alphabet = minu + maj + nombre + spéciaux
pwd_length = 8 

while True:
    pwd = ""
    for i in range(pwd_length):
        pwd += "" .join(random.choice(alphabet))
    if (any(char in spéciaux for char in pwd)and any(char in nombre for char in pwd)and any(char in minu for char in pwd) and any(char in maj for char in pwd)):
        break
    print(pwd)
