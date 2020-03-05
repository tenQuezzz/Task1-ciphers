def encrypt(ch, key):
    c = (ch + key) % 256
    return c


def decrypt(ch, key):
    c = (ch - key) % 256
    return c


def encrypt_data(data, key):
    encrypted = []
    for value in data:
        encrypted.append(encrypt(value, key))
    return encrypted


def decrypt_data(data, key):
    decrypted = []
    for value in data:
        decrypted.append(decrypt(value, key))
    return decrypted
