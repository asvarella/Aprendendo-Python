'''
Exercício 2:
Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
'''

valor = float(input('Digite um valor: '))
valor_conv = valor * 1000
print(f'{valor} metros são {valor_conv: .2f} milímetros.')
