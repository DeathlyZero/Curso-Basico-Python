numero = int(input("Dame un numero: "))
print("El numero es: ", str(numero))
aux = 1
factorial = 1
while aux <= numero:
    factorial = (factorial*aux)
    aux = aux+1

print("El factorial es: ", str(factorial))