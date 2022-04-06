'''Exercícios de fixação sobre listas/arrays em python'''

#Calculando média dos alunos

notas = []

#primeira versão: usando dois whiles, um para adicionar elementos no array e outro para cálculo da média
'''
k = 1
while k <= 4:
    notas.append(float(input('Insira a nota: ')))
    k = k + 1
soma = k = 0
while k <= 3:
    soma = soma + notas[k]
    k = k + 1
print(f'Média {notas} é {soma/4: .2f}')'''


#fazendo o código de maneira mais eficiente
soma = k = 0

while k <= 3:
    notas.append(float(input('Insira a nota: ')))
    soma = soma + notas[k]
    k = k + 1
print (f'Média {notas} é {soma/4: .2f}')
