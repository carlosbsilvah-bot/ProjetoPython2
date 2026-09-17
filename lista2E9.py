# Declar

numeroUm:int = 0
numeroDois:int = 0
# Inicio

# Pede os valores para o usuário
numeroUm= int((input('Digite o primeiro valor para saber se o maior número é divisível pelo menor: ')))
numeroDois= int((input('Digite o segundo valor para saber se o maior número é divisível pelo menor: ')))

# Procura o menor valor
if (numeroUm > numeroDois): # Se o primeiro número for maior que o segundo faça
    if(numeroUm % numeroDois == 0):
        print('O', numeroUm,'é maior e é divisível por', numeroDois)
    else:
       print('o número:', numeroUm, 'é maior e não é divisel por', numeroDois)
elif (numeroDois > numeroUm): # Se não, só pode ser o contrário o segundo número é maior que o primeiro faça
    if(numeroDois % numeroUm == 0):
          print('O', numeroDois,'é maior e é divisível por', numeroUm)
    else:
         print('o número:', numeroDois, 'é maior e não é divisel por', numeroUm)
# Fim