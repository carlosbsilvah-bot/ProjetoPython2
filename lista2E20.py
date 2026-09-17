# Declarar

num:float = 0
maior:float = 0
menor:float = 0
cont:int = 0

# Inicio

for cont in range(1, 101, 1):

    num = float(input('Digite um número positivo: '))

    if (num > 0):

        if (cont == 1):
            maior = num
            menor = num

        elif (num > maior):
            maior = num

        elif (num < menor):
            menor = num

print('O maior valor é:', maior)
print('O menor valor é:', menor)

# Fim