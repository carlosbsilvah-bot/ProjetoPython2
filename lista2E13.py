#Declarar

cont:int = 0
res:int = 0

#Inicio

# Para o contador em um comprimento de 10 a 150, suba 1 número
for cont in range (10, 151, 1):

    #resultado pega o quadrado dos números de 10 até 150
    res = cont ** 2
    print('o quadrado de', cont, 'é:', res)

#Fim