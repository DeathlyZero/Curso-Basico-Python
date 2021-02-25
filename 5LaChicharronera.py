print("Este metodo calcula de a como tu chicharron ")
a = int(input("Dame el valor de a: "))
b = int(input("Dame el valor de b: "))
c = int(input("Dame el valor de c: "))

chicharron1 = ((-b) + ((b*b)-(4*a*c))**0.5)/(2*a)
chicharron2 = ((-b) - ((b**2)-(4*a*c))**0.5)/(2*a)

print("El chicharron1 cuesta: ", str(chicharron1))
print("El chicharron2 cuesta: ", str(chicharron2))