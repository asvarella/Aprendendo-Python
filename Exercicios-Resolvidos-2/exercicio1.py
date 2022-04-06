'''Exercício 1:
Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

DEFINIÇÃO DE TRIÂNGULO:
    "A soma das medidas de dois lados é sempre maior que a medida do terceiro."
    
    TRIÂNGULO ESCALENO:
        Três lados com medidas diferentes.
    TRIÂNGULO ISÓSCELES:
        Dois lados com a mesma medida.
    TRIÂNGULO EQUILÁTERO:
        Três lados com a mesma medida.
'''

a = int(input('Lado 1: '))
b = int(input('Lado 2: '))
c = int(input('Lado 3: '))


if ((a + b > c) and (b + c > a) and (a + c > b)):
    if((a == b) and (a == c)): #subentende-se que b == c
        print ('É um triângulo equilátero!')
    elif((a == b) or (a == c) or (b == c)): #pelo menos dois lados são iguais
        print ('É um triângulo isósceles!')
    else:
        print ('É um triângulo escaleno!')
else:
    print ('Não é um triângulo!')