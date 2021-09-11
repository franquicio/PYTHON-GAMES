import random

numero_de_intentos = 0
numero_minimo = 1
numero_maximo = 100
nombre_usuario = input("Ingrese su nombre: ")


numero_generado = random.randint(numero_minimo, numero_maximo)

print("Hola " + str(nombre_usuario) + " tienes que adivinar mi número, el cual puede ser del " + str(numero_minimo) + " al " + str(numero_maximo))


while numero_de_intentos < 5:
    print("Adivina: ")
    numero_adivinado = int(input())

    numero_de_intentos = numero_de_intentos + 1

    if numero_adivinado == 0:
        print("No lo lograste a pesar de tratar "+ str(numero_de_intentos) + " veces. Más suerte para otra vez")
        break
    if int(numero_generado - numero_adivinado) < 5:
        print("Estás a una distancia menor que 5")
    if int(numero_generado-numero_adivinado) in range(5, 10):
        print("Estás a una distancia mayor que 5 y menor que 10")
    if int(numero_generado - numero_adivinado) in range(10,20):
        print("Estas a una distancia mayor que 10 y menor que 20")
    if int(numero_generado - numero_adivinado) > 20:
        print("Estas a una distancia mayor que 20")
    if numero_adivinado == numero_generado:
        break
    
    
if  numero_adivinado == numero_generado:
    numero_de_intentos = str(numero_de_intentos)
    print("Ganaste " + nombre_usuario + " en " + numero_de_intentos + " intentos." )

if numero_adivinado != numero_generado:
    print("Has perdido, el número era: " + str(numero_generado))
