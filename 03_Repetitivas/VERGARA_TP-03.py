# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero_usuario = input("Ingrese un numero")
# No casteo el input a tipo num, entonces queda como un string, el cual si es iterable
# esto permite recorrerlo con un for in.

i = 0
digito = 0
for i in numero_usuario:
    digito += 1
print(digito)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num_1 = int(input("Ingrese el primer numero"))
num_2 = int(input("Ingrese el segundo numero"))
acc = 0

if num_1 >= num_2:
    print("El segundo numero debe ser el mas grande")
else:
    for i in range((num_1 + 1), num_2):
        acc = acc + i
    print(acc)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

acc = 0
a = int(input("Ingrese un numero"))

while a != 0:
    acc += a
    a = int(input("Ingrese un numero"))
print(acc)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final,
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

flag = True
n_intentos = 0
numero_aleatorio = random.randint(0, 9) # Tambien podria poner esta linea dentro del bucle, para aumentar la dificultad.

while flag:
  numero_usuario = int(input("Ingrese un numero"))
  n_intentos += 1
  if numero_usuario == numero_aleatorio:
    flag = False
print(f"Ha adivinado el numero!\nNumero de intentos: {n_intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

# Como no aclara que si hay que incluir extremos lo escribí asi:

for i in range(98, 0, -2):
    print(i)

# Este es auxiliar, con extremos incluidos
# for i in range(100, -2, -2):
#     print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

numero_usuario = int(input("Ingrese un numero"))
acc = 0
# tampoco dejamos ingresar ceros, para que se pueda realizar la operacion
if numero_usuario <= 0:
    print("Ingrese un numero positivo distinto de cero, para poder realizar la operación")
else:
 for i in range(0, numero_usuario):
    acc = acc + i
 print(f"Suma: {acc}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio)

pares = 0
impares = 0
positivos = 0
negativos = 0
 
for i in range(2):
    numero_usuario =  int(input("Ingrese numero"))   
    if numero_usuario % 2 == 0:
      pares += 1
    else: impares += 1
    if numero_usuario > 0:
        positivos += 1
    else: negativos += 1
         
print(f"Pares: {pares}\nImpares: {impares}\nPositivos: {positivos}\nNegativos: {negativos}\n")  

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

contador = 0
acc = 0

for i in range(100):
    numero_usuario = int(input("Ingrese un numero"))
    acc = acc + numero_usuario
    contador += 1
print(f"La media de los valores ingresados es: {acc / contador}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

import math
numero_usuario = int(input("Ingrese un numero"))
numero_invertido = ''

if numero_usuario > 0:
    while numero_usuario > 0:
        ultimo_digito = numero_usuario % 10
        numero_usuario = int(numero_usuario / 10)
        numero_invertido += str(ultimo_digito)
    print(numero_invertido)
else:
    print("Solo valores positivos")   