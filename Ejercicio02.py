###Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
Numero_dividendo = float (input('introduzca el dividendo'))
Numero_Divisor = float (input('introduzca el divisor'))
Resultado = Numero_dividendo // Numero_Divisor
if Numero_Divisor > 0 :
    print (Resultado)
elif Numero_Divisor == 0 :
    print ('error')