#TP 7 RECURSIVIDAD

#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #Recursividad
    
num = int(input("Ingrese un numero: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} es {factorial(i)}")


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 

# Funcion recursiva 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


pos = int(input("Ingresa hasta que posicion queres ver la serie de Fibonacci: "))

# Mostramos la serie completa hasta esa posicion
print("Serie de Fibonacci: ")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print("\n")
print("*" * 30)

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente -1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)

print(f"{base}^{exponente} = {resultado}")


#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
#unos (1), en base 2. 


def decimal_a_binario(n):
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresá un número entero positivo en decimal: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es {binario}")



#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 


def es_palindromo(palabra):
    # si la palabra tiene 0 o 1 caracter es palíndromo
    if len(palabra) <= 1:
        return True
    # Compara la primera y ultima letra
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


texto = input("Ingresa una palabra sin espacios ni tildes: ").lower()
print(es_palindromo(texto))


#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 

def suma_digitos(n):
    # si el número tiene un solo digito se devuelve ese dígito
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingresá un número entero positivo: "))
print(f"La suma de sus dígitos es: {suma_digitos(numero)}")


#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque.  
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 

def contar_bloques(n):
    # si queda 1 nivel solo hay 1 bloque
    if n == 1:
        return 1
    # bloques en nivel actual + bloques en niveles superiores
    return n + contar_bloques(n - 1)

nivel_bajo = int(input("Ingresá la cantidad de bloques en el nivel más bajo: "))
total = contar_bloques(nivel_bajo)
print(f"El total de bloques para construir la pirámide es: {total}")


#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 

def contar_digito(numero, digito):
    # si el número es 0
    if numero == 0:
        return 0
    # Cuenta 1 si el último dígito es igual al que se busca sino 0
    cuenta_actual = 1 if (numero % 10) == digito else 0
    # recursion
    return cuenta_actual + contar_digito(numero // 10, digito)


num = int(input("Ingresa un número entero positivo: "))
dig = int(input("Ingresa un dígito (0-9) para buscar: "))
print(f"El digito {dig} aparece {contar_digito(num, dig)} veces en el número {num}.")
