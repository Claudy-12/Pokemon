import requests

def scarica_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"

    risposta = requests.get(url)

    if risposta.status_code == 200:
        return risposta.json()

    return None