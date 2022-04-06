'''Faça um programa que leia uma palavra e troque as vogais por *
STRINGS SÃO IMUTÁVEIS
    texto = 'Alo Mundo'
    texto = '@' + texto[1:]
    print(texto)
    saída esperada: '@lo Mundo'
'''

palavra = input('Palavra: ')
k = 0
troca = ''

while k < len(palavra):
    if palavra[k] in 'aeiou': #se encontra uma das vogais, adiciona um asterisco
        troca = troca + '*'
    else:  #caso contrário, adiciona caractere da string de entrada
        troca = troca + palavra[k]
    k = k + 1
print(troca)
