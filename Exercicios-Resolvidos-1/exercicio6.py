'''
Exercicio 6:
Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem.
'''

distancia = float(input('Informe a distância a percorrer (km): '))
velocidade = float(input('Informe a velocidade média do trajeto (km/h): '))
tempo = distancia/velocidade
print(f'Tempo de viagem estimado: {tempo: .2f} horas.')
