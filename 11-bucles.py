comida = ["manzana", "pan", "queso", "leche"]
print(comida[0])
print(comida[2])

# BUCLE
for food in comida:
    if food == "queso":
        print('Tienes que comprar queso')
    print(food)

for food in comida:
    if food == "pan":
        break
    print(food)
# finaliza en pan

# No me va a mostrar el valor pan
for food in comida:
    if food == "pan":
        continue
    print(food)

# Para recorrer un rango
for number in range(1, 8):
    print(number)

# Puedo recorrer un string
for letter in 'Hello':
    print(letter)

# WHILE: debe tener un incremento o decremento en count, sino tenemos un bucle infinito
count = 4
while count <= 10:
    print(count)
    count +=1  # aumenta de 1 a 1 en cada ciclo
