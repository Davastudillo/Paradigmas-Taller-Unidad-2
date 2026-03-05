#DATOS A USAR. 

listal = [1,2,3] 
lista2 = [4,5,6] 
lista3 = [7,8,9] 

#OPERACION CON "map()" Y "lambda". 
resultado = map(lambda x, y, z: x + y + z, listal, lista2, lista3) 

print(list(resultado))

"""
Analisis ejercicio 10:

a) Resultado: [12, 15, 18]

b) Analisis del codigo:
Inicialmente se declaran e inicializan las variables lista1, lista2, lista3 con sus respectivos valores

Luego se realiza el calculo, la función lambda x, y, z: x + y + z es una función matemática anónima, en este caso su proposito es recibir 3 números y sumarlos.

La función map() se encarga de ejecutar la función lambda tomando un número de cada lista al mismo tiempo, lo hace en tres iteraciones:

Posición 0: Toma el 1, 4 y 7 => suma = 12 
Posición 1: Toma el 2, 5 y 8 => suma = 15
Posición 2: Toma el 3, 6 y 9 => suma = 18

La función list() en este caso sirve para ejecutar las sumas y agrupar los resultados en una lista visible: [12, 15, 18]

"""