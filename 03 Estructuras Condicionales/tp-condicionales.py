from statistics import mode, median, mean
import random
#TP 3 - Condicionales - Lucas Pucheta

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "));

if edad >=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad");

print("-" * 30);


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "));

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("-" * 30);

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar

numPar = int(input("Ingrese un numero par: "));

if numPar % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

print("-" * 30)

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años

edadUsu = int(input("Ingrese su edad: "));

if edadUsu < 12:
    print("Niño/a")
elif edadUsu >= 12 and edadUsu < 18:
    print("Adolescente")
elif edadUsu >= 18 and edadUsu < 30:
    print("Adulto/a joven")
elif edadUsu >= 30:
    print("Adulto/a")

print("-" * 30)


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("Ingrese su contraseña: ");

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña correcta");

print("-" * 30)


#6) Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "Distribución sin patrón claro de sesgo"

print("Lista de números aleatorios:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print("Resultado del análisis:", sesgo)


print("-" * 30)

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

texto = input("Ingrese una frase o palabra: ");


if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)


print("-" * 30)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

nomb = input("Ingrese su nombre: ")
opc = input("Elija una opcion: 1 (mayusculas), 2 (minusculas), 3 (primera letra mayuscula): ")

if opc == "1":
    print(nomb.upper())
elif opc == "2":
    print(nomb.lower())
elif opc == "3":
    print(nomb.title())
else:
    print("Opcion no valida")

print("-" * 30)


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy Leve (Imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (Ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (Sentido por personas, pero generalmente no causa daño)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (Puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte (Puede causar daños significativos)")
else:
    print("Extremo (Puede causar daños a gran escala)")

print("-" * 30)


#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 

hemisferio = input("Indique en que hemisferio se encuentra(N/S): ").upper()
mes = int(input("Ingrese que mes(1 a 12): "))
dia = int(input("Ingrese el dia del mes: "))

#Convierto la fecha a numero para que se pueda manejar mas facilmente en los ifs
fecha = mes * 100 + dia

estacion = ""

if hemisferio == "N":
    if 321 <= fecha <= 621:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Invierno"
elif hemisferio == "S":
    if 321 <= fecha <= 621:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Verano"
else:
    print("Hemisferio no valido")

print("Estas en ", estacion)


print("-" * 30)










