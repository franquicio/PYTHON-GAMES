import time
import random

numero =  30  #tienes random segundos que pueden variar entre 1 y 30 

for i in range(numero):
    print(numero)
    time.sleep(1) #el numero adentro de sleep es la cantidad de segundos de la cuenta regresiva
    numero -= random.randint(1,30)
    if (numero<=0):
        print("Se acabó el tiempo")
        break
    



