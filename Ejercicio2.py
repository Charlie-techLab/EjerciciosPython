""" 
2. Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
estudiante de manera individual, escriba un código en Python que permita crear un correo 
electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
“@est.uca.edu.ni”

"""

primer_nombre = input("Escribe tu primer nombre: ")
segundo_nombre = input("Escribe tu segundo nombre: ")
primer_apellido = input("Escribe tu primer apellido: ")
segundo_apellido = input("Escribe tu segundo apellido: ")

print(f'Tu correo electrónico asignado es: {primer_nombre.lower()}.{primer_apellido.lower()}@est.uca.edu.ni')