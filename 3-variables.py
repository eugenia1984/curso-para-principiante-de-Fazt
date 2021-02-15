# VARIABLE: nombre simbólico para un valor (puede ser cualquiertipo de dato), que se asigna mediante un =.
# Son case sensitive, tener cuidado con las mayúsculas y las minúsculas.
# Para nombrarla sse usan [a-z] , [A-Z] y _ . No pueden empezar con número, si puede tener un número entre medio o al final.

name = 'Juan'  # guardo la variable
print(name)   # llamo a la variable y la imprimo con print()

x = 100 # guardo un inter en una variable

# Las puedo definir todas a la vez
a, b, c = 100, 'Hola', 10.5
print(a, b, c)

# CONVENCIONES: 
# SNAKE CASE: Se separan con _ . Por ejemplo nombre_de_variable.
# CAMEL CASE: la primer palabra toda en minúscula y las que siguen con la primer letra en mayúscula. Ejemplo: camelCase
# PASCAR CASE: todas las palabras con la primer letra en mayúscula. Ejemplo: PascalCase.

# CONSTANTES : para los valores que no cambian, se escribe todo en mayúscula.
PI = 3.1416
MY_NAME = 'Juan'  # Porque mi nombre no va a cambiar

# Python es un lenguaje dinámico, puedo reasignar valor a una misma variable
e = 10
print(e)   # 10
e = 20
print(e)   #20


