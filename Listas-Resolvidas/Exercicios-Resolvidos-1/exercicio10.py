'''
Exercício 10:
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.

'''

numCigarros = int(input('Quantos cigarros você fuma por dia? '))
numAnos = float(input('Você fuma há quantos anos? '))

diasPerdidos = (numAnos * 365 * numCigarros * 600)/86400

print(f'Você perdeu um total de {diasPerdidos: .1f} dias de vida por fumar.')

