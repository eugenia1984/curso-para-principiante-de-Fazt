# LISTAS: entre [] va guardando varios elementos, que pueden ser de cualquier tipo de dato

# Creando lista con el constructor, basada en tuplas ()
lista_de_numeros = list((1, 2, 3, 4))
print(lista_de_numeros)  # [1, 2, 3, 4]

# Creando una lista con el construcor, basada en un rango
r = list(range(1,10))
print(r)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]


# print(dir(r))  y veo qué puedo hacer con una lista

print(len(r))  # 9 la longitud
print(r[0])  # 1 la ubicación
print(r[-2]) # 8 la ubicación,empezando a contar desde el final
print('20' in r)  # False, para ver si un elemento existe dentro de la lista

# Para reasignar valor a un elemento de la lista
r[1] = 20
print(r)   #[1, 20, 3, 4, 5, 6, 7, 8, 9]

# Para agregar elementos a la lista, basado en una tupla, al final:
r.extend([55, 60])
print(r)   # [1, 20, 3, 4, 5, 6, 7, 8, 9, 55, 60]

# Para agregar un elemento, indicando en la posiciñon que quiero que esté:
r.insert(1, 800)
print(r)   # [1, 800, 20, 3, 4, 5, 6, 7, 8, 9, 55, 60]

# Para agregar un elemento, al final:
r.insert(len(r), 700)
print(r)    # [1, 800, 20, 3, 4, 5, 6, 7, 8, 9, 55, 60, 700]

# Para quitar el último elemento:
r.pop()
print(r)   # [1, 800, 20, 3, 4, 5, 6, 7, 8, 9, 55, 60]

# Para especificar qué posición quiero sacar (por índice)
r.pop(1)
print(r)   # [1, 20, 3, 4, 5, 6, 7, 8, 9, 55, 60]

# Para especificar qué elemento quiero sacar
r.remove(7)
print(r)   # [1, 20, 3, 4, 5, 6, 8, 9, 55, 60]

# Para dejar la lista vacia
r.clear()
print(r)   # []

# Creo una nueva lista
colores = ["red", "green", "blue", "red"]

# Para ordenarlos alfabéticamente
# colores.sort()
# print(colores)

# Para ordenarlos a la inversa
# colores.sort(reverse=True)
# print(colores)

# Para obtener el índice de un elemento (su posicion)
# print(colores.index('red'))

# Parasaber cuántas veces tengo un mismo elemento
print(colores.count('red')) 



 






