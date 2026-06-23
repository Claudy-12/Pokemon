from poke_api import scarica_pokemon

pokemon = scarica_pokemon("pikachu")

if pokemon:
    print("Nome:", pokemon["name"])
    print("Altezza:", pokemon["height"])
else:
    print("Pokémon non trovato")