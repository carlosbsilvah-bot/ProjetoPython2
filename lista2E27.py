# Declarar

cont:int = 0
res:float = 0

# Inicio

for cont in range(1, 16, 1):

    if (cont % 2 != 0):
        res = res + (cont / (cont * cont))

    elif (cont % 2 == 0):
        res = res - (cont / (cont * cont))

print('O resultado da série é:', res)

# Fim