import json

lista_productos = []

with open('Liquidos.json') as json_file:
    data = json.load(json_file)
    nombre = []
    precio = []
    for x in range(17):
        nombre = (data['data']['products'][x]['name'])
        precio =(data['data']['products'][x]['prices'][0]['price'])

        producto = {
            'Producto': nombre,
            'Precio': precio
        }
        lista_productos.append(producto)


print(lista_productos)
