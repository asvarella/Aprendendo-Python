'''Exercício 3:
Verifique se um inteiro positivo n é primo
NUMEROS PRIMOS: divisíveis apenas por 1 e por eles mesmos
'''
#Garantindo corretude dos dados:
negativo = True
while negativo:
    n = int(input('Número inteiro positivo: '))
    if(n > 0):
        negativo = False

divisores = 0
k = 1

while (k <= n and divisores <= 2):
    if(n % k == 0):
        divisores = divisores + 1
    k = k + 1

if divisores == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')
