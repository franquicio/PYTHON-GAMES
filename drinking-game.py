#Juego para beber, se bebe la diferencia entre la adivnanza y el numero.

import random

cartas = random.randint(1,13)

print("Selecciona una carta del 1 al 13")
pass

numero_adivinado = int(input())
print("Ingrese su numero:")

if numero_adivinado == cartas:
    print("Ganaste, regala 3 tragos")
else:
    print(f"Perdiste, el número fue {cartas}, tomas {abs(cartas - numero_adivinado)} ")    