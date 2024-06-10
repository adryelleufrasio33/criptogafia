# cripto_scripts/decrypt_image.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_image(input_encrypted_path, output_image_path, key_path):
    with open(input_encrypted_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Ler chave e IV do arquivo
    with open(key_path, 'rb') as key_file:
        key_iv = key_file.read()
        key = key_iv[:32]  # Primeiros 32 bytes para a chave
        iv = key_iv[32:]  # Últimos 16 bytes para o IV

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Verificar se o diretório existe e criar se necessário
    output_directory = os.path.dirname(output_image_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Salvar imagem descriptografada no caminho especificado
    with open(output_image_path, 'wb') as image_file:
        image_file.write(decrypted_data)

    print(f"Imagem descriptografada salva em: {output_image_path}")

# Exemplo de uso

