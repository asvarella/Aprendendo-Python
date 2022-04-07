'''
Exercício 11:
Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
a um milhão.
'''

num = 2 ** 1000000
texto = str(num)
print(len(texto))
