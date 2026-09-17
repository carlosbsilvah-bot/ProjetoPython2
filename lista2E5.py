#Declarar

primValor:int = 0
segValor:int = 0

#Inicio

# Pede os valores para o usuário
primValor = int(input('Digite o primeiro valor: '))
segValor = int(input('Digite o segundo valor: '))

# Se o primeiro valor for maior então mostre o menor e depois o maior
if (primValor > segValor):
    print('Em ordem crescente é:', segValor,',',primValor)
else: # Se não o segundo valor é maior, então mostre o menor e depois o maior
    print('Em ordem decrescente é:', primValor,',', segValor)

