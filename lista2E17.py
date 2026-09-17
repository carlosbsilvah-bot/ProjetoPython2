# Declarar

num1:int = 0
num2:int = 0
cont:int = 0
maior:int = 0
menor:int = 0
res:int = 0

# Inicio

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if (num1 > num2):
    maior = num1
    menor = num2
elif (num2 > num1):
    maior = num2
    menor = num1
else:
    maior = num1
    menor = num2

for cont in range(menor, maior + 1, 1):
    if (cont % 2 != 0):
        res = res + cont
        print('O maior número é:', maior)
        print('A somatória dos números ímpares é:', res)

# Fim