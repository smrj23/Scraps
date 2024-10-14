import json

with open('Liquidos.json') as json_file:
    data = json.load(json_file)
    nombre = []
    precio = []
    for x in range(17):
        nombre.append(data['data']['products'][x]['name'])
        precio.append(data['data']['products'][x]['prices'][0]['price'])

print(nombre,precio)