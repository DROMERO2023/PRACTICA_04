
# EJERCICIO 01 - PC 04 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:

# PASO 01: Leer el texto desde el archivo
with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

# PASO 02: Contar la palabra "la" en el texto leído
palabra_a_contar = "la"
contador = contenido.lower().count(palabra_a_contar.lower())
print(f'La palabra "{palabra_a_contar}" aparece {contador} veces en el texto.')

# PASO 03: Agregar texto al final del archivo
texto_nuevo = input("Ingrese texto para agregar al final del archivo: ")
with open("texto.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\n" + texto_nuevo)

print("Texto agregado exitosamente al final del archivo.")
