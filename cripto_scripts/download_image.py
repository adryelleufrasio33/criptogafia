import requests


def download_image(url, path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content)
        print(f"Imagem baixada e salva em: {path}")
    else:
        print(f"Falha ao baixar a imagem. Status code: {response.status_code}")


if __name__ == "__main__":
    image_url = "https://stock.adobe.com/br/search?k=%22umbilical+hernia%22&asset_id=273474082"
    image_path = 'prova_cripto.jpg'

    download_image(image_url, image_path)
