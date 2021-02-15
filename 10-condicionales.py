# OPERADORES DE COMPARACIÓN: >, <, >=, <=, ==, !=

# EJEMPLO DE IF:
x = 20
if x < 30:
    print('x es menor que 3')
# Si es cierta (True) la condición de x, entonces se ejecuta el print

# EJEMPLO DE IF / ELSE
y = 31
if y == 30:
    print(' y es igual a 30')
else:
    print(' y es distinto de 30')
# Si es cierta (True) la condicion de y seejecuta el primer código, sino para al else y ejecuta el códigode else.

# EJEMPLO DE IF / ELIF / ELSE

color = 'green'
if color == 'red':
    print(' El color es RED')
elif color == 'blue':
    print (' El color es BLUE')
else:
    print('Cualquier color')
# Si color = ' red' imprime 'El color es RED'
# Si color = 'blue' imprime 'El color es BLUE'

# Puedo tener un IF anidado en otro if, debe cumplir las dos condiciones de ambos if, si no cumple la primer condición del if salta y va hacia el último else
name = "John"
last_name = "Carter"

if name == "John":
    if last_name == "Carter":
        print('Yu eres John Carter')
    else:
        print('Tu no eres John Carter')
else:
    print('Tu no eres John')

# OPERADORES LÓGICOS: AND, OR, NOT

# Para que AND sea TRUE, ambas condiciones deben cumplirse (ser True).
# Si quiero saber si un número está entre 2 y 10
x = 3
if x > 2 and x < 10:
    print ('x es mayor a dos y menor a 10')

# Para que OR sea True basta que una de las condiciones se cumplan

# El operador NOT cambia el valor booleano, si es True pasa a False, y vice versa.



