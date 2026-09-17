# Declarar
numVoltas:int = 0
extMetros:float = 0.0
tempoMinutos:float = 0.0
distanciaKm:float = 0.0
tempoHoras:float = 0.0
velocidadeMedia:float = 0.0

# Pede os dados da corrida para o usuário
numVoltas = int(input("Digite o número de voltas: "))
extMetros = float(input("Digite a extensão do circuito em metros: "))
tempoMinutos = float(input("Digite o tempo de duração em minutos: "))

# Verifica se o tempo ou a distância são válidos para evitar divisão por zero
if (numVoltas > 0 and extMetros > 0 and tempoMinutos > 0):
    distanciaKm = (numVoltas * extMetros) / 1000
    tempoHoras = (tempoMinutos / 60)
    velocidadeMedia = (distanciaKm / tempoHoras)
    print("A velocidade média é:", velocidadeMedia, "km/h")
else:
    print("Dados inválidos")
