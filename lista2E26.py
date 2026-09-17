# Declarar

base:int = 0
expoente:int = 0
cont:int = 0
res:int = 1

# Inicio

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

for cont in range(1, expoente + 1, 1):

    res = res * base

print('O resultado da potência é:', res)

# Fim