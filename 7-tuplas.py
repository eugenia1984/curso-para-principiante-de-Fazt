# TUPLAS: datos que no cambian

x = (1, 2, 3)
print(x)

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

# Crearla con un constructor
y = tuple(("a", "b", "c"))
print(y)

# Métodos con tuplas, para listarlos todos:
# print(dir(x))

# Si creo una tupla de un solo elemento x = (1), y si mando a la console, me imprime 1, como un int, no como una tupla.
# Para crear una tupla de un solo elemento x = (1,) , con la , indico que es un elemento dentro de un conjunto de elementos.

# Para acceder al valor de un elemento:
print(x[0])

# Al ser tupla no puedo reasignar valores (sus valores no varían)

# Para borrar la tupla
del x 

# Dentro de un diccionario puedo tener tuplas dentro
locations = { (35.125, 39.55445):"Tokyo", (57.558, 28.458):"New York" }
print(locations)