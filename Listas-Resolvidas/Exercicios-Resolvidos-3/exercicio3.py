'''Exercicio 3:
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento'''

popA = 80000
popB = 200000
anos = 0
while popA < popB:
    popA = popA + popA * 0.03
    popB = popB + popB * 0.015
    anos = anos + 1

print(f'População do país A: {int(popA)}\nPopulação do país B: {int(popB)}\nAnos que passaram: {anos}')