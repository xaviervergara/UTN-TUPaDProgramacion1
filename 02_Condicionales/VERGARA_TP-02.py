# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_usuario = int(input("Ingrese su edad"))

if edad_usuario > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota_usuario = int(input("Ingrese su nota"))

if nota_usuario >= 6:
    print("Aprobado")
else: print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un numero par"))

if num % 2 == 0:
    print("Ha ingresado un número par")
else: print("Por favor, ingrese un número par")    

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad_usuario = int(input("Ingrese su edad"))

if edad_usuario < 12:
    print("Niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Adolescente")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Adulto/a joven")
else: 
    print("Adulto/a") #Podria hacer un elif y evaluar la condicion edad_usuario >= 30, pero en este caso particular el else funciona igual y me ahorro una evaluacion.

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

contrasena_usuario = str(input("Introduzca su contraseña: debe tener entre 8 y 14 caracteres")) #conversión a type string por si se ingresan numeros
longitud_contrasena = len(contrasena_usuario)

if 8 <= longitud_contrasena <= 14:
    print("Ha ingresado una contrseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")    

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario,
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabras_usuario = input("Ingrese una palabra o frase")

ultima_letra = palabras_usuario[-1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{palabras_usuario}!")
else:
    print(palabras_usuario)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

nombre_usuario = input("Ingrese su nombre")
opcion_numerica = int(input("Ingrese un numero del 1 al 3"))

match opcion_numerica:
  case 1:
    print(nombre_usuario.upper())
  case 2:
    print(nombre_usuario.lower())
  case 3:
    print(f"{nombre_usuario[0].upper()}{nombre_usuario[1:]}")
  case _:
    print("Error: debe ingresar un numero entre 1 y 3")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según la escala 
# de Richter e imprima el resultado por pantalla:

magnitud_usuario = float(input("Ingrese la magnitud del terremoto"))

print(magnitud_usuario)

if magnitud_usuario < 3:
    print("Muy leve (Imperceptible)")
elif 3 <= magnitud_usuario < 4:
    print("Leve (Ligeramente perceptible)")    
elif 4 <= magnitud_usuario < 5:
    print("Moderado (Sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_usuario < 6:
    print("Fuerte (Puede causar daños en estructuras débiles)")
elif 6 <= magnitud_usuario < 7:
    print("Muy fuerte (Puede causar daños significativos)")
elif magnitud_usuario >= 7:
    print("Extremo (Puede causar graves daños a gran escala)")
    
# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio_usuario = input("Ingrese el hemisferio donde se encuentra: N/S").lower()
mes_usuario = int(input("Ingrese el mes actual en formato numerico"))
dia_usuario = int(input("Ingrese el día actual en formato numerico"))

periodo_1 = ((mes_usuario == 12 and dia_usuario >= 21) or mes_usuario == 1 or mes_usuario == 2 or (mes_usuario == 3 and dia_usuario <= 20))     # 21 dic hasta 20 marzo
periodo_2 = ((mes_usuario == 3 and dia_usuario >= 21) or mes_usuario == 4 or mes_usuario == 5 or (mes_usuario == 6 and dia_usuario <= 20))      # 21 marzo hasta 20 jun
periodo_3 = ((mes_usuario == 6 and dia_usuario >= 21) or mes_usuario == 7 or mes_usuario == 8 or (mes_usuario == 9 and dia_usuario <= 20))      # 21 jun hasta 20 spt
periodo_4 = ((mes_usuario == 9 and dia_usuario >= 21) or mes_usuario == 10 or mes_usuario == 11 or (mes_usuario == 12 and dia_usuario <= 20))   # 21 spt hasta 20 dic

# print(periodo_4)

if periodo_1:
    if hemisferio_usuario == "n":
        print("Invierno")
    else:
        print("Verano")
elif periodo_2:
    if hemisferio_usuario == "n":
        print("Primavera")
    else:
        print("Otoño")
elif periodo_3:
    if hemisferio_usuario == "n":
        print("Verano")
    else:
        print("Invierno")
elif periodo_4:
    if hemisferio_usuario == "n":
        print("Otoño")
    else:
        print("Primavera")    