#Declarar

cont:int = 0
res:float = 0
num:int = 0

#Inicio

num = int(input('Digite um número para fazer sua tabuada: '))
# Para o contador em um comprimento de 0 a num, suba 1 número
for cont in range (0, 11, 1):
    #faz a tabuada do número passado
    res = num * cont
    print(num,'x', cont,'=', res)

#Fim