"""
1. Mostrar el total a pagar por la compra de n cantidad de productos a un precio 
desconocido.
 """

total = 0
precio = 0

cantidad_productos = int(input("Digite la cantidad de productos que va a comprar: "))

for precio in range(cantidad_productos):
    print(precio+1, ".Ingrese el precio del producto: ", end = " ")
    precio = float(input("C$"))
    total += precio

print("El total a pagar es C$", end = " ")
print(total)



