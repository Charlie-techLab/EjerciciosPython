"""
10. Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique 
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda 
después del retiro.
"""

saldo_inicial = 1000
numero_cuenta = int(input("Ingrese el número de su cuenta bancaria: "))

if(numero_cuenta == 1234567):
    print("Usted ha ingresado de manera exitosa a su cuenta :D")
    monto_retiro = float(input("¿Cuánto dinero desea retirar de su cuenta bancaria? "))
    if(monto_retiro > saldo_inicial):
        print(f"Usted no puede realizar un retiro de C${monto_retiro} debido a que su saldo es de C${saldo_inicial}")
    elif(monto_retiro < saldo_inicial):
            saldo_actual = saldo_inicial - monto_retiro
            print(f"Su nuevo saldo es de C${saldo_actual}")
else:
    print("Error. Por favor asegúrese de ingresar un número de cuenta válido.")






