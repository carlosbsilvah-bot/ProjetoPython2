# Declar

a:float = 0
b:float = 0
c:float = 0
delta:float = 0
resUm:float = 0
resDois:float = 0

# Inicio

# Pede os valores para o usuário
a= float((input('Digite o primeiro valor para a equação: ')))
b= float((input('Digite o segundo valor para a equação:')))
c= float((input('Digite o terceiro valor para a equação: ')))

delta = (b ** 2) - (4 * a * c)


# Se for maior ou igual a 0 é porque tem raiz, independente se for raiz igual ou não
if (delta >= 0): # Se o primeiro número for maior que o segundo faça
  resUm = (-b + (delta ** 0.5)) / (2 * a)
  resDois = (-b - (delta ** 0.5)) / (2 * a)
  print('O valor da primeira raiz é:', resUm, 'e a segunda raiz é: ', resDois)
else: # Não tem raiz porque é menor que 0
  print('Não existem raízes reais')
# Fim