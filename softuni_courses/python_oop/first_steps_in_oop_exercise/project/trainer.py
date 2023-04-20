from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for i in self.pokemons:
            if i.name == pokemon_name:
                self.pokemons.remove(i)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data_to_be_returned = ''
        data_to_be_returned += f'Pokemon Trainer {self.name}\n'
        data_to_be_returned += f"Pokemon count {len(self.pokemons)}\n"
        for i in self.pokemons:
            data_to_be_returned += f"- {i.pokemon_details()}\n"
        return data_to_be_returned
