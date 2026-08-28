import os

key = os.urandom(32)

with open("secret.key", "wb") as file:
    file.write(key)

print("The AES-256 key was successfully generated.")
print("The key is stored in secret.key")

