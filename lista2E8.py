# Declarar
minutosInicio:int = 0
minutoInicio:int = 0
minutosFim:int = 0
horaInicio:int = 0
horaFim:int = 0
minutoFim:int = 0

#Inicio

# Pede a hora/minuto inicial e final do jogo 
horaInicio = int(input("Digite a hora de início: "))
minutoInicio = int(input("Digite o minuto de início: "))
horaFim = int(input("Digite a hora de término: "))
minutoFim = int(input("Digite o minuto de término: "))

minutosInicio = (horaInicio * 60) + minutoInicio
minutosFim = (horaFim * 60) + minutoFim

# Calcula a duração bruta
duracaoMinutos = minutosFim - minutosInicio

# Se a duração deu negativa, somamos 24 horas em minutos (1440 minutos)
if (duracaoMinutos < 0):
    duracaoMinutos += 1440

# Converte o resultado final para Horas e Minutos
horasFinais = (duracaoMinutos // 60)
minutosFinais = (duracaoMinutos % 60) 

print("O jogo durou:", horasFinais, "horas e", minutosFinais, "minutos")
#Fim