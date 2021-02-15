# MODULO (BIBLIOTECA): códigoescrito y ya testeado, para reutilizar al descargar el módulo. 
# Están nuestros propios módulos, los que bajas de internet y los de Python.

# Módulos preconstruidos (los da Python), vemos el ejemplo de datetime
import datetime 
# Para ver el día actual
print(datetime.date.today())
# Para convertir los minutos en horas( y minutos)
print(datetime.timedelta(minutes=70))

# Otra forma de importarlo sin tener que escribir datetime

# from datetime import timedelta
# print(timedelta(minutes=70))

# from datetime import timedelta, date
# print(date.today())

# Para  crear mi propio módulo, quiero crear una función para sumar y otra para restar, que están en el archivo fmath.py

import fmath
fmath.add(1,2)
fmath.substract(1, 2)

# from fmath import add, substract
# add(1,2)
# substract (1, 2)

# Cómo usar módulos de terceros? En la web pypi.org, y buscamos por ejemplo el módulo colorama, en la termina : pip install colorama, y ya lo puedo usar
from colorama  import Fore, Style
#  init(convert=True)  # si en la consola no se ve a color, se agrega
print(Fore.RED + 'Hola mundo')
# y veo Hola mundo en rojo

# Flash y Django(es un framework) son las más usadas







