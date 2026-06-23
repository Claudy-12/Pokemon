import requests

URL_BASE = "https://pokeapi.co/api/v2/pokemon/"

def scarica_pokemon(nome):
    url = URL_BASE + nome.lower()

    try:
        risposta = requests.get(url, timeout=10)

        if risposta.status_code == 200:
            return risposta.json()
        else:
            print("Errore: Pokémon non trovato")
            return None

    except requests.exceptions.RequestException:
        print("Errore di connessione")
        return None


if __name__ == "__main__":
    pokemon = scarica_pokemon("pikachu")

    if pokemon:
        print("OK! Nome:", pokemon["name"])