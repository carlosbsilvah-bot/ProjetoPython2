#Declarar

num:int = 0
cont:int = 0
res:int = 1

#Inicio

# Pede o valor de fatoria para o usuário
num = int(input('Digite um número para fatoriar: '))

# Vai fazer um laço de repetição que vai diminuir o valor que o usuário digitou até 1
for cont in range (num, 0, -1):

    # 1 = 1 * 4
    # 4 = 4 * 3
    # 12 = 12 * 2
    # 24 = 24 * 1
    # 24 
    res = res * cont
    print(res)

#Fim