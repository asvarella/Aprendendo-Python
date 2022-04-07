'''Exercício 4:
Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.
'''

#Garantindo corretude dos dados:
negativo = True
while negativo:
    n = int(input('Número inteiro positivo: '))
    if(n > 0):
        negativo = False

fator = 2
#loop de fatoração:
while n != 1:
    mult = 0
    while n % fator == 0:
        n = n / fator
        mult = mult + 1
    if mult != 0:
        print(f'Fator {fator} multiplicidade {mult}')
    fator = fator + 1


    
    

