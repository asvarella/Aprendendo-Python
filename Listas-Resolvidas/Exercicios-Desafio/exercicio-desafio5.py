'''Exercício 5:
Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321'''

#Garantindo corretude dos dados:
negativo = True
while negativo:
    n = int(input('Número inteiro positivo: '))
    if(n > 0):
        negativo = False

inv = 0 #variável que guardará o valor invertido
while n>0:
    digito = n % 10
    inv = inv * 10 + digito
    n = int(n / 10)

print(inv)
