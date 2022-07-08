from cgitb import text
import hashlib

msg = input("Saisir le message à hasher : ")
hash = hashlib.sha256()
hash.update(msg.encode('utf-8'))

print("Voici le message hashé : {}".format(hash.hexdigest()))