""" 
3. Aplicar el IVA al precio de un producto.
"""

IVA = 0.15
precio = 0
precio_con_iva = 0

precio = float(input("Digite el precio del producto: "))
precio_con_iva = (precio * IVA) + precio
precio_con_iva = print("El precio del producto con IVA incluido es C$", precio_con_iva)
