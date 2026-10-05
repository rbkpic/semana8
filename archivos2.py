"""
file=open("misdatos/txt", "r")
print(file.read())
file.close
"""

with open("misdatos.txt", "r") as file:
    contenido=file.read()

print(contenido)

