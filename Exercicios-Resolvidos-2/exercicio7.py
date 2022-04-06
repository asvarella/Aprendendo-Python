'''Exercício 7:
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
'''
tam = float(input('Informe a área (m^2): '))
numLitros = tam / 3
numLatas = int(numLitros / 18)

if(numLitros % 18 != 0):
    numLatas = numLatas + 1

print (f'Total de latas a comprar: {numLatas}\nPreço total: R$ {numLatas*80: .2f}')


