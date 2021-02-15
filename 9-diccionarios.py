# DICCIONARIO: definir un dato a través de claves y valores

cart = { 
    "name": "book",
    "quantity": 3,
    "price": 4.99
}
print(type(cart))
# class 'dict'

person = { "first_name": "Ryan", "last_name": "Lopez"}

# print(dir(person)) para ver la lista de métodos

# print(person.keys())
# Imprime: dict_keys(['first_name', 'last_name'])

# print(person.items())
# Imprime: dict_items([('first_name', 'Ryan'), ('last_name', 'Lopez')])

# Para eliminar un diccionario:
# del person

# Para limpiar los datos de adentro, queda un diciconario vacío:
# print(cart.clear())

# Los diccionarios puedes agruparlos dentro de una lista de productos
productos = [
    {"name": 'book', "price": 10.99},
    {"name": 'laptop', "price": 30.999}
]

print(productos)
# [{'name': 'book', 'price': 10.99}, {'name': 'laptop', 'price': 30.999}]