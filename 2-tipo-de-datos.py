# STRING: cadena de caracteres, el espacio en blanco también es un caracter, es case sensitive. 
# Pueden ir entre comillas dobles y comillas simples.

# Ejemplos:
print('Hello World')
print("Hello world")
print(type('Hola'))   #TYPE() es para saber el tipo de dato, te informa: class 'str'
# Ejemplo de concatenar (unión)
print( 'Ho' + 'la')

# NUMBERS: números. Si está entre comillas es string.

# INTEGER
print(type(30))  
#es class'int', INTEGER, número entero

#FLOAT
print(type(30.5))   
#es class'float', FLOAT, número flotante (decimal)

# BOOLEAN: booleanos (tipo de dato lógico), puede ser: True, False
foco_prendido = True
foco_apagado = False
print(type(foco_prendido))  # class 'bool'

# LIST: lista de elementos (datos), puede ser de enteros, string, de varios tipos de datos, que pueden cambiar. 
# Va entre [].
numeros = [10, 20, 30, 55]  # lista de enteros
print(numeros)
print(type(numeros))  # class 'list'
print(['Hola', 10, False])  #ejemplo de lista con distintos tipos de datos

# TUPLES: tuplas. Agrupamos datos, que no cambian. Va entre ().
print(type((10, 30)))  # class 'tuple'

# DICTIONARIES : diccionarios. Va entre {} y sepadados por,.
# Está compuesto por KEY(K, clave) : VALUE(C,valor),
# K es el nombre
{
    'nombre': 'Juan',
    'apellido': 'Rodriguez',
    'apodo': 'Juanpa'
}
a= {'pais':'Argentina', 'Provincia': 'Buenos Aires', 'Ciudad': 'San Isidro'}
# Asigno el diccionario a la variable a y la imprimo cocn print()
print(a)
print(type(a))  # class 'dict'

# NONE TYPE: no hay dato definido
type(None)   #class 'NoneType'

