# Declarar

ana:float = 1.10
maria:float = 1.50
anos:int = 0

# Inicio

for anos in range(1, 101, 1):

    ana = ana + 0.03
    maria = maria + 0.02

    if (ana > maria):
        print('Serão necessários', anos, 'anos.')
        break

# Fim