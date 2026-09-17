# Declarar

num:int = 0
cont:int = 0
ant:int = 1
atual:int = 1
prox:int = 0

# Inicio

num = int(input('Digite a quantidade de termos da série de Fibonacci: '))

for cont in range(1, num + 1, 1):

    print(atual)

    prox = ant + atual
    ant = atual
    atual = prox

# Fim