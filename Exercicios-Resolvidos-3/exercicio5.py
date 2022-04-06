'''Exercício 5:
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.

ALGORITMO DE EUCLIDES:
O algoritmo de Euclides é baseado no princípio de que o MDC não muda se o menor número for subtraído ao maior. 
Por exemplo, 21 é o MDC de 252 e 105 (252 = 21 × 12; 105 = 21 × 5); já que 252 − 105 = 147, o MDC de 147 e 105 é também 21.
'''

a = int(input('N1: '))
b = int(input('N2: '))
#encontrando mdc entre n1 e n2
while b != 0:
    r = a % b
    a = b
    b = r
print(f'Máximo divisor comum é {a}')




