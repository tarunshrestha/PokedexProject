import requests
import os

url = 'https://pokeapi.co/api/v2/pokemon?limit=1'

response = requests.get(url)


def search_image(name):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': name,
        'cx': os.environ.get('SEARCH_ENGINE_ID'),
        'key': os.environ.get('GOOGLE_API_KEY'),
        'searchType': 'image',
        'num': 1,
    }
    response = requests.get(search_url, params=params)
    print(response.json())
    if response.status_code == 200:
        try:
            search_results = response.json()
            items = search_results.get('items')
            if items:
                return items[0]['link']  # Return the first image link
        except requests.exceptions.JSONDecodeError:
            print("Error decoding JSON response")
    else:
        print(f"Request failed with status code {response.status_code}")


class PokemonsData:
    def __init__(self):
        self.data = response.json()

    def get_data(self):
        datas = self.data
        pokemons_data = {}
        for pokemon in datas['results']:
            name = pokemon['name']
            detail_url = pokemon['url']
            data = requests.get(pokemon['url']).json()
            types = [type['type']['name'] for type in data['types']]
            moves = [move['move']['name'] for move in data['moves']]
            image_url = search_image(name)
            pokemons_data[name] = {
                'detail_url': detail_url,
                'types': types,
                'moves': moves,
                'image_url': image_url
            }
        return pokemons_data


# data = PokemonsData()
# print(data.get_data())

# print(search_image("Dragon"))