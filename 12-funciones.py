# FUNCIONES: porción de código que hace algo y nos puedo o no devolver algo.

# Ya fuimos utilizando las siguientes funciones que ya vienen predefinidas: print(), dir(), type()

# Ejemplo defunción:

# La creo:
def hello():
    print('Buen día')
# Llamo a la función:
hello()

# Función con parámetro, le asignamos un valor dentro de la función
def hello(name=',cómo estás?'): # si no le ingreso ningñun valor, me vaa mostrar Buen día, cómo estas?
    print('Buen día ' + name)
hello('Ana')

# Función de suma:
def suma (num1, num2):
    return num1 + num2
print(suma(10, 20))

# Función lambda
suma = lambda num1, num2: num1 + num 2
print(suma(15, 28))