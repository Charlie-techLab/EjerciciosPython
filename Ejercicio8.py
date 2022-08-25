"""
8. Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.
"""

lista_precios = []
cantidad_precios = int(input("Digite la cantidad de precios que va a ingresar: "))

for i in range(cantidad_precios):
    precio = int(input("Ingrese el precio del producto: "))
    lista_precios.append(precio)

lista_precios.sort()
print(lista_precios)

print("El precio mayor es ", lista_precios[len(lista_precios)-1])
print("El precio menor es ", lista_precios[0])




