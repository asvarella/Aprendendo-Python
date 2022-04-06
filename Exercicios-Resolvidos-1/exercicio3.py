'''
Exercício 3:
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.
'''

dias = int(input('Informe quantos dias se passaram: '))
horas = int(input('Informe quantas horas se passaram: '))
minutos = int(input('Informe quantos minutos se passaram: '))
segundos = int(input('Informe quantos segundos se passaram: '))

totalSegundos = segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos equivalem a {totalSegundos} segundos.')
