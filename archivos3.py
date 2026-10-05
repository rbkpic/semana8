#crear y gyardar un archivo

frase=input("Dime tu frase favorita: ")

with open("frase.txt", "w") as archivo: #la doble w lo que hace es que guarda la informacion y crea un archivo, pero al volver a ejecutar, cambia la informacion del archivo previamente creado
    archivo.write(frase)

print("Archivo creado satisfactoriamente.")