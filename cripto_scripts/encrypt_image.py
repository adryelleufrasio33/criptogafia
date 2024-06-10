# cripto_scripts/encrypt_image.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_image(input_image_path, output_image_path, key_path):
    with open(input_image_path, 'rb') as image_file:
        image_data = image_file.read()

    key = os.urandom(32)  # Chave AES de 256 bits
    iv = os.urandom(16)  # Vetor de Inicialização

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    encrypted_data = encryptor.update(image_data) + encryptor.finalize()

    with open(output_image_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    # Salvar chave e IV em um arquivo
    with open(key_path, 'wb') as key_file:
        key_file.write(key + iv)
