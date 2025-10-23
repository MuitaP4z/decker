import requests

def buscar_carta_scryfall(nome):
    url = f"https://api.scryfall.com/cards/named?fuzzy={nome}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    return {
        'edicao': data.get('set_name', ''),                # aqui garantimos 'edicao'
        'imagem_url': data.get('image_uris', {}).get('normal', ''),
        # você pode retornar outros campos se quiser
    }
