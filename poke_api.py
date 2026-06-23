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

    except requests.exceptions.ConnectionError:
        print("Errore: nessuna connessione a Internet")
        return None

if __name__ == "__main__":
    pokemon = scarica_pokemon("pikachu")

    if pokemon is not None:
        print("OK! Nome:", pokemon["name"])
        print("ID:", pokemon["id"])
        print("Altezza:", pokemon["height"])
        print("Peso:", pokemon["weight"])

