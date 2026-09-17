# Declarar

cont:int = 0
res:float = 0
den:int = 1

# Inicio

for cont in range(1, 51, 1):

    res = res + (cont / den)

    den = den + 2

print('O resultado da série é:', res)

# Fim