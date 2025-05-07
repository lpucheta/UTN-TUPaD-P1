import random
#Tp Estructuras repetitivas

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 


for i in range(0, 101):
    print(i)

print ("*" *30)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

numero = input("Ingrese un numero entero: ")

print("Cantidad de digitos: ", len(numero))

print("*" * 30)


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

inicio = min(a, b)
fin = max(a, b)

suma = 0

for i in range(inicio + 1, fin):
    suma += i  

print("La suma de todos los números entre", a, "y", b, "es", suma)


print("*" * 30)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0. 

total = 0

while True:
    numero = int(input("Ingresa un numero(0 para detener): "))

    if numero == 0:
        break
    total += numero

print("El total acumulado es: ", total)

print("*" * 30)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

numero_aleatorio = random.randint(0, 9) #Generamos numero aleatorio entre 0 y 9
intentos = 0


while True:
    adivinanza = int(input("Adivina el numero entre 0 y 9: "))

    intentos += 1 #Aumenta el contador de intentos

    if adivinanza == numero_aleatorio:
        print(f"Felicidades adivinaste el numero! {numero_aleatorio} en {intentos} intentos.")
        break #salimos del bucle cuando el usuario acierta
    else:
        print("Intentalo de nuevo")

print("*" * 30)


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 

for i in range (100, -1, -1):
    if i % 2 == 0:
        print(i)

print("*" * 30)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 

n = int(input("Ingrese un numero: "))

suma = 0

for i in range(0, n+1):
    suma += i

print("La suma entre 0 y ", n, "es ", suma)


print("*" * 30)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0


for i in range(cantidad):
    num = int(input(f"Ingrese el numero {i+1}: "))

    #Par o Impar
    if num % 2 == 0:
        pares += 1
    else:
        impares +=1

    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("\n--- Resultados ---")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)


print("*" * 30)


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 

cant = 100
suma = 0

for i in range(cant):
    num = int(input(f"Ingrese el numero {i+1}: "))
    suma += num

media = suma / cant

print("\n--- Resultado ---")
print("La media de los números ingresados es:", media)


print("*" * 30)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 


num = input("Ingrese el numero: ")

num_invertido = num[::-1] #[::-1] Esta sintaxis invierte la cadena

print("El numero invertido es: ", num_invertido)