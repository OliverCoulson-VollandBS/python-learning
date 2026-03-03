# imports requests library. used to send HTTP requests to websites or APIs, this in particular being PokeAPI
#Application Programming Interface 
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    #returns a response object, need to do verify=false passed into uction to avoid SSLError and avoid needing perms to enter site
    # sends a GET request to the API, and returns a respnse object
    response = requests.get(url, verify=False)

# if the status code is correct, (200), the API sends back the data in JSON format, whwere JSON converts it into a python dicionary
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "snorlax"
pokemon_info = get_pokemon_info(pokemon_name)

#(is true)
if pokemon_info:
    print(f"name: {pokemon_info["name"]}".title())
    print(f"id: {pokemon_info["id"]}")
    print(f"pikachus height is {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

print("New branch")