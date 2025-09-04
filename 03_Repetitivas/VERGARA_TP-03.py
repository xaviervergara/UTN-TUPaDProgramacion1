# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero_usuario = input("Ingrese un numero")
# print(len(numero_usuario)) ---> Metodo mas rapido

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