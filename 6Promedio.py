promedio = 0.0
while promedio < 9.5:
    calif1 = float(input("Ingresa tu primer calificacion: "))
    calif2 = float(input("Ingresa tu segunda calificacion: "))
    calif3 = float(input("Ingresa tu tercera calificacion: "))
    calif4 = float(input("Ingresa tu cuarta calificacion: "))
    calif5 = float(input("Ingresa tu quinta calificacion: "))
    promedio = (calif1 + calif2 + calif3 + calif4 + calif5)/5
    if promedio >= 9.5:
        print("Tu promedio es : ", str(promedio),"\nTienes una calificacion EGGCELENT!!!")
    else:
        print("Tu promedio fue de ", str(promedio), "\nEsfuerzate mas a la proxima")