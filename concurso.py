import random
import time

concursantes = ["Franco", "Victoria", "Balto", "Luna"]


print("El ganador del concurso es: ")

numero = 10

for i in range(numero):
    print(numero)
    time.sleep(1)
    numero -= 1

print(random.choice(concursantes))