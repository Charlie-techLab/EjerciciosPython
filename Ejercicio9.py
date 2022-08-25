"""
9. Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio. 
Evaluar si es apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85 
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a 
95.
"""

nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese sus apellidos: ")
carrera = input("Ingrese el nombre de la carrera que está cursando: ")
promedio = float(input("Ingrese su promedio: "))

if(promedio > 85) and (carrera != "Ingeniería de Sistemas"):
    print(f"El estudiante {nombre} {apellidos} que estudia la carrera de {carrera} puede aplicar a una beca.")
elif(promedio > 95) and (carrera == "Ingeniería de Sistemas"):
    print(f"El estudiante {nombre} {apellidos} que estudia la carrera de {carrera} puede aplicar a una beca.")
else:
    print(f"El estudiante {nombre} {apellidos} que estudia la carrera de {carrera} no puede aplicar a una beca.") 