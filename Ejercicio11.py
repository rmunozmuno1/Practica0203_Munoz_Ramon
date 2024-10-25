###Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = input('Introduce una palabra')
print('Las letras de la palabra en orden inverso son')
for letra in palabra[::-1]:  
    print(letra)