#Declarar

primValor:int = 0
segValor:int = 0
terValor:int = 0
quaValor:int = 0


#Inicio

# Pede os valores para o usuário
primValor = int(input('Digite o primeiro valor em ordem crescente: '))
segValor = int(input('Digite o segundo valor em ordem crescente: '))
terValor = int(input('Digite o terceiro valor em ordem crescente: '))
quaValor = int(input('Digite o quarto valor pode ser um número qualquer: '))

#Ve se é menor de todos, segundo menor, terceiro menor ou maior de todos

if (quaValor < primValor and quaValor < segValor and quaValor < terValor): #menor de todos
    print('Em ordem crescente é:', quaValor,',',primValor,',',segValor,',',terValor)
elif (quaValor > primValor and quaValor < segValor and quaValor < terValor): #segundo menor
    print('Em ordem crescente é:',primValor,',',quaValor, ',', segValor,',',terValor)
elif (quaValor > primValor and quaValor > segValor and quaValor < terValor): # terceiro menor
    print('Em ordem crescente é:',primValor,',',segValor, ',', quaValor,',',terValor)
else: # maior de todos
    print('Em ordem crescente é:',primValor,',',segValor, ',', terValor,',',quaValor)

