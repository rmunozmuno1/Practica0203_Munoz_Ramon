### Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y Slytheryn por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
Nombre = input('¿Cual es tu nombre?')
Sexo = input('Introduzca su sexo')
if (Sexo == 'm' and Nombre[0] < 'm') or (Sexo == 'h' and Nombre[0] > 'n') :
    print ('Felicidades el sombrero seleccionador a elegido Gryffindor')
else :
    print ('Felicidades el sombrero seleccionador a elegido Slytherin')
    

