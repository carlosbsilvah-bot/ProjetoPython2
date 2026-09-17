#Declarar

precoAtual:float = 0
mediaMensal:float = 0
reajuste:float = 0

#Inicio

# Pede os valores ao usuário de preço e media mensal
precoAtual = float(input('Digite o preço atual do produto: '))
mediaMensal = float(input('Digite a media mensal de venda do produto: '))

# Confere como a tabela que o professor passou e já faz o reajuste de 10%, 15% e -5%
if (mediaMensal < 500 and precoAtual < 30.00):
    reajuste =  (precoAtual * 10 / 100)
    reajuste = (precoAtual + reajuste)
    print('O novo valor reajustado para 10% é:', reajuste)
elif (mediaMensal >= 500 and mediaMensal < 1000 and precoAtual >= 30.00 and precoAtual < 80.00):
    reajuste =  (precoAtual * 15 / 100)
    reajuste = (precoAtual + reajuste)
    print('O novo valor reajustado para 15% é:', reajuste)
elif (mediaMensal >= 1000 and precoAtual >= 80.00):
    reajuste =  (precoAtual * 5/ 100)
    reajuste = (precoAtual - reajuste)
    print('O novo valor reajustado para -5% é:', reajuste)
else:
    print('O valor permanece o mesmo', precoAtual)

#Fim