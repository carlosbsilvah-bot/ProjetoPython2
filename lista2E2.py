# Declar

numeroUm:int = 0
numeroDois:int = 0
# Inicio

# Pede os valores para o usuário
numeroUm= int((input('Digite o primeiro valor para saber o maior número: ')))
numeroDois= int((input('Digite o segundo valor para saber o maior número: ')))

# Procura o menor valor
if (numeroUm > numeroDois): # Se o primeiro número for maior que o segundo faça
  print('o número:', numeroUm, 'é maior que o', numeroDois)
else: # Se não, só pode ser o contrário o segundo número é maior que o primeiro faça
  print('o número:', numeroDois, 'é maior que o', numeroUm)
# Fim