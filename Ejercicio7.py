"""
7. Leer x cantidad de edades y mostrar el promedio de dichas edades.
"""

edades = 0
suma_edades = 0
promedio = 0


edades = int(input("Digite la cantidad de edades que va a ingresar: "))
      
for edad in range(edades):
    print(edad+1, ". Ingrese la edad de la persona: ", end = " ")
    edad = int(input())
    suma_edades += edad
    promedio = suma_edades / edades
        
    
if(edades < 1):
    print("Por favor ingrese un número que sea mayor o igual que cero")
elif(edades == 1):
    print(f"El promedio de la edad es: {promedio}")
else:
    print(f"El promedio de las edades es: {promedio}")

