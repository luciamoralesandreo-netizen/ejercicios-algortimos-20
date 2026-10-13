#ALGORITMO SIGNO DE UN NUMERO
#Entradas: un número
#Salidas: signo de ese número
#Recibir un numero
#si n < 0:
  #devolver n es negativo 
#si no si n > 0:
  #devolver n es positivo 
#si no si n = 0 
  #devolver n es cero
  
def signo_numero(n):
    if n > 0:
        return(n, "es positivo")
    if n < 0:
        return(n, "es negativo")
    if n == 0:
        return(n, "es cero")
print(signo_numero(-1))
print(signo_numero(0))
print(signo_numero(1))




#ALGORITMO AÑO BISIESTO
#Entradas: año
#Salidas: resultado de si es bisiesto
#Recibir un numero
#si el resto de ese año entre 400 = 0 
 #TRUE
#si el resto de ese año entre 100 = 0 
 #False
#si el resto de ese año entre 4 = 0 
 #TRUE
 
def es_bisiesto(año):
    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 4 == 0:
        return True
    else:
        return False
print(es_bisiesto(2026))
print(es_bisiesto(2024))




#ALGORTIMO EL MAYOR DE TRES NUMEROS
#Entradas: 3 numeros (a, b, c)
#Salidas: un solo numero, el mayor 
#Recibe 3 numero
#si a > b & a > c
 #return a es el mayor 
#si b > a & b > c
 #return c b es el mayor 
# si pasa otra cosa entonces 
 # return c es mayor 
 
def mayor_numero(a, b,c):
    if a > b and a > c:
        return(a, "es el mayor de los tres")
    elif b > a and b > c:
        return(b, "es el mayor de los tres")
    else: 
        return(c, " es el mayor de los tres")
print( mayor_numero(1, 4, 8))
print(mayor_numero(0, -1, 6))




#AlGORITMO PESO Y ENVÍO
#Entradas: un peso 
#Salidas: categoria 
#Recibe un numero 
#si numero < 1 
 #devuelve sobre
# si numero > 1 y numero < 5
 #devuelve paquete pequeño
#si numero > 5 y numero <20 
 #devuelve paqeute grande 
#si numero > 20 
 #devuelve voluminoso 
 
def categoria_envio(peso):
     if peso <=1:
         return "es un sobre"
     elif peso > 1 and peso <= 5:
         return "es un paquete pequeño"
     elif peso > 5 and  peso<= 20:
         return "es un paquete grande"
     else: 
         return "es un paquete voluminoso"
print(categoria_envio(100))
print(categoria_envio(7))
print(categoria_envio(1))




#ALGORITMO SUMA DE PARES
#Entradas: un numero (n)
#Salidas: suma de los pares entre 1 y ese numeero
#Recibe un numero (n)
#suma = 0 
#para numero desde 1 hasta n
 #si el resto de dividir numero entre 2 = 0 
 #suma = suma + numero
 #devolver suma

def suma_pares(n):
    suma = 0
    for numero in range(1, n+1): #si no pongo n +1 entonces no va sumando los numeros pares hasta llegar al n 
        if numero %2 == 0:
            suma = suma + numero 
    return suma
print(suma_pares(6))
print(suma_pares(3))




#ALGORTIMO FACTORIAL 
#Entradas: un numero (n)
#Salidas: su factorial 
#Recibe un numero (n)
#resultado = 1
#para numero desde el 1 al n hacer
 #resultado= resultado * numero
 #devolver resultado 

def factoriales(n):
    resultado = 1
    for numero in range (1, n+1): #aqui pasa lo mismo que en el de antes, sino pongo n + 1 no recorre todos los numeros hasta llegar a n 
        resultado= resultado * numero
    return resultado
print(factoriales(3))
print(factoriales(4))




#ALGORITMO CONTAR VOCALES 
#Entradas: palabra
#Salidas: numero (suma de la cantidad de vocales que hay en esa palabra)
#Recibe una palabra
#vocales= 0 
#para letra en palabra
 #si la letra esta en aeiou
 #vocales = vocales +1
 #devolver vocales

def contar_vocales(palabra):
    vocales = 0 
    for letra in palabra:
        if letra in "aeiou":
            vocales= vocales + 1
    return vocales
print(contar_vocales("programacion"))
print(contar_vocales("qtd"))




#ALGORITMO TABLA DE MULTIPLICAR 
#Entradas: un numero 
#Salidas: la tabla de multiplicar de ese numero 
#Recibe un numero 
#numero = 1
#para i en el rango del 1 hasta el 10
 # multiplica = numero * i 
 # devuelve i * numero = multiplica

def tabla_multiplicar(numero): 
    for i in range(1, 11):  #pongo el 11 pq el ultimo numero no lo incluye
        resultado = numero * i
        print(numero,  "x",   i,  "=", resultado)
print(tabla_multiplicar(2))




#ALGORITMO PROMEDIO NUNMEROS
#Entradas: lista 
#Salidas: promedio
#Recibe una lista
#suma los numeros de esa lista
#cuenta la cantidad de numeros de la lista
#suma/ cantidad 
#devuleve promedio

def promedio_numeros(lista):
    total= sum(lista)
    cantidad= len(lista)
    promedio= total/cantidad 
    return promedio
print(promedio_numeros([1,2,3]))




#ALGORITMO TEXTO EN MAYUSCULAS Y NUMERO DE PALABRAS
#Entradas: frase
#Salidas: frase en mayuscula y recuento de palabras
#Recibe una frase 
#convertir la frase en mayuscula 
#contar las palabras 
#devulve la frase en mayusculas y recuento 

def mayusculas_recuento(frase):
    mayusculas= frase.upper()
    recuento= len(frase.split()) #si no pongo split no puede hacer de la frase una lista con las palabras separadas
    return mayusculas , recuento
print(mayusculas_recuento("hola mi nombre es lucia"))




#ALGORITMO VALIDAR CONSTRASEÑA 
#Entradas: contraseña 
#Salidas: booleano 
#Recibe una contraseña 
#establecer parametro
#si la longitud de la contrasdeña es <8
 #devuelva false

def contraseña(contraseña):
    if len(contraseña)<= 8:
        return False
    else:
        return True
print(contraseña("holacaracola"))




#ALGOTIRMO CONVERSION TEMPERATURA
#Entradas: grados (numero)
#Salidas: la conversion de esos grados 
#Recibe un numero (temperatura en celsius)
#multiplicar el numero por 9, divirlo entre 5 y sumar 33
#devuleve el numero 

def celsius_fahrenheit(celsius):
    fahrenheit= celsius*9 /5 +32
    return fahrenheit
print(celsius_fahrenheit(25))


#Entradas: grados (numero)
#Salidas: la conversion de esos grados 
#Recibe un numero (temperatura en fahrenheit)
#restar 32 al numero, multiplicarlo por 5 y luego dividir entre 9
#devuelve el numero

def fahrenheit_celsius(fahrenheit):
    celsius= (fahrenheit-32)*5 /9
    return celsius
print(fahrenheit_celsius(77))




#ALGORITMO FACTORIAL RECURSIVO
#Entradas:un numero
#Salidas: factorial 
#Recibir un numero
#si el numero es = 0
 #devolver 1 
#si el numero es distinto es distinto de 0 
 #devolver el numero * factorial recursivo 

def factorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero *factorial_recursivo(numero-1)
print(factorial_recursivo(5)) #No se lo que es un factorial recursivo, lo he hecho ayudandome de la IA porfa si lo puedes explicar en clase 




#ALGORITMO SUCESION FIBONACCI
#Entradas: un numero 
#Salidas: otro numero 
#Recibe un numero 
#si ese numero es igual a 0 
 #devolver 0 
#si ese numero es igual a 1
 #devolver 1 
#sino 
 #devolver fibonacci(numero-1) + fibonacci(numero -2)

def sucesion_fibonacci(numero): #suma los dos numeros anteriores del numero recibido
    if numero == 0:
        return 0 
    elif numero == 1:
        return 1
    else:
        return sucesion_fibonacci(numero-1) + sucesion_fibonacci(numero-2)
print(sucesion_fibonacci(6))




#ALGORITMO SUMA RECURSIVA DE UNA LISTA 
#Entradas: una lista 
#Salidas: numero (suma de la lista)
#Recibe una lista 
#suma lso numeros de la lista 
#devuelve la lista sumada

def suma_lista(lista):
    if len(lista) == 0:
        return 0 
    suma= lista[0] +suma_lista(lista[1: ])
    return suma 
print(suma_lista([1, 2, 3]))
    
    
    
    
#ALGORITMO INVERTIR UN TEXTO 
#Entradas: una frase 
#Salidas: la frase invertida
#Recibe una frase
#si la frase tiene menos de un caracter 
 #devuelve la frase
#sino 
 #invierte la frase
 
def invertir_frase(frase):
    if len(frase)<=1:
        return frase
    else: 
        return invertir_frase(frase[1:]) + frase[0]
print(invertir_frase("hola que tal"))    




#ALGORITMO DIVISION
#Entradaas: dos numeros
#Salidas: su division 
#Recibe dos numeros
#intenta dividirlos 
#si sale erorr 
 #devuelve error division entre 0

def division_segura(a,b):
    try:
        return a/b
    except ZeroDivisionError: 
        return "Error: division entre cero"
print(division_segura(4,2))
print(division_segura(2, 0))




#ALGORITMO CONVERTIR TEXTO A UN NUMERO 
#Entradas: texto 
#Salidas: un numero 
#Recibe un texto 
#intentarlo (pero si es texto)
 #delvuelve error 
#si es numero
 #devuelve el entero

def texto_numero(texto):
    try:
        numero= int(texto)
        return numero
    except ValueError:
        return "Error: no es un numero"
print(texto_numero("hola"))
print(texto_numero(12))




#ALGORITMO ACCESO A UNA LISTA 
#Entradas: una lista 
#Salidas: una posicion de la lista 
#intentarlo 
 #devolver posicion
#si la posicion no existe 
 #devuelve error 

def posicion_lista(lista, posicion): 
    try: 
        return(lista[posicion])
    except IndexError:
        return "Error: posicion no encontrada"
print(posicion_lista([1, 2, 3], 2))
print(posicion_lista([1, 2, 3], 6))




#ALGORITMO CALCULADORA ERRORES
#Entrada: 3 textos 
#Salida: operacion
#Recibe 3 numeros/texto 
#lo intenta 
#si operacion = suma 
 #devolver la suma a+b
#si operacion = division
 #devolver division a/b
#sino 
 #devolver error 

def calculadora(a, b, operacion):
    try:
        a=float(a)
        b=float(b)
        if operacion == "suma":
            return a+b
        elif operacion == "division":
            return a/b
        else: 
            return "Error: operación no valida"
    except ZeroDivisionError: 
        return "Error: no se puede dividir entre 0"
print(calculadora(2,0, "division"))
print(calculadora(2,2, "division"))
print(calculadora(2,2, "suma"))
    
