# Declar

numero:int = 0
divDois:int = 0
divTres:int = 0
# Inicio

# Pede os valores para o usuário
numero= int((input('Digite um número para saber se é divisível por 2 ou 3: ')))


# Procura o menor valor
if (numero % 2 == 0): # Se for divisível apenas por 2
  print('o numero', numero, 'é divisível por 2')
elif (numero % 3 == 0): # Se for divisível apenas por 3
  print('o numero', numero, 'é divisível por 3')

else:
  print('o numero', numero, 'não é divisível por 2 nem por 3')
# Fim