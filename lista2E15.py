#Declarar

cont:int = 0
res:float = 0
num:int = 0

#Inicio

num = int(input('Digite um número para seguir a série : '))
# Para o contador num comprimento de 10 a 150, suba 1 número

for cont in range (1, num + 1, 1):
    res = res + 1/cont
    print('o resultado da sério é:', res)

#Fim