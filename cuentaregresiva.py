import time

numero = 30 #tienes 30 segundos 

for i in range(numero):
    print(numero)
    time.sleep(1) #el numero adentro de sleep es la cantidad de segundos de la cuenta regresiva
    numero -= 1
    if (numero==0):
        print("Se acabó el tiempo")



