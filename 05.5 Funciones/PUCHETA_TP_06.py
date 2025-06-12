import math
#TP FUNCIONES

#1) Crear una función llamada imprimir_hola_mundo que imprima por
 #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 #programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

#2) Crear una función llamada saludar_usuario(nombre) que reciba
 #como parámetro un nombre y devuelva un saludo personalizado.
 #Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)

print(saludo)


#3)  Crear una función llamada informacion_personal(nombre, apellido,
 #edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 #[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
 # Pedir los datos al usuario y llamar a esta función con los valores ingresados. 

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del ciruclo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")


#5) Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas")


#6) Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}: ")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#7) Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida(No se puede dividir por 0)"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print("\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


#8)  Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales

def calculcar_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calculcar_imc(peso, altura)

print(f"Su IMC es: {imc:.2f}")


#9)  Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_farenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
farenheit = celsius_a_farenheit(celsius)

print(f"{celsius}°C equivalen a {farenheit:.2f}°F")

#10) Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c / 3)

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))
c = float(input("Ingrese el tercer valor: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de los numeros es: {promedio:.2f}")


