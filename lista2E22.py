# Declarar

num1:int = 0
num2:int = 0
cont:int = 0
div:int = 0
primo:int = 1

# Inicio

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

for cont in range(num1, num2 + 1, 1):

    primo = 1

    for div in range(2, cont, 1):

        if (cont % div == 0):
            primo = 0

    if (primo == 1 and cont > 1):
        print(cont)

# Fim