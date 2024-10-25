###Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
Edad = int(input('¿Cual es tu edad?'))
if Edad <= 16 :
    print ('Felicidades no tienes que tributar')
elif Edad > 16 :
    ingresos = float(input('Cuales son tus'))
    if ingresos > 1000 :
        print ('Vaya putada tienes que tributar')
    else : 
        print ('Felicidades no tributas')


