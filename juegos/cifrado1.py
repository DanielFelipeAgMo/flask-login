'''def David(a, b):
    return (a + b)

a = int(input('Ingrese el 1er numero: '))
b = int(input('Ahora el 2do numero: '))

print(f'La suma de {a} y {b} es {David(a, b)}')

'''#ordenar los elementos
'''print ("Lista ordenada")
so = ['windows','linux','mac', 'solaris', 'bsd','unix']
so.sort()
so.reverse()
print (so)'''






shift = 3  # definimos el numero de posiciones que queremos desplazar las letras

text = "JUAN"

encryption = ""

for c in text:

    # para este algoritmo está aplicado el verificar que las letras sean mayúsculas
    if c.isupper():

        # calculando la posición en un rango de  0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # esta operacion realiza el desplazamiento de forma positiva utilizando el modulo
        new_index = (c_index + shift) % 26

        # convirtiendo el caracter original al nuevo utilizando el desplazamiento
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # esta parte reemplaza cada una de las letras ingresadas por su nuevo valor
        encryption = encryption + new_character

    else:

        # esta condición permite guardar el caracter si no es mayuscula
        encryption += c

print("El texto a encriptar es:", text)

print("El texto encriptado ahora es:", encryption)