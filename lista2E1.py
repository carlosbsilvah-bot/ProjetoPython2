# Declar

numeroUm:int = 0
numeroDois:int = 0
res:int = 0
# Inicio

# Pede os valores para o usuário
numeroUm= int((input('Digite o primeiro valor para saber a diferente entre o maior e o menor')))
numeroDois= int((input('Digite o segundo valor para saber a diferente entre o maior e o menor')))

# Procura o menor valor
if (numeroUm > numeroDois): # Se o primeiro número for menor que o segundo faça
  res = numeroUm - numeroDois # Calculo da diferença
  print('a diferente entre', numeroUm, 'para o', numeroDois, 'é:', res)
else: # Se não, só pode ser o contrário o segundo número é maior que o primeiro
  res = numeroDois - numeroUm 
  print('a diferente entre', numeroDois, 'para o', numeroUm, 'é:', res)
# Fim