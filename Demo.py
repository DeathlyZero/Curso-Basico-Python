"""
Notas importantes:

print("")

print(f"")

print("", end="", sep="")

pyton no permite la concatenacion de una cadena y un entero por lo que debemos
convertir el entero a una cadena con el metodo:

str()

lista[]-> Solo acepta cadenas
tupla()-> Acepta cadenas y numeros

for "variable" in "lista/tupla":
    print("variable")

"variable" puede estar declarada o no, al momento de usarse se crea y adquiere un valor, en caso contrario 
recibiriamos un error

for "variable" in range(1-9)

print("Cual es tu nombre?")
nombre = input()
print("Hola", nombre)

"""
nombre = input("Cual es tu nombre?")
print("Hola", nombre)