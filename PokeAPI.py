import requests

pokemon = input("Ingresa nombre del Pokemon: ")
peticion = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
data = peticion.json()

print("\nTipo(s): ")



print("Habilidades: \n")
habilidades = data["abilities"]
print(habilidades[0]["ability"]["name"])
print("\n")

print("Posibles Ataques: \n")
movimientos = data["moves"]
for mov in movimientos:
    print(mov["move"]["name"])
print("\n")








