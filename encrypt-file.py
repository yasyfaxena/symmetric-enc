from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

KEY_FILE = "secret.key"
INPUT_FILE = "FileScr.txt"
OUTPUT_FILE = "FileScr.txt.enc"

with open(KEY_FILE, "rb") as f:
    key = f.read()

with open(INPUT_FILE, "rb") as f:
    data = f.read()

nonce = os.urandom(12)
aesgcm = AESGCM(key)
encrypted_data = aesgcm.encrypt(nonce, data, None)

with open(OUTPUT_FILE, "wb") as f:
    f.write(nonce + encrypted_data)

print("File encryption successful!")
print(f"Input file : {INPUT_FILE}")
print(f"Output file: {OUTPUT_FILE}")

