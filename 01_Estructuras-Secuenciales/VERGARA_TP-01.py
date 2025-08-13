# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 

nombre = input("Ingrese su nombre")
print(f"Hola {nombre}")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = int(input("Ingrese su edad"))
residencia = input("Ingrese su lugar de residecia")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math

radio = int(input("Ingrese radio"))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"Area del cirulo: {area}\nPerimetro del circulo: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos"))

horas_equivalentes = round(segundos / 3600, 2) #round para redondear los decimales a n, en este caso elegí 2 decimales

print(f"La cantidad de segundos ingresada equivale a {horas_equivalentes} hora/s")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = int(input("Ingrese un numero"))

print(f"""
{num} * 1 = {num * 1}\n
{num} * 2 = {num * 2}\n
{num} * 3 = {num * 3}\n
{num} * 4 = {num * 4}\n
{num} * 5 = {num * 5}\n
{num} * 6 = {num * 6}\n
{num} * 7 = {num * 7}\n
{num} * 8 = {num * 8}\n
{num} * 9 = {num * 9}\n
{num} * 10 = {num * 10}\n
""")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num_1 = int(input("Ingrese primer numero distinto de cero")) # No hemos visto condicionales asique no compruebo el caso != 0
num_2 = int(input("Ingrese primer numero distinto de cero"))

print(f"""
Suma: {num_1 + num_2}
Division: {num_1 / num_2}
Multiplicacion: {num_1 * num_2}
Resta: {num_1 - num_2}
""")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

altura = float(input("Ingrese su altura"))
peso = float(input("Ingrese su peso"))

imc = peso / (altura ** 2)

print(f"Su indice de masa corporal: {round(imc, 2)}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Ingrese grados Celsius"))

farenheit = 9 / 5 * celsius + 32

print(f"Equivalente en Farenheit: {round(farenheit, 2)}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num_1 = int(input("Ingrese el primer numero"))
num_2 = int(input("Ingrese el segundo numero"))
num_3 = int(input("Ingrese el tercer numero"))

promedio = (num_1 + num_2 + num_3) / 3

print(f"Promedio de los numeros ingresados: {round(promedio, 2)}")