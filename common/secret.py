from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("../secret/secret.key", "wb") as key_file:
        key_file.write(key)
    return key


def load_key():
    """
    Load the previously generated key
    """
    return open("./secret/secret.key", "rb").read()


def encrypt_message(message, key):
    """
    Encrypts a message
    """
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message


def decrypt_message(encrypted_message, key):
    """
    Decrypts an encrypted message
    """
    f = Fernet(key)
    message = f.decrypt(encrypted_message)
    return message.decode()
