### Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
altura = int(input('Introduzca un numero entero'))
for i in range(1, altura + 1): ### He buscado como usar el for ya que no lo entendeia muy bien
    print("*" * i)
