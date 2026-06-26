from poke_api import scarica_pokemon
from poke_info import estrai_info
from poke_file import salva_scheda


def main():
    nome = input("Inserisci il nome del Pokémon: ")

    # Scarica i dati dalla PokéAPI
    dati = scarica_pokemon(nome)

    if dati is None:
        print("Impossibile ottenere i dati del Pokémon.")
        return

    # Estrae solo le informazioni utili
    info = estrai_info(dati)

    # Mostra le informazioni a schermo
    print("\n=== SCHEDA POKÉMON ===")
    print(f"Numero: {info['numero']}")
    print(f"Nome: {info['nome']}")
    print(f"Tipo: {info['tipo']}")
    print(f"Altezza: {info['altezza_m']} m")
    print(f"Peso: {info['peso_kg']} kg")
    print(f"Esperienza: {info['esperienza']}")

    # Salva la scheda in un file di testo
    nome_file = f"{info['nome']}.txt"
    salva_scheda(info, nome_file)


if __name__ == "__main__":
    main()