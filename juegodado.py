import random

dado = random.randint(1,6)

if dado >= 3:
    print(f"Ganaste, el numero fue {dado}")
else:
    print(f"Perdiste, el numero fue {dado}")
