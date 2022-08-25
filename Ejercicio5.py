"""
5. Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
enteros.
"""

valor_inicial = 0
valor_final = 0
numero_par = 0
valor_inicial = int(input("Digite el valor inicial: "))
valor_final = int(input("Digite el valor final: "))

print(f"Los números pares entre el número {valor_inicial}  y el número {valor_final} son:", end = " ")
for valor in range(valor_inicial, valor_final+1):
    if valor%2 == 0:
        print(valor,"-", end = " ")
        
