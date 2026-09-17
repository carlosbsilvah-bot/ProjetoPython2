#Declarar
prim:float = 0
seg:float = 0
terc:float = 0
quar:float = 0
media:float = 0

#Inicio

# Pede as notas para o usuário
prim = float(input('Digite a nota do primeiro bimestre: '))
seg = float(input('Digite a nota do segundo bimestre: '))
terc = float(input('Digite a nota do terceiro bimestre: '))
quar = float(input('Digite a nota do quarto bimestre: '))

# Calcula a média
media = (prim + seg + terc + quar) /  4

# Ve se o aluno foi aprovado ou não
if (media > 6):
    print('Parabéns, você foi APROVADO!')
elif (media > 3 and media < 6):
    print('Realizar EXAME')
else:
    print('Sinto muito, você foi RETIDO')

#Fim