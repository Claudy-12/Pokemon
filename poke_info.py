def estrai_info(dati):
    """
    Riceve il dizionario JSON grezzo da PokéAPI.
    Ritorna un dizionario semplice con solo i campi utili.
    """
    info = {}

    # CAMPO 1: nome del Pokémon
    info["nome"] = dati["name"]

    # CAMPO 2: numero del Pokédex
    info["numero"] = dati["id"]

    # CAMPO 3: altezza in metri (height è in decimetri, dividi per 10)
    info["altezza_m"] = dati["height"] / 10

    # CAMPO 4: peso in kg (weight è in ettogrammi, dividi per 10)
    info["peso_kg"] = dati["weight"] / 10

    # CAMPO 5: tipo principale (attenzione: è una struttura annidata!)
    info["tipo"] = dati["types"][0]["type"]["name"]

    # CAMPO 6: esperienza base
    info["esperienza"] = dati["base_experience"]

    return info


# Test: esegui questo file direttamente per provare
if __name__ == "__main__":
    # Dati finti per testare senza chiamare l'API
    dati_finti = {
        "name": "pikachu",
        "id": 25,
        "height": 4,
        "weight": 60,
        "base_experience": 112,
        "types": [{"slot": 1, "type": {"name": "electric"}}]
    }

    risultato = estrai_info(dati_finti)
    print(risultato)