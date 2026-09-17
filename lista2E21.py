# Declarar

cont:int = 0
qtd:float = 1
res:float = 0

# Inicio

for cont in range(1, 65, 1):

    res = res + qtd
    qtd = qtd * 2

print('A quantidade de grãos no tabuleiro é:', res)

# Fim