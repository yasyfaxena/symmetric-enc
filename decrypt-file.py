from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_FILE = "secret.key"
INPUT_FILE = "FileScr.txt.enc"
OUTPUT_FILE = "decrypted_FileScr.txt"

with open(KEY_FILE, "rb") as f:
    key = f.read()

with open(INPUT_FILE, "rb") as f:
    encrypted_data = f.read()

nonce = encrypted_data[:12]
ciphertext = encrypted_data[12:]
aesgcm = AESGCM(key)
decrypted_data = aesgcm.decrypt(nonce, ciphertext, None)

with open(OUTPUT_FILE, "wb") as f:
    f.write(decrypted_data)

print("File decryption successful!")
print(f"Input file : {INPUT_FILE}")
print(f"Output file: {OUTPUT_FILE}")

