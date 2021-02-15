my_str = 'Hola Mundo'

# print(dir(my_str))   
# dir() ves las propiedades (métodos) que le podés aplicara las string.

print(my_str.upper())   
# HOLA MUNDO con .upper() paso todo a mayúscula

print(my_str.lower())   
# hola mundo con .lower() paso todo a minúscula

print(my_str.swapcase())  
# hOLA mUNDO con swapcase() pasa de mayúscula aminúscula y vice versa.

print(my_str.capitalize())   
# Hola Mundo con capitalize() pasa a mayúscula la primer letra de laprimer palabra.

print(my_str.replace('Hola', 'Chau').upper()) 
# CHAU MUNDO ejecute dos métodos seguidos (método encadenado), primero cambio Hola por Chau con .replace() y luego paso todo a mayúscula con .upper()

print(my_str.count('l'))  
# 1 con .count() me indica cuantas veces tengo elcaracter indicado, puedo contar también el caracter vacío con .count(' ')

print(my_str.startswith('Hola'))  
# True con .startswith() corrobora si empieza con la palabra indicada entre (), su resultado es booleano: true o false.
# Compara letra por letra, puedo pedir que se fije si solo empieza con H, Ho.

print(my_str.endswith('do'))  
# True con .endswith()comparo como termina, puedo comparar toda la palabra o algunas letras

print(my_str.split())  
# ["Hola", "mundo"] puedo dividir el texto en dos variables, lo veo como una lista, los separa basado en el espacio.
# Si en vez de un espacio tengo una coma o un caracter también lo puedo hacer ( pero si indicopor letra, esa letra la quita)
print(my_str.split('o'))   
# ["H", "la Mund"]

print(my_str.find('o'))  # 1
# Devuelve la posición  ( el índice ) en el string; recordar que comienza en 0.

print(len(my_str)) # 10
# Muestra cuántoscaracteres tengo, incluyendo los espacios en blanco.

print(my_str.index('o'))  # 1
# Te da la ubicación de la letra indicada entre ().

print(my_str.isnumeric())   # False
# Corrobora si es dato numérico.

print(my_str.isalpha())   # False
# Corrobora si es dato alphanumérica.

print(my_str[0])  
# H, me muestra el valor del índice indicado.
print(my_str[-1])
# o, me muestra el último valor.

# Para imprimir dos string concatenadas

a = 'Hola'

print( a, 'a todos')
print (f"{a} a todos")  # indico entre {} cuáles la variable
print("{0} a todos".format(a))

















