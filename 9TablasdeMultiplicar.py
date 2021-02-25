tabla = 1
aux = 1
print("Tabla del ", tabla)
while tabla <= 10:
    print(tabla, "x", aux, "=", (tabla*aux))
    aux = aux + 1
    if aux > 10:
        tabla = tabla + 1
        print("Tabla del ", tabla)
        aux = 1
