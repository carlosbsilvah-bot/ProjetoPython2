# Declarar

num:int = 0
cont:int = 0
fat:int = 1
res:float = 1

# Inicio

num = int(input('Digite um número: '))

for cont in range(1, num + 1, 1):
    fat = fat * cont
    res = res + (1 / fat)

print('O resultado da série é:', res)

# Fim