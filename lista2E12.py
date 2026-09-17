#Declarar

investimento:int = 0
valorInvestimento:float = 0
reajuste:float = 0
#Inicio

# Pede ao usuário a opção aonde ele deseja investir e o valor que ele vai deixar para investir
investimento = int(input("Digite 1 para investir na poupança ou 2 para renda fixa: "))
valorInvestimento = float(input("Digite o valor para o investimento: "))

# Ao escolher a opção ele faz o rejuste que a opção oferece escolhido
if(investimento == 1):
    reajuste = (valorInvestimento * 3 / 100)
    valorInvestimento = valorInvestimento + reajuste
    print('Após 30 dias seu valor investido rendeu 3%', valorInvestimento, 'é o valor atual da conta')
elif(investimento == 2):
    reajuste = (valorInvestimento * 5 / 100)
    valorInvestimento = valorInvestimento + reajuste
    print('Após 30 dias seu valor investido rendeu 5%', valorInvestimento, 'é o valor atual da conta')
else:
    print('Opção invalida, digite 1 ou 2 para prosseguir')