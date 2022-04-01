#Nuestra primera funcion
def songs():
    print("No te pares frente a mi")
    print("Con esa mirada tan hiriente")

songs()

print(type (songs))

#Las funciones se pueden usar tambien  dentro de otras funciones
def chorus():
    songs()
    songs()

chorus()

